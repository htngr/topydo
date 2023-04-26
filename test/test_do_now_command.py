import unittest
from .command_testcase import CommandTest
from topydo.commands.DoNowCommand import DoNowCommand
from topydo.lib.TodoList import TodoList


class DoNowCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        todos = [
            'Foo',
            'Bar min:30',
            'Baz',
            'Qux min:30'
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

    def test_do_now_command3(self):
        command = DoNowCommand(['3'], self.todolist, self.out, self.error, None, True, 0)
        command.execute()

        self.assertEqual(self.todolist.todo(3).source(), 'Baz min:0')
        self.assertEqual(self.output, 'DOING: Baz\n'
                                      '\n0 MINUTE(S) PASSED\n'
                                      'UPDATED TODO: |3| Baz min:0\n')
        self.assertFalse(self.errors)
        self.assertTrue(self.todolist.dirty)

    def test_do_now_command4(self):
        command = DoNowCommand(['4'], self.todolist, self.out, self.error, None, True, 0)
        command.execute()

        self.assertEqual(self.todolist.todo(4).source(), 'Qux min:30')
        self.assertEqual(self.output, 'DOING: Qux min:30\n'
                                      '\n0 MINUTE(S) PASSED\n'
                                      'UPDATED TODO: |4| Qux min:30\n')
        self.assertFalse(self.errors)
        self.assertFalse(self.todolist.dirty)

    def test_do_now_command5(self):
        command = DoNowCommand([], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.output)
        self.assertEqual(self.errors, command.usage() + '\n')
        self.assertFalse(self.todolist.dirty)

    def test_do_now_command6(self):
        command = DoNowCommand(['5'], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.output)
        self.assertEqual(self.errors, "Invalid todo number.\n")
        self.assertFalse(self.todolist.dirty)

    def test_do_now_command7(self):
        command = DoNowCommand([''], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.output)
        self.assertEqual(self.errors, "Invalid todo number.\n")
        self.assertFalse(self.todolist.dirty)

    def test_do_now_command8(self):
        command = DoNowCommand([None], self.todolist, self.out, self.error)

        with self.assertRaises(TypeError) as error:
            command.execute()

        self.assertEquals(str(error.exception),
                          "int() argument must be a string, a bytes-like object or a real number, not 'NoneType'")
        self.assertFalse(self.output)
        self.assertFalse(self.errors)
        self.assertFalse(self.todolist.dirty)


if __name__ == '__main__':
    unittest.main()
