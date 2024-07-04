from .connection import get_engine
from core.config import config
import models

from sqlalchemy.orm import Session, sessionmaker

engine = get_engine(drivername=config.DB_DRIVERNAME, 
                      host=config.DB_HOST,
                      user=config.DB_USER,
                      password=config.DB_PASSWORD,
                      port=config.DB_PORT,
                      database=config.DATABASE,
                      )
    
models.Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


'''
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''