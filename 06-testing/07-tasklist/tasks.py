from datetime import date

class Task:
    def __init__(self, description, due_date):
        if not isinstance(due_date, date):
            raise TypeError("due_date must be a date instance")
        self._description = description
        self._due_date = due_date
        self.finished = False

    @property
    def description(self):
        return self._description

    @property
    def due_date(self):
        return self._due_date


class TaskList:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("Only Task instances can be added")
        if task.due_date < date.today():
            raise RuntimeError("Cannot add a task with a due date in the past")
        self._tasks.append(task)

    def __len__(self):
        return len(self._tasks)

    @property
    def finished_tasks(self):
        return [task for task in self._tasks if task.finished]

    @property
    def due_tasks(self):
        return [task for task in self._tasks if not task.finished]

    @property
    def overdue_tasks(self):
        today = date.today()
        return [task for task in self._tasks if not task.finished and task.due_date < today]
