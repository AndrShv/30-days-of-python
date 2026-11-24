import asyncio
from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from db_models import Base, DBUser, DBLog
from unit_of_work import UnitOfWork


def print_orm_state(obj: Base, stage: str):
    state = inspect(obj)
    print(f"[{stage}] State of {obj.__class__.__name__}: "
          f"Transient={state.transient}, Pending={state.pending}, "
          f"Persistent={state.persistent}, Detached={state.detached}")


async def main():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(lambda sync_conn: Base.metadata.create_all(sync_conn))

    session_factory = async_sessionmaker(engine, expire_on_commit=False)

    async with UnitOfWork(session_factory) as uow:
        new_user = DBUser(username="Alex")
        print_orm_state(new_user, "1. After Instantiation")  # Transient

        await uow.users.create_user(new_user)
        print_orm_state(new_user, "2. After uow.users.create_user()")  # Pending

        log1 = DBLog(event_id=1, payload="processed_payload_1", user=new_user)
        log2 = DBLog(event_id=2, payload="processed_payload_2", user=new_user)
        await uow.logs.create_log(log1)
        await uow.logs.create_log(log2)

    print_orm_state(new_user, "3. After UoW Commit")

    async with UnitOfWork(session_factory) as uow:
        print("\n--- Выборка юзеров вместе с логами (selectinload) ---")
        users = await uow.users.get_all_with_logs()
        for user in users:
            print(f"User: {user.username}, Logs count: {len(user.logs)}")
            for l in user.logs:
                print(f"  - Log {l.event_id}: {l.payload}")


if __name__ == "__main__":
    asyncio.run(main())