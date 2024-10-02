class TaskManager:
    def __init__(self, category="default"):
        self.category = category
        self.filename = f"tasks_{self.category}.txt"
        self.tasks = []

    def load_tasks(self):
        """Load tasks and deadlines from the file."""
        try:
            with open(self.filename, "r") as file:
                self.tasks = [tuple(line.strip().split(" | ")) for line in file.readlines()]  # Store tasks as (task, deadline)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """Save tasks and deadlines to the file."""
        with open(self.filename, "w") as file:
            for task, deadline in self.tasks:
                file.write(f"{task} | {deadline}\n")

    def add_task(self, task, deadline="No deadline"):
        """Add a task with an optional deadline."""
        self.tasks.append((task, deadline))
        self.save_tasks()

    def remove_task(self, task):
        """Remove a task and save."""
        self.tasks = [t for t in self.tasks if t[0] != task]
        self.save_tasks()
