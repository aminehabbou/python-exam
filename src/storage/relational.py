from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

database_url = "mysql+pymysql://root:hello1@localhost:3345/exampyth"

engine = create_engine(database_url, echo=True, pool_size=5, max_overflow=10)


class Base(DeclarativeBase):
    pass


Session = sessionmaker(bind=engine)
