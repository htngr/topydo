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

    def test_donow1(self):
        command = DoNowCommand(['1'], self.todolist, self.out, self.error, None, True, 1)
        command.execute()

        self.assertEqual(self.todolist.todo(1).source(), 'Foo min:1')
        self.assertEqual(self.output, 'WORKING ON: Foo\n'
                                      '\nMINUTE(S) PASSED: 1\n'
                                      'UPDATED TODO: |1| Foo min:1\n')
        self.assertFalse(self.errors)
        self.assertTrue(self.todolist.dirty)

    def test_donow2(self):
        command = DoNowCommand(['2'], self.todolist, self.out, self.error, None, True, 2)
        command.execute()

        self.assertEqual(self.todolist.todo(2).source(), 'Bar min:32')
        self.assertEqual(self.output, 'WORKING ON: Bar min:30\n'
                                      '\nMINUTE(S) PASSED: 2\n'
                                      'UPDATED TODO: |2| Bar min:32\n')
        self.assertFalse(self.errors)
        self.assertTrue(self.todolist.dirty)

    def test_donow3(self):
        command = DoNowCommand(['3'], self.todolist, self.out, self.error, None, True, 0)
        command.execute()

        self.assertEqual(self.todolist.todo(3).source(), 'Baz min:0')
        self.assertEqual(self.output, 'WORKING ON: Baz\n'
                                      '\nMINUTE(S) PASSED: 0\n'
                                      'UPDATED TODO: |3| Baz min:0\n')
        self.assertFalse(self.errors)
        self.assertTrue(self.todolist.dirty)

    def test_donow4(self):
        command = DoNowCommand(['4'], self.todolist, self.out, self.error, None, True, 0)
        command.execute()

        self.assertEqual(self.todolist.todo(4).source(), 'Qux min:30')
        self.assertEqual(self.output, 'WORKING ON: Qux min:30\n'
                                      '\nMINUTE(S) PASSED: 0\n'
                                      'UPDATED TODO: |4| Qux min:30\n')
        self.assertFalse(self.errors)
        self.assertFalse(self.todolist.dirty)

    def test_donow_multi_args1(self):
        command = DoNowCommand(['3', '4'], self.todolist, self.out, self.error, None, True, 1)
        command.execute()

        self.assertEqual(self.todolist.todo(3).source(), 'Baz min:1')
        self.assertEqual(self.output, 'WORKING ON: Baz\n'
                                      '\nMINUTE(S) PASSED: 1\n'
                                      'UPDATED TODO: |3| Baz min:1\n')
        self.assertFalse(self.errors)
        self.assertTrue(self.todolist.dirty)

    def test_donow_multi_args2(self):
        command = DoNowCommand(['4', '3'], self.todolist, self.out, self.error, None, True, 1)
        command.execute()

        self.assertEqual(self.todolist.todo(4).source(), 'Qux min:31')
        self.assertEqual(self.output, 'WORKING ON: Qux min:30\n'
                                      '\nMINUTE(S) PASSED: 1\n'
                                      'UPDATED TODO: |4| Qux min:31\n')
        self.assertFalse(self.errors)
        self.assertTrue(self.todolist.dirty)

    def test_invalid_arg(self):
        command = DoNowCommand([], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.output)
        self.assertEqual(self.errors, command.usage() + '\n')
        self.assertFalse(self.todolist.dirty)

    def test_invalid_todo1(self):
        command = DoNowCommand(['5'], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.output)
        self.assertEqual(self.errors, 'Invalid todo number.\n')
        self.assertFalse(self.todolist.dirty)

    def test_invalid_todo2(self):
        command = DoNowCommand(['01'], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.output)
        self.assertEqual(self.errors, 'Invalid todo number.\n')
        self.assertFalse(self.todolist.dirty)

    def test_invalid_todo3(self):
        command = DoNowCommand(['AAA'], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.output)
        self.assertEqual(self.errors, 'Invalid todo number.\n')
        self.assertFalse(self.todolist.dirty)

    def test_invalid_todo4(self):
        command = DoNowCommand([''], self.todolist, self.out, self.error)
        command.execute()

        self.assertFalse(self.output)
        self.assertEqual(self.errors, 'Invalid todo number.\n')
        self.assertFalse(self.todolist.dirty)

    def test_none1(self):
        command = DoNowCommand([None], self.todolist, self.out, self.error)

        with self.assertRaises(TypeError):
            command.execute()

        self.assertFalse(self.output)
        self.assertFalse(self.errors)
        self.assertFalse(self.todolist.dirty)

    def test_none2(self):
        command = DoNowCommand(None, self.todolist, self.out, self.error)

        with self.assertRaises(TypeError) as error:
            command.execute()

        self.assertEquals(str(error.exception), "'NoneType' object is not subscriptable")
        self.assertFalse(self.output)
        self.assertFalse(self.errors)
        self.assertFalse(self.todolist.dirty)

    def test_donow_name(self):
        name = DoNowCommand.name()

        self.assertEqual(name, 'donow')

    def test_help(self):
        command = DoNowCommand(['help'], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, '')
        self.assertEqual(self.errors, command.usage() + '\n\n' + command.help() + '\n')


if __name__ == '__main__':
    unittest.main()
