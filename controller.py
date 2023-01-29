import view

def start():
    while (True):
        text_operation = view.select_operation()
        if text_operation == 1:
            view.add_student()
        elif text_operation == 2:
            view.add_task()
        elif text_operation == 3:
            view.add_mark()
        elif text_operation == 4:
            view.view_journal()
        elif text_operation == 5:
            view.view_marks()
        elif text_operation == 6:
            print('Программа завершена!')
            break