import uuid
from sqlalchemy import Column, String, Enum as SQLEnum
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from safecity_platform.models.categories import IncidentCategory, LawBreakingCategory

DATABASE_URL = "postgresql://greenhouse_user:greenhouse_secure_pass@localhost:5432/greenhouse_db"
#docker exec -it greenhouse_postgres psql -U greenhouse_user -d greenhouse_db
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class DBIncident(Base):
    __tablename__ = "incidents"
    id = Column(String,
                primary_key=True,
                index=True ,
                default=lambda: str(uuid.uuid4())
                )
    title = Column(String, index=True,
                   nullable=False)
    incident_category = Column(SQLEnum(IncidentCategory),
                      index=True,
                      nullable=False)
    law_breaking_category = Column(SQLEnum(LawBreakingCategory),
                                   default=LawBreakingCategory.STH_ELSE)

class DBUser(Base):
    __tablename__ = "users"
    id = Column(String,
                primary_key=True,
                default=lambda: str(uuid.uuid4())
                )
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1) Изменяешь Python-класс в db_model.py
# 2) PYTHONPATH=. alembic revision --autogenerate -m "имя_миграции"(можно без -m... так как просто коммит в файл)
# 3) Запускаешь PYTHONPATH=. alembic upgrade head.



