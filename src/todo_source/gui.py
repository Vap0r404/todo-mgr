import tkinter as tk
from tkinter import messagebox
from .task_manager import TaskManager  # Using relative import

# Initialize the task manager with file persistence
manager = TaskManager()

# Function to add tasks
def add_task():
    task = task_entry.get()
    if task:
        manager.add_task(task)
        task_entry.delete(0, tk.END)
        update_task_list()

# Function to remove tasks
def remove_task():
    selected_task = task_listbox.get(tk.ACTIVE)
    if selected_task:
        manager.remove_task(selected_task)
        update_task_list()

# Function to update task list in GUI
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in manager.get_tasks():
        task_listbox.insert(tk.END, task)

# Exit program with confirmation
def exit_program():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

# Input field for tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add and Remove buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=10)

# Load tasks into the Listbox when the program starts
update_task_list()
