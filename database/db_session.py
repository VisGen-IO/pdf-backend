from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from settings import DB_URL

engine = create_engine(DB_URL, pool_pre_ping=True, pool_size=20, max_overflow=10)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():    
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
