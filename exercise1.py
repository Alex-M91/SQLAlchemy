from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy import create_engine
from models import Base, Address, Student
from secrets import host, user, password
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc, desc

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING.format(host=host, user=user, password=password, db="default")
)
Base.metadata.create_all(eng)
Session = sessionmaker(bind=eng)
s = Session()
try:
    s.add_all(
        [
            Address(student=1, street_name="Stoneleigh Place", number=7, city= "Los Angeles"),
            Address(student=2, street_name="Old Town", number=3, city= "California"),
            Address(student=3, street_name="Orsman Place", number=5, city= "Ilinois"),
            Address(student=4, street_name="Chudleigh Street", number=2, city= "New York"),
            Address(student=5, street_name="Albemarle Way", number=11, city="Washington"),
            Address(student=6, street_name="Vasile Godlis", number=24, city="Alba"),
            Address(student=7, street_name="Muresului", number=2, city="Cugir"),
            Address(student=8, street_name="1 Decembrie", number=6, city="Orastie"),
            Address(student=9, street_name="Mihai Viteazu", number=8, city="Cluj Napoca"),

        ]
    )
    s.commit()

except IntegrityError:
    s.rollback()
    print("Address already created !")
rows = s.query(Student, Address).join(Address).filter(Address.number == 2)
for row in rows:
    student, address = row
    print(f"Student with address #{address.street_name}: {student}")

##   ORDER BY ASC
# ascending = s.query(Student, Address).join(Address).order_by(asc(Address.street_name))
# for row in ascending:
#     student, address = row
#     print(f"Addresses A-Z: {address.street_name}")

## ORDER BY DESC
# descending = s.query(Student, Address).join(Address).order_by(desc(Address.street_name))
# for row in descending:
#     student, address = row
#     print(f"Adreesses Z-A {address.street_name}")

## LIMIT -> first 3 students
# first3 = s.query(Student).filter(Student.id <= 3)
# for row in first3:
#     print(row)

##   UPDATE -> Address
# update_address = s.query(Address).filter(Address.street_name=="Mihai Viteazu")
# for row in update_address:
#     row.street_name = "Stefan Cel Mare"
#
# s.commit()

## DELETE
delete_address = s.query(Student).filter()