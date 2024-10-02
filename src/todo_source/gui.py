from tkinter import Tk, Listbox, Button, Entry, StringVar, OptionMenu, Label
from .task_manager import TaskManager

# Initialize the main Tkinter window
root = Tk()
root.title("todo-mgr")
root.geometry("400x450")

# Task Manager Initialization
task_manager = None

# Create a category selection dropdown
category_var = StringVar(root)
category_var.set("Casual")  # Default category
categories = ["Casual", "Work", "Personal", "School"]

def on_category_change(*args):
    global task_manager
    task_manager = TaskManager(category_var.get())
    task_manager.load_tasks()
    update_task_listbox(task_manager.tasks)

category_var.trace("w", on_category_change)

# Create the category dropdown menu
category_menu = OptionMenu(root, category_var, *categories)
category_menu.pack()

# Task listbox
task_listbox = Listbox(root)
task_listbox.pack()

# Task entry
task_entry = Entry(root)
task_entry.pack()

# Deadline entry
deadline_label = Label(root, text="Deadline (optional, format: YYYY-MM-DD):")
deadline_label.pack()
deadline_entry = Entry(root)
deadline_entry.pack()

# Update the task listbox with tasks
def update_task_listbox(tasks):
    task_listbox.delete(0, 'end')  # Clear the current tasks
    for task, deadline in tasks:
        task_listbox.insert('end', f"{task} (Due: {deadline})")

# Load tasks for the default category
task_manager = TaskManager(category_var.get())
task_manager.load_tasks()
update_task_listbox(task_manager.tasks)

# Function to add a task
def add_task():
    task = task_entry.get()
    deadline = deadline_entry.get() or "No deadline"  # Use "No deadline" if no input
    if task:
        task_manager.add_task(task, deadline)
        update_task_listbox(task_manager.tasks)
        task_entry.delete(0, 'end')
        deadline_entry.delete(0, 'end')

add_task_button = Button(root, text="Add Task", command=add_task)
add_task_button.pack()

# Function to remove a task
def remove_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection()).split(" (Due: ")[0]  # Extract task without deadline
        task_manager.remove_task(selected_task)
        update_task_listbox(task_manager.tasks)
    except:
        pass  # Handle no task selected

remove_task_button = Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack()

# Start the Tkinter main loop
root.mainloop()
