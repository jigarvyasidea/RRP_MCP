# this file handel the database connections 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# ese url hum kabhi nahi dete this is bad practive anyonce can see this on github or somewhere else 
# in future we will changed it.
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:123456@localhost/dummydb'
# now we create enginer this engine is responsisible to connect sql achemy to postgrees 
engine  = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False , autocommit = False , bind=engine)
# now we need to create out base class 
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()