from unittest import TestCase
from todomanager import TodoManager, Task

class SimpleTodoTest(TestCase):

    def setUp(self):
        self.manager = TodoManager()

    def test_setup(self):
        self.assertEqual( len(self.manager.tasks), 0 )

    def test_addTask(self):
        task1 = Task("Sample task 1")
        task2 = Task("Sample task 2")

        id1 = self.manager.addTask(task1)
        self.assertEqual( len(self.manager.tasks), 1 )
        self.assertTrue( id1 in self.manager.tasks )

        id2 = self.manager.addTask(task2)
        self.assertEqual( len(self.manager.tasks), 2 )
        self.assertTrue( id2 in self.manager.tasks )
