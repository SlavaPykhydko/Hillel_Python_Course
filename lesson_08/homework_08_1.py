class Student:


    def __init__(self, name, surname, avg_grade):
        self.name = name
        self.surname = surname
        self.avg_grade = avg_grade

    def change_avg_grade(self, avg_grade):
        self.avg_grade = avg_grade

student_1 = Student(name='Slava', surname='Pykhydko', avg_grade=100)

print(f'Student with name {student_1.name} '
      f'and surname {student_1.surname} and average grade {student_1.avg_grade}')

student_1.change_avg_grade(80)

print(f'Student"s average grade after change {student_1.avg_grade}')