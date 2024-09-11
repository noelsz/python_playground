import os


def to_do_menu(tasks):
    print("1. Add a task \n2. Remove a task \n3. List all tasks \n")
    choice = int(input("Enter your choice: "))
    if choice:
        match choice:
            case 1:
                return add_task(tasks)
            case 2:
                return remove_task(tasks)
            case 3:
                return list_tasks(tasks)
            case _:
                print("Invalid choice, returning to menu...\n")
                return to_do_menu(tasks)
    else:
        print("Exiting program upon no choice.")
        return



def add_task(tasks):

    print("What do you want to add?")
    task_name = input("Name of the task: ")
    task_description = (input("A short description of the task: "))
    print()
    tasks.update({task_name: task_description})

    os.system('cls')
    to_do_menu(tasks)


def remove_task(tasks):
    print("Which task would you like to remove?")
    task_name = input("Name of the task: ")
    print()
    del tasks[task_name]
    os.system('cls')
    to_do_menu(tasks)


def list_tasks(tasks):
    for key, value in tasks.items():
        print(f"{key} : {value}")
    input("Press any key to continue...")
    os.system('cls')
    to_do_menu(tasks)

to_do_list = {}
to_do_menu(to_do_list)