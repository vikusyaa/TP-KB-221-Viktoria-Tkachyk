class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Bob", 22),
    Student("Anna", 19),
    Student("Nik", 14)
]

for student in sorted(students, key=lambda s: s.name):
    print(student.name, student.age)

