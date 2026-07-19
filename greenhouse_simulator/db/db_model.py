
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session



DATABASE_URL = "postgresql://greenhouse_user:greenhouse_secure_pass@localhost:5432/greenhouse_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class DBTargetSensor(Base):
    __tablename__ = "sensors"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    temperature = Column(Float, default=0.0)
    humidity = Column(Float, default=0.0)
    light = Column(Float, default=0.0) 
    critical_humidity = Column(Float, default=30.0)
    status = Column(String, default="active")
    critical_temperature = Column(Float, default=30.0)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
