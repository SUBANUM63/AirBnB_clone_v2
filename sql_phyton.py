#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    f'mysql+pymysql://{os.environ["HBNB_MYSQL_USER"]}:{os.environ["HBNB_MYSQL_PWD"]}@localhost/hbnb_dev_db'
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
