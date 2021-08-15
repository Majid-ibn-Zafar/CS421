from main import db, Student
import random
import string


print_students = Student.query.all()

firstStudent = Student.query.get(1)

print(print_students)
