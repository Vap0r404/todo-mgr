import time

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for task in tasks:
            print(f"- {task}")

    # Prompt user to choose an option
    choose_option2()

def choose_option():
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    option = input("Enter your choice: ")
    handle_option(option)

def choose_option2():
    
    option = input("Enter your choice: ")
    handle_option(option)

def handle_option(option):
    if option == '1':
        add_task()
    elif option == '2':
        view_tasks(tasks)
    elif option == '3':
        remove_task()
    elif option == '4':
        print("Exiting todo-mgr.")
        exit()
    else:
        print("Invalid option. Please try again.")
        choose_option()

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
    choose_option()

def remove_task():
    view_tasks(tasks)
    task_to_remove = input("Enter the task to remove: ")
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        print(f"Task '{task_to_remove}' removed.")
    else:
        print(f"Task '{task_to_remove}' not found.")
    choose_option()

# Main program
tasks = []
print("Welcome to the To-Do List Manager!")

# Start the program by showing the menu
choose_option()

