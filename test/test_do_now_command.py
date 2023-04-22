import unittest
from .command_testcase import CommandTest
from topydo.commands.DoNowCommand import DoNowCommand
from topydo.lib.TodoList import TodoList


class DoNowCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        todos = [
            'Foo',
            'Bar min:30'
        ]

        self.todolist = TodoList(todos)

    def test_do_now_command1(self):
        command = DoNowCommand(['1'], self.todolist, self.out, self.error, None, True, 1)
        command.execute()

        self.assertEqual(self.todolist.todo(1).source(), 'Foo min:1')
        self.assertEqual(self.output, 'DOING: Foo\n'
                                      '\n1 MINUTE(S) PASSED\n'
                                      'UPDATED TODO: |1| Foo min:1\n')
        self.assertFalse(self.errors)
        self.assertTrue(self.todolist.dirty)

    def test_do_now_command2(self):
        command = DoNowCommand(['2'], self.todolist, self.out, self.error, None, True, 2)
        command.execute()

        self.assertEqual(self.todolist.todo(2).source(), 'Bar min:32')
        self.assertEqual(self.output, 'DOING: Bar min:30\n'
                                      '\n2 MINUTE(S) PASSED\n'
                                      'UPDATED TODO: |2| Bar min:32\n')
        self.assertFalse(self.errors)
        self.assertTrue(self.todolist.dirty)


if __name__ == '__main__':
    unittest.main()
