from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./Kakeibo.db"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#セッション
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()