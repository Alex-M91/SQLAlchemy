from sqlalchemy import create_engine
from models import Base, Student
from secrets import host, user, password

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING.format(host=host, user=user, password=password, db="default")
)
Base.metadata.create_all(eng)
