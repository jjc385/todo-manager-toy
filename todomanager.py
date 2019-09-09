import uuid

class Task:
    """A task for the todo manager

    Currently contains only its `content`, a string, 
    which is the name/description of the task
    """

    def __init__(self, content):
        if not isinstance(content, str):
            raise ValueError(
                    "Expected parameter `content`"
                    "to be an instance of str, not {}"
                    .format(type(content))
                )
        self.content = content

class TodoManager:
    """A simple object to keep track of tasks

    Tracks tasks along with their assigned IDs.
    """

    def __init__(self):
        self.tasks = {}

    def addTask(self, task):
        """Add a task to the manager

        Parameters:
        task -- The Task instance to be added

        Returns:
        The ID of the task added -- a UUID string
        """
        if not isinstance(task, Task):
            raise ValueError(
                    "Expected parameter `task`"
                    "to be an instance of Task, not {}"
                    .format(type(task))
                )
        ID = str(uuid.uuid4())
        self.tasks[ID] = task
        return ID



