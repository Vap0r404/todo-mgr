class TaskManager:
    def __init__(self, category="default"):
        self.category = category
        self.filename = f"tasks_{self.category}.txt"
        self.tasks = []

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                for line in file.readlines():
                    parts = line.strip().split(" | ")
                    if len(parts) == 2:  # Ensure there are exactly two parts
                        self.tasks.append(tuple(parts))
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task, deadline in self.tasks:
                file.write(f"{task} | {deadline}\n")

    def add_task(self, task, deadline="No deadline"):
        self.tasks.append((task, deadline))
        self.save_tasks()

    def remove_task(self, task):
        self.tasks = [t for t in self.tasks if t[0] != task]
        self.save_tasks()

    def sort_tasks_by_name(self):
        self.tasks.sort(key=lambda x: x[0])

    def sort_tasks_by_deadline(self):
        self.tasks.sort(key=lambda x: x[1] if x[1] != "No deadline" else "")

    def sort_tasks_by_priority(self):
        priority_order = {"Low": 1, "Medium": 2, "High": 3}
        self.tasks.sort(key=lambda x: priority_order[x[2]])
