import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv

load_dotenv()
# подключение к базе данных
DATABASE_URL = f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@localhost/{os.getenv("POSTGRES_DB")}'

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
    engine = create_engine(DATABASE_URL)
except Exception as e:
    print(f"Ошибка при создании соединения: {e}")


def init_db():
    """Инициализация базы данных: создание всех таблиц."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """ Подключение к базе данных """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
