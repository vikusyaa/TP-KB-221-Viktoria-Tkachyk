students = [
    {'name': "Анна", 'grade': 90},
    {'name': "Віктор", 'grade': 80},
    {'name': "Софія", 'grade': 60},
    {'name': "Михайло", 'grade': 85},
    {'name': "Олександра", 'grade': 100}
]

reverse_sort = input("Сортувати від меншого до більшого? (так/ні): ").lower()

reverse = False
if reverse_sort == 'ні':
    reverse = True


sorted_students_by_name = sorted(students, key=lambda x: x['name'])
print("Сортування за ім'ям:")
for student in sorted_students_by_name:
    print(student)



sorted_students_by_grade = sorted(students, key=lambda x: x['grade'])
print("\nСортування за оцінкою:")
for student in sorted_students_by_grade:
    print(student)