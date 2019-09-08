import uuid

class Task:

    def __init__(self, content):
        self.content = content

class TodoManager:

    def __init__(self):
        self.tasks = {}

    def addTask(self, task):
        if not isinstance(task, Task):
            raise ValueError(
                    "Expected instance of Task, not {}, of type {}"
                    .format(task, type(task))
                )
        #return  # intentional mistake, so some tests fail
        ID = str(uuid.uuid4())
        self.tasks[ID] = task
        return ID



