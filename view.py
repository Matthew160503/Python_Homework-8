import addstudent
import addtask

def select_operation():
    operation = int(input('\n1 - Добавить студента\n2 - Добавление предмета\n'+
    '3 - Добавление оценки ученику по предмету\n4 - Показ списка учеников\n'+
    '5 - Показ листа оценок конкретного ученика\n6 - Выход из программы\n'))
    return operation

students = {}
tasks = []
names = []

def add_student():
    student = addstudent.new_student()
    global students, tasks, names
    if student not in names:
        names.append(student)
        students[student] = {}
    print(f'Ученик {student} добавлен в список школы')

def add_task():
    task = addtask.new_task()
    global students, tasks, names
    if task not in tasks:
        tasks.append(task)
        for name in names:
            students[name][task] = []

def add_mark():
    global students, tasks, names
    student = addstudent.new_student()
    task = addtask.new_task()
    mark = int(input('Введите оценку: '))
    students[student][task].append(mark)

def view_journal():
    print(students)

def view_marks():
    global students, tasks, names
    student = addstudent.new_student()
    task = addtask.new_task()
    print(f'Оценки выбранного ученика: {students[student][task]}')

