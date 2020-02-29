from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from secrets import *

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"
eng = create_engine(
        CONNECTION_STRING.format(host=host, user=user, password=password, db="default")
)
Session = sessionmaker(bind=eng)
s = Session()

rows = s.query(Student).all()   # SELECT * FROM Student
for row in rows:
    print(row)

print("---")
total = s.query(Student).count()    # SELECT COUNT(*) FROM Student
print(f"Total: {total}")

print("---")
# query_result = s.query(Student).filter(Student.id >= 2, Student.first_name.like("M%"))    # Select * FROM Student
# print("Found students:")                                                             # Where id >=2 AND first_name LIKE "Bre%";
# for row in query_result:
#     print(row)

# query_result_mih% = s.query(Student).filter(Student.last_name.like("Mih%"))
# for row in query_result_mih%:
#     print(row)

# query_result_id1 = s.query(Student).filter(Student.id == 1)
# for row in query_result_id1:
#     print(row)

# query_result_last_name = s.query(Student).filter(Student.last_name.like("Cezar"))
# for row in query_result_last_name:
#     print(row)

## s.query , unde s = Session si poate fi scris si Session.query
#alex = s.query(Student).filter(Student.first_name=="Alex").first()    # functia first ne returneaza doar primul rand gasit cu acel nume
## Set new last name
#alex.last_name = "M"
## Commit the change to the database
#s.commit()

## Use multiple Students
# Mihai_2 = s.query(Student).filter(Student.first_name=="Mihai")  # toti studentii cu numele Mihai vor fi modificati
# for Mihai in Mihai_2:
#     Mihai.first_name = "Mihaitza"
#
# s.commit()

Mihai_c2 = s.query(Student).filter(Student.first_name=="Mihaitza").first()
Mihai_c2.first_name = "Mihai"

s.commit()
