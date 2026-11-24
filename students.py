
students = []

def add_student(name):
    students.append(name)
    print("Студент добавлен:", name)


def show_students():
    print("Список студентов:")

    for student in students:
        print(student)


def delete_student(name):
    if name in students:
        students.remove(name)
        print("Студент удалён:", name)
    else:
        print("Студент не найден")
