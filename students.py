from sqlalchemy import create_engine
from models import Base, Student
from secrets import host, user, password
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(    # engine stie unde e baza de date
    CONNECTION_STRING.format(host=host, user=user, password=password, db="default")
)

Session = sessionmaker(bind=eng)    # leaga-te la enginu respectiv
s = Session()

s.add_all(  # functia add care poate adauga un singur obiect sau add_all care adauga mai multe obiecte
    [
        Student(first_name="Mike", last_name="Wazowski"),
        Student(first_name="Netti", last_name="Nashe"),
        Student(first_name="Jessamine", last_name="Addison"),
        Student(first_name="Brena", last_name="Bugdale"),
        Student(first_name="Theobald", last_name="Oram"),
        Student(first_name="Alex", last_name="Mihaescu"),
        Student(first_name="Mihai", last_name="Crudu"),
        Student(first_name="Mihai", last_name="Gavrila"),
        Student(first_name="Iustin", last_name="Cezar"),
    ]
)
s.commit()  # in momentul in care ii dam comit datele sunt trimise in data de baze si stocate in workbench
