# Topydo - A todo.txt client written in Python.
# Copyright (C) 2014 - 2015 Bram Schoenmakers <bram@topydo.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
from datetime import date, timedelta

from topydo.commands.DoCommand import DoCommand
from topydo.lib.Config import config
from topydo.lib.TodoList import TodoList

from .command_testcase import CommandTest


def _yes_prompt(self):
    return "y"


def _no_prompt(self):
    return "n"


class DoCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        todos = [
            "Foo id:1",
            "Bar p:1",
            "Baz p:1",
            "Recurring! rec:1d",
            "x 2014-10-18 Already complete",
            "Inactive t:2030-12-31 id:2",
            "Subtodo of inactive p:2",
            "Strict due:2014-01-01 rec:1d",
            "Invalid rec:1",
            "a @test with due:2015-06-03",
            "a @test with +project",
        ]

        todos_with_priorities = [
            '(A) Start a band',
            '(B) Foo id:1',
            '(B) Bar p:1',
            '(B) Baz p:1',
            'Go to the gym due:2023-04-21',
            'x 2014-10-18 (C) Already complete',
            '(D) a @test with due:2015-06-03',
            '(E) a @test with +project',
            '(F) Recurring! rec:1d'
        ]

        self.todolist = TodoList(todos)
        self.todolist_with_priorities = TodoList(todos_with_priorities)
        self.today = date.today()
        self.tomorrow = self.today + timedelta(1)
        self.yesterday = self.today - timedelta(1)

        self.yesterday = self.yesterday.isoformat()
        self.today = self.today.isoformat()
        self.tomorrow = self.tomorrow.isoformat()

    def test_do1(self):
        command = DoCommand(["3"], self.todolist, self.out, self.error,
                            _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertTrue(self.todolist.todo(3).is_completed())
        self.assertEqual(self.output,
                         "Completed: x {} Baz p:1\n".format(self.today))
        self.assertEqual(self.errors, "")

    def test_do_subtasks1(self):
        command = DoCommand(["1"], self.todolist, self.out, self.error,
                            _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        result = "|  2| Bar p:1\n|  3| Baz p:1\nCompleted: x {today} Bar p:1\nCompleted: x {today} Baz p:1\nCompleted: x {today} Foo id:1\n".format(
            today=self.today)

        for number in [1, 2, 3]:
            self.assertTrue(self.todolist.todo(number).is_completed())

        self.assertTrue(self.todolist.dirty)
        self.assertFalse(self.todolist.todo(4).is_completed())
        self.assertEqual(self.output, result)
        self.assertEqual(self.errors, "")

    def test_do_subtasks2(self):
        command = DoCommand(["1"], self.todolist, self.out, self.error,
                            _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        result = "|  2| Bar p:1\n|  3| Baz p:1\nCompleted: x {} Foo id:1\n".format(self.today)

        self.assertTrue(self.todolist.dirty)
        self.assertTrue(self.todolist.todo(1).is_completed())
        self.assertFalse(self.todolist.todo(2).is_completed())
        self.assertFalse(self.todolist.todo(3).is_completed())
        self.assertEqual(self.output, result)
        self.assertEqual(self.errors, "")

    def test_do_subtasks_force1(self):
        def prompt(p_prompt):
            prompt.prompt_shown = True

        prompt.prompt_shown = False

        command = DoCommand(["-f", "1"], self.todolist, self.out, self.error,
                            prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(prompt.prompt_shown)
        self.assertEqual(self.errors, "")
        self.assertFalse(self.todolist.todo(2).is_completed())

    def test_do_subtasks_force2(self):
        def prompt(p_prompt):
            prompt.prompt_shown = True

        prompt.prompt_shown = False

        command = DoCommand(["--force", "1"], self.todolist, self.out,
                            self.error, prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(prompt.prompt_shown)
        self.assertEqual(self.errors, "")
        self.assertFalse(self.todolist.todo(2).is_completed())

    def _recurrence_helper(self, p_flags):
        command = DoCommand(p_flags, self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.errors, "")
        self.assertEqual(self.todolist.count(), 12)

    def test_recurrence(self):
        self.assertFalse(self.todolist.todo(4).has_tag('due'))

        self._recurrence_helper(["4"])

        self.assertTrue(self.todolist.todo(4).is_completed())
        result = """Completed: x {today} Recurring! rec:1d
The following todo item(s) became active:
| 12| {today} Recurring! rec:1d due:{tomorrow}\n""".format(today=self.today, tomorrow=self.tomorrow)
        self.assertEqual(self.output, result)

        todo = self.todolist.todo(10)
        self.assertFalse(todo.is_completed())
        self.assertTrue(todo.has_tag('due'))

    def test_strict_recurrence1(self):
        self._recurrence_helper(["-s", "8"])
        result = """Completed: x {today} Strict due:2014-01-01 rec:1d
The following todo item(s) became active:
| 12| {today} Strict due:2014-01-02 rec:1d\n""".format(today=self.today)
        self.assertEqual(self.output, result)

    def test_strict_recurrence2(self):
        self._recurrence_helper(["--strict", "8"])

        result = """Completed: x {today} Strict due:2014-01-01 rec:1d
The following todo item(s) became active:
| 12| {today} Strict due:2014-01-02 rec:1d\n""".format(today=self.today)
        self.assertEqual(self.output, result)

    def test_recurrence_no_creation_date(self):
        config("test/data/docommand.conf")

        self._recurrence_helper(["4"])

        result = """Completed: x {today} Recurring! rec:1d
The following todo item(s) became active:
| 12| Recurring! rec:1d due:{tomorrow}\n""".format(today=self.today, tomorrow=self.tomorrow)
        self.assertEqual(self.output, result)

    def test_invalid1(self):
        command = DoCommand(["99"], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist.dirty)
        self.assertFalse(self.output)
        self.assertEqual(self.errors, "Invalid todo number given.\n")

    def test_invalid2(self):
        command = DoCommand(["AAA"], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist.dirty)
        self.assertFalse(self.output)
        self.assertEqual(self.errors, "Invalid todo number given.\n")

    def test_invalid3(self):
        command = DoCommand(["01"], self.todolist, self.out, self.error,
                            _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist.dirty)
        self.assertFalse(self.output)
        self.assertEqual(self.errors, "Invalid todo number given.\n")

    def test_activated_todos1(self):
        command = DoCommand(["2"], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        first_output = "Completed: x {} Bar p:1\n".format(self.today)

        self.assertEqual(self.output, first_output)
        self.assertEqual(self.errors, "")

        command = DoCommand(["3"], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertEqual(self.output,
                         first_output + "Completed: x {} Baz p:1\nThe following todo item(s) became active:\n|  1| Foo id:1\n".format(
                             self.today))
        self.assertEqual(self.errors, "")

    def test_activated_todos2(self):
        command = DoCommand(["7"], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertEqual(self.output, "Completed: x {} Subtodo of inactive p:2\n".format(self.today))
        self.assertEqual(self.errors, "")

    def test_already_complete(self):
        command = DoCommand(["5"], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist.dirty)
        self.assertEqual(self.todolist.todo(5).completion_date(),
                         date(2014, 10, 18))
        self.assertFalse(self.output)
        self.assertEqual(self.errors, "Todo has already been completed.\n")

    def test_do_regex1(self):
        command = DoCommand(["baz"], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertTrue(self.todolist.todo(3).is_completed())
        self.assertEqual(self.output,
                         "Completed: x {} Baz p:1\n".format(self.today))
        self.assertEqual(self.errors, "")

    def test_do_custom_date1(self):
        command = DoCommand(["-d", "2014-11-18", "3"], self.todolist, self.out,
                            self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output, "Completed: x 2014-11-18 Baz p:1\n")
        self.assertEqual(self.errors, "")

    def test_do_custom_date2(self):
        command = DoCommand(["-d", "2014-11-18", "1"], self.todolist, self.out,
                            self.error, _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output,
                         "|  2| Bar p:1\n|  3| Baz p:1\nCompleted: x 2014-11-18 Bar p:1\nCompleted: x 2014-11-18 Baz p:1\nCompleted: x 2014-11-18 Foo id:1\n")
        self.assertEqual(self.errors, "")

    def test_do_custom_date3(self):
        command = DoCommand(["--date=2014-11-18", "3"], self.todolist,
                            self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output, "Completed: x 2014-11-18 Baz p:1\n")
        self.assertEqual(self.errors, "")

    def test_do_custom_date4(self):
        command = DoCommand(["-d", "foo", "3"], self.todolist, self.out,
                            self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output,
                         "Completed: x {} Baz p:1\n".format(self.today))
        self.assertEqual(self.errors, "")

    def test_do_custom_date5(self):
        """
        Make sure that the new recurrence date is correct when a custom
        date is given.
        """
        command = DoCommand(["-d", self.yesterday, "4"], self.todolist,
                            self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output, """Completed: x {yesterday} Recurring! rec:1d
The following todo item(s) became active:
| 12| {today} Recurring! rec:1d due:{today}\n""".format(today=self.today, yesterday=self.yesterday))
        self.assertEqual(self.errors, "")

    def test_do_custom_date6(self):
        """
        When a custom date is set, strict recurrence must still hold on to the
        due date as the offset. This todo item however, has no due date, then
        the completion date must be used as an offset.
        """
        command = DoCommand(["-s", "-d", self.yesterday, "4"], self.todolist,
                            self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output, """Completed: x {yesterday} Recurring! rec:1d
The following todo item(s) became active:
| 12| {today} Recurring! rec:1d due:{today}\n""".format(today=self.today, yesterday=self.yesterday))
        self.assertEqual(self.errors, "")

    def test_do_custom_date7(self):
        """
        When a custom date is set, strict recurrence must still hold on to the
        due date as the offset.
        """
        command = DoCommand(["-s", "-d", self.yesterday, "8"], self.todolist,
                            self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output, """Completed: x {yesterday} Strict due:2014-01-01 rec:1d
The following todo item(s) became active:
| 12| {today} Strict due:2014-01-02 rec:1d\n""".format(today=self.today, yesterday=self.yesterday))
        self.assertEqual(self.errors, "")

    def test_do_custom_date8(self):
        """
        Convert relative completion dates to an absolute date (yesterday).
        """
        command = DoCommand(["-d", "yesterday", "3"], self.todolist, self.out,
                            self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output, "Completed: x {} Baz p:1\n".format(self.yesterday))
        self.assertEqual(self.errors, "")

    def test_do_custom_date9(self):
        """
        Convert relative completion dates to an absolute date (-1d)
        """
        command = DoCommand(["-d", "-1d", "3"], self.todolist, self.out,
                            self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output,
                         "Completed: x {} Baz p:1\n".format(self.yesterday))
        self.assertEqual(self.errors, "")

    def test_multi_do1(self):
        command = DoCommand(["1", "3"], self.todolist, self.out, self.error,
                            _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.todo(1).is_completed())
        self.assertTrue(self.todolist.todo(2).is_completed())
        self.assertTrue(self.todolist.todo(3).is_completed())

        self.assertEqual(self.output,
                         "|  2| Bar p:1\n|  3| Baz p:1\nCompleted: x {today} Bar p:1\nCompleted: x {today} Baz p:1\nCompleted: x {today} Foo id:1\n".format(
                             today=self.today))

    def test_multi_do2(self):
        command = DoCommand(["1", "3"], self.todolist, self.out, self.error,
                            _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.todo(1).is_completed())
        self.assertFalse(self.todolist.todo(2).is_completed())
        self.assertTrue(self.todolist.todo(3).is_completed())

        self.assertEqual(self.output,
                         "|  2| Bar p:1\n|  3| Baz p:1\nCompleted: x {today} Foo id:1\nCompleted: x {today} Baz p:1\n".format(
                             today=self.today))

    def test_multi_do3(self):
        command = DoCommand(["3", "3"], self.todolist, self.out, self.error,
                            _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.todo(3).is_completed())
        self.assertEqual(self.output,
                         "Completed: x {} Baz p:1\n".format(self.today))

    def test_multi_do4(self):
        command = DoCommand(["99", "3"], self.todolist, self.out, self.error,
                            _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist.todo(3).is_completed())
        self.assertEqual(self.errors, "Invalid todo number given: 99.\n")

    def test_multi_do5(self):
        """
        Check output when all supplied todo numbers are invalid.
        """
        command = DoCommand(["99", "15"], self.todolist, self.out, self.error,
                            _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertEqual(self.errors, "Invalid todo number given: 99.\nInvalid todo number given: 15.\n")

    def test_multi_do6(self):
        """
        Throw an error with invalid argument containing special characters.
        """
        command = DoCommand([u"Fo\u00d3B\u0105r", "Bar"], self.todolist,
                            self.out, self.error, None)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist.dirty)
        self.assertEqual(self.errors,
                         u"Invalid todo number given: Fo\u00d3B\u0105r.\n")

    def test_expr_do1(self):
        command = DoCommand(["-e", "@test"], self.todolist, self.out,
                            self.error, None)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output,
                         "Completed: x {t} a @test with due:2015-06-03\nCompleted: x {t} a @test with +project\n".format(
                             t=self.today))
        self.assertEqual(self.errors, "")

    def test_expr_do2(self):
        command = DoCommand(["-e", "@test", "due:2015-06-03"], self.todolist,
                            self.out, self.error, None)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output, "Completed: x {} a @test with due:2015-06-03\n".format(self.today))
        self.assertEqual(self.errors, "")

    def test_expr_do3(self):
        command = DoCommand(["-e", "@test", "due:2015-06-03", "+project"],
                            self.todolist, self.out, self.error, None)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist.dirty)

    def test_expr_do4(self):
        """ Don't do anything with unrelevant todo items. """
        command = DoCommand(["-e", "Foo"], self.todolist, self.out, self.error,
                            None)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist.dirty)

    def test_expr_do5(self):
        """ Force marking unrelevant items as done with additional -x flag. """
        command = DoCommand(["-xe", "Foo"], self.todolist, self.out,
                            self.error, _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        result = "|  2| Bar p:1\n|  3| Baz p:1\nCompleted: x {t} Bar p:1\nCompleted: x {t} Baz p:1\nCompleted: x {t} Foo id:1\n".format(
            t=self.today)

        self.assertTrue(self.todolist.dirty)
        self.assertEqual(self.output, result)
        self.assertEqual(self.errors, "")

    def test_invalid_recurrence(self):
        """
        Show error message when an item has an invalid recurrence pattern.
        """
        command = DoCommand(["9"], self.todolist, self.out, self.error,
                            _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertEqual(self.output,
                         "Completed: x {} Invalid rec:1\n".format(self.today))
        self.assertEqual(self.errors, "Warning: todo item has an invalid recurrence pattern.\n")

    def test_empty(self):
        command = DoCommand([], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist.dirty)
        self.assertFalse(self.output)
        self.assertEqual(self.errors, command.usage() + "\n")

    def test_keep_priority_do1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['1'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(1).is_completed())
        self.assertEqual(self.output, f'Completed: x (A) {self.today} Start a band\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['1'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(1).is_completed())
        self.assertEqual(self.output, f'Completed: x {self.today} Start a band\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_subtasks1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['2'], self.todolist_with_priorities, self.out, self.error, _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        for number in [2, 3, 4]:
            self.assertTrue(self.todolist_with_priorities.todo(number).is_completed())

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertFalse(self.todolist_with_priorities.todo(5).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x (B) {self.today} Bar p:1\n'
                                      f'Completed: x (B) {self.today} Baz p:1\n'
                                      f'Completed: x (B) {self.today} Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_subtasks2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['2'], self.todolist_with_priorities, self.out, self.error, _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        for number in [2, 3, 4]:
            self.assertTrue(self.todolist_with_priorities.todo(number).is_completed())

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertFalse(self.todolist_with_priorities.todo(5).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x {self.today} Bar p:1\n'
                                      f'Completed: x {self.today} Baz p:1\n'
                                      f'Completed: x {self.today} Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_subtasks3(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['2'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(3).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x (B) {self.today} Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_subtasks4(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['2'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(3).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x {self.today} Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_no_priority1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['5'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(5).is_completed())
        self.assertEqual(self.output, f'Completed: x {self.today} Go to the gym due:2023-04-21\n')
        self.assertFalse(self.errors)

    def test_keep_priority_no_priority2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['5'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(5).is_completed())
        self.assertEqual(self.output, f'Completed: x {self.today} Go to the gym due:2023-04-21\n')
        self.assertFalse(self.errors)

    def test_keep_priority_activated_todos1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['3'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertEqual(self.output, f'Completed: x (B) {self.today} Bar p:1\n')
        self.assertFalse(self.errors)

        command = DoCommand(['4'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertFalse(self.todolist_with_priorities.todo(2).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(3).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'Completed: x (B) {self.today} Bar p:1\n'
                                      f'Completed: x (B) {self.today} Baz p:1\n'
                                      f'The following todo item(s) became active:\n'
                                      f'|  2| (B) Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_activated_todos2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['3'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertEqual(self.output, f'Completed: x {self.today} Bar p:1\n')
        self.assertFalse(self.errors)

        command = DoCommand(['4'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertFalse(self.todolist_with_priorities.todo(2).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(3).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'Completed: x {self.today} Bar p:1\n'
                                      f'Completed: x {self.today} Baz p:1\n'
                                      f'The following todo item(s) became active:\n'
                                      f'|  2| (B) Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_multi_do1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['2', '4'], self.todolist_with_priorities, self.out, self.error, _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(3).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x (B) {self.today} Bar p:1\n'
                                      f'Completed: x (B) {self.today} Baz p:1\n'
                                      f'Completed: x (B) {self.today} Foo id:1\n')

    def test_keep_priority_multi_do2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['2', '4'], self.todolist_with_priorities, self.out, self.error, _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(3).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x {self.today} Bar p:1\n'
                                      f'Completed: x {self.today} Baz p:1\n'
                                      f'Completed: x {self.today} Foo id:1\n')

    def test_keep_priority_multi_do3(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['2', '4'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(3).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x (B) {self.today} Foo id:1\n'
                                      f'Completed: x (B) {self.today} Baz p:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_multi_do4(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['2', '4'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(3).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x {self.today} Foo id:1\n'
                                      f'Completed: x {self.today} Baz p:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_multi_do5(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['4', '4'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'Completed: x (B) {self.today} Baz p:1\n')

    def test_keep_priority_multi_do6(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['4', '4'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'Completed: x {self.today} Baz p:1\n')

    def test_keep_priority_do_regex1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['bar'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(3).is_completed())
        self.assertEqual(self.output, f'Completed: x (B) {self.today} Bar p:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_regex2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['bar'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(3).is_completed())
        self.assertEqual(self.output, f'Completed: x {self.today} Bar p:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_subtasks_force1(self):
        def prompt(p_prompt):
            prompt.prompt_shown = True

        prompt.prompt_shown = False

        config('test/data/keeppriority1.conf')

        command = DoCommand(['--force', '2'], self.todolist_with_priorities, self.out, self.error, prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(prompt.prompt_shown)
        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(3).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x (B) {self.today} Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_subtasks_force2(self):
        def prompt(p_prompt):
            prompt.prompt_shown = True

        prompt.prompt_shown = False

        config('test/data/keeppriority0.conf')

        command = DoCommand(['--force', '2'], self.todolist_with_priorities, self.out, self.error, prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(prompt.prompt_shown)
        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(3).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.output, f'|  3| (B) Bar p:1\n'
                                      f'|  4| (B) Baz p:1\n'
                                      f'Completed: x {self.today} Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_custom_date1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['-d', '2014-11-18', '4'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.todolist_with_priorities.todo(4).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.output, 'Completed: x (B) 2014-11-18 Baz p:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_custom_date2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['-d', '2014-11-18', '4'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.todolist_with_priorities.todo(4).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.output, 'Completed: x 2014-11-18 Baz p:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_custom_date3(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['-d', '2014-11-18', '2'], self.todolist_with_priorities, self.out, self.error, _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(3).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.todolist_with_priorities.todo(2).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.todolist_with_priorities.todo(3).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.todolist_with_priorities.todo(4).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.output, '|  3| (B) Bar p:1\n'
                                      '|  4| (B) Baz p:1\n'
                                      'Completed: x (B) 2014-11-18 Bar p:1\n'
                                      'Completed: x (B) 2014-11-18 Baz p:1\n'
                                      'Completed: x (B) 2014-11-18 Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_custom_date4(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['-d', '2014-11-18', '2'], self.todolist_with_priorities, self.out, self.error, _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(3).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.todolist_with_priorities.todo(2).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.todolist_with_priorities.todo(3).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.todolist_with_priorities.todo(4).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.output, '|  3| (B) Bar p:1\n'
                                      '|  4| (B) Baz p:1\n'
                                      'Completed: x 2014-11-18 Bar p:1\n'
                                      'Completed: x 2014-11-18 Baz p:1\n'
                                      'Completed: x 2014-11-18 Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_custom_date5(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['-d', '2014-11-18', '2'], self.todolist_with_priorities, self.out, self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(3).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.todolist_with_priorities.todo(2).completion_date(), date(2014, 11, 18))
        self.assertFalse(self.todolist_with_priorities.todo(3).completion_date(), date(2014, 11, 18))
        self.assertFalse(self.todolist_with_priorities.todo(4).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.output, '|  3| (B) Bar p:1\n'
                                      '|  4| (B) Baz p:1\n'
                                      'Completed: x (B) 2014-11-18 Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_do_custom_date6(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['-d', '2014-11-18', '2'], self.todolist_with_priorities, self.out,
                            self.error, _no_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(2).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(3).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(4).is_completed())
        self.assertEqual(self.todolist_with_priorities.todo(2).completion_date(), date(2014, 11, 18))
        self.assertFalse(self.todolist_with_priorities.todo(3).completion_date(), date(2014, 11, 18))
        self.assertFalse(self.todolist_with_priorities.todo(4).completion_date(), date(2014, 11, 18))
        self.assertEqual(self.output, '|  3| (B) Bar p:1\n'
                                      '|  4| (B) Baz p:1\n'
                                      'Completed: x 2014-11-18 Foo id:1\n')
        self.assertFalse(self.errors)

    def test_keep_priority_expr_do1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['-e', '@test'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(7).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(8).is_completed())
        self.assertEqual(self.output, f'Completed: x (D) {self.today} a @test with due:2015-06-03\n'
                                      f'Completed: x (E) {self.today} a @test with +project\n')
        self.assertFalse(self.errors)

    def test_keep_priority_expr_do2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['-e', '@test'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(7).is_completed())
        self.assertTrue(self.todolist_with_priorities.todo(8).is_completed())
        self.assertEqual(self.output, f'Completed: x {self.today} a @test with due:2015-06-03\n'
                                      f'Completed: x {self.today} a @test with +project\n')
        self.assertFalse(self.errors)

    def test_keep_priority_test_recurrence1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['9'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(9).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(10).is_completed())
        self.assertEqual(self.output, f'Completed: x (F) {self.today} Recurring! rec:1d\n'
                                      f'The following todo item(s) became active:\n'
                                      f'| 10| (F) {self.today} Recurring! rec:1d due:{self.tomorrow}\n')
        self.assertFalse(self.errors)
        self.assertEqual(self.todolist_with_priorities.count(), 10)

    def test_keep_priority_test_recurrence2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['9'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertTrue(self.todolist_with_priorities.dirty)
        self.assertTrue(self.todolist_with_priorities.todo(9).is_completed())
        self.assertFalse(self.todolist_with_priorities.todo(10).is_completed())
        self.assertEqual(self.output, f'Completed: x {self.today} Recurring! rec:1d\n'
                                      f'The following todo item(s) became active:\n'
                                      f'| 10| (F) {self.today} Recurring! rec:1d due:{self.tomorrow}\n')
        self.assertFalse(self.errors)
        self.assertEqual(self.todolist_with_priorities.count(), 10)

    def test_keep_priority_already_complete1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['6'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist_with_priorities.dirty)
        self.assertEqual(self.todolist_with_priorities.todo(6).completion_date(), date(2014, 10, 18))
        self.assertFalse(self.output)
        self.assertEqual(self.errors, 'Todo has already been completed.\n')

    def test_keep_priority_already_complete2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['6'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist_with_priorities.dirty)
        self.assertEqual(self.todolist_with_priorities.todo(6).completion_date(), date(2014, 10, 18))
        self.assertFalse(self.output)
        self.assertEqual(self.errors, 'Todo has already been completed.\n')

    def test_keep_priority_invalid1(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['99'], self.todolist_with_priorities, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist_with_priorities.dirty)
        self.assertFalse(self.output)
        self.assertEqual(self.errors, 'Invalid todo number given.\n')

    def test_keep_priority_invalid2(self):
        config('test/data/keeppriority0.conf')

        command = DoCommand(['AAA'], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist_with_priorities.dirty)
        self.assertFalse(self.output)
        self.assertEqual(self.errors, 'Invalid todo number given.\n')

    def test_keep_priority_invalid3(self):
        config('test/data/keeppriority1.conf')

        command = DoCommand(['01'], self.todolist_with_priorities, self.out, self.error, _yes_prompt)
        command.execute()
        command.execute_post_archive_actions()

        self.assertFalse(self.todolist_with_priorities.dirty)
        self.assertFalse(self.output)
        self.assertEqual(self.errors, 'Invalid todo number given.\n')

    def test_do_name(self):
        name = DoCommand.name()

        self.assertEqual(name, 'do')

    def test_help(self):
        command = DoCommand(["help"], self.todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertEqual(self.output, "")
        self.assertEqual(self.errors,
                         command.usage() + "\n\n" + command.help() + "\n")





if __name__ == '__main__':
    unittest.main()
