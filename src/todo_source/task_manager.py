class TaskManager:
    def __init__(self, file_path="tasks.txt"):
        self.tasks = []
        self.file_path = file_path
        self.load_tasks()  # Load tasks from file when initializing

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()  # Save tasks after adding

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()  # Save tasks after removing

    def get_tasks(self):
        return self.tasks

    # Save tasks to a file
    def save_tasks(self):
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    # Load tasks from a file
    def load_tasks(self):
        try:
            with open(self.file_path, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty list
            self.tasks = []
