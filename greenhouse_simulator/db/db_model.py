import uuid

from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session



DATABASE_URL = "postgresql://greenhouse_user:greenhouse_secure_pass@localhost:5432/greenhouse_db"
#docker exec -it greenhouse_postgres psql -U greenhouse_user -d greenhouse_db
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class DBTargetSensor(Base):
    __tablename__ = "greenhouse_sensors"
    id = Column(
        String,
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )
    name = Column(String, unique=True, index=True, nullable=False)
    temperature = Column(Float, default=0.0)
    humidity = Column(Float, default=0.0)
    light = Column(Float, default=0.0) 
    critical_humidity = Column(Float, default=30.0)
    status = Column(String, default="active")
    critical_temperature = Column(Float, default=30.0)



class DBUser(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
