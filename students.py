
students = []

def add_student(name):
    students.append(name)
    print("Студент добавлен:", name)


def show_students():
    print("Список студентов:")

    for student in students:
        print(student)
