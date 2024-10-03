from tkinter import Tk, Listbox, Button, Entry, StringVar, OptionMenu, Label
from .task_manager import TaskManager

root = Tk()
root.title("todo-mgr")
root.geometry("400x350")

task_manager = None

category_var = StringVar(root)
category_var.set("Casual")
categories = ["Casual", "Work", "Personal", "School"]

def on_category_change(*args):
    global task_manager
    task_manager = TaskManager(category_var.get())
    task_manager.load_tasks()
    update_task_listbox(task_manager.tasks)

category_var.trace("w", on_category_change)

category_menu = OptionMenu(root, category_var, *categories)
category_menu.pack()

task_listbox = Listbox(root, width=50)
task_listbox.pack()

task_entry = Entry(root, width=50)
task_entry.pack()

deadline_label = Label(root, text="Deadline (optional, format=YYYY-MM-DD):", width=50)
deadline_label.pack()
deadline_entry = Entry(root)
deadline_entry.pack()

def update_task_listbox(tasks):
    task_listbox.delete(0, 'end')
    for task, deadline in tasks:
        task_listbox.insert('end', f"{task} (Due: {deadline})")

task_manager = TaskManager(category_var.get())
task_manager.load_tasks()
update_task_listbox(task_manager.tasks)

def add_task():
    task = task_entry.get()
    deadline = deadline_entry.get() or "No deadline"
    if task:
        task_manager.add_task(task, deadline)
        update_task_listbox(task_manager.tasks)
        task_entry.delete(0, 'end')
        deadline_entry.delete(0, 'end')

add_task_button = Button(root, text="Add Task", command=add_task)
add_task_button.pack()

def remove_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection()).split(" (Due: ")[0]
        task_manager.remove_task(selected_task)
        update_task_listbox(task_manager.tasks)
    except:
        pass

remove_task_button = Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack()

sort_var = StringVar(root)
sort_var.set("Sort by Name")
sort_options = ["Sort by Name", "Sort by Deadline"]

def on_sort_change(*args):
    if sort_var.get() == "Sort by Name":
        task_manager.sort_tasks_by_name()
    else:
        task_manager.sort_tasks_by_deadline()
    update_task_listbox(task_manager.tasks)

sort_var.trace("w", on_sort_change)

sort_menu = OptionMenu(root, sort_var, *sort_options)
sort_menu.pack()

root.mainloop()
