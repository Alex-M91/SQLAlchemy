from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy import create_engine
from models import Base, Grades, Student
from secrets import host, user, password
from sqlalchemy.orm import sessionmaker


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
            Grades(student=1, grade=5),
            Grades(student=2, grade=7),
            Grades(student=3, grade=4),
            Grades(student=4, grade=3),
            Grades(student=5, grade=8),
            Grades(student=6, grade=9),
            Grades(student=7, grade=6),
            Grades(student=8, grade=4),
            Grades(student=9, grade=6),

        ]
    )
    s.commit()

except IntegrityError:
    s.rollback()
    print("Grades already created !")
rows = s.query(Student, Grades).join(Grades).filter(Grades.grade == 6)
for row in rows:
    student, grades = row
    print(f"Student with grade #{grades.grade}: {student}")
