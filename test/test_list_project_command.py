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

from topydo.commands.ListProjectCommand import ListProjectCommand

from .command_testcase import CommandTest
from .facilities import load_file_to_todolist






class ListProjectCommandTest(CommandTest):
    def test_projects1(self):
        todolist = load_file_to_todolist("test/data/TodoListTest.txt")
        command = ListProjectCommand([""], todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()  # test default implementation of post_archive

        self.assertEqual(self.output, "Project1\nProject2\n")
        self.assertFalse(self.errors)

    def test_projects2(self):
        todolist = load_file_to_todolist("test/data/TodoListTest.txt")
        command = ListProjectCommand(["aaa"], todolist, self.out, self.error)
        command.execute()
        command.execute_post_archive_actions()

        self.assertEqual(self.output, "Project1\nProject2\n")
        self.assertFalse(self.errors)

    def test_listproject_name(self):
        name = ListProjectCommand.name()

        self.assertEqual(name, 'listproject')

    def test_help(self):
        command = ListProjectCommand(["help"], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, "")
        self.assertEqual(self.errors,
                         command.usage() + "\n\n" + command.help() + "\n")


    def test_sort_ignore_case(self):
        input_list = ['applications', 'Books', 'cake']
        expected_output = ['applications', 'Books', 'cake']
        actual_output = sorted(input_list, key=lambda s: s.lower())
        assert actual_output == expected_output


    def test__lists_projects_alphabetically(self):
        todolist = load_file_to_todolist("test/data/TodoListTest.txt")
        todolist.add_project('Project A')
        todolist.add_project('project b')
        todolist.add_project('Project C')

        output = []

        command = ListProjectCommand([], todolist, p_out=output.append)
        command.execute()

        assert len(output) == 3
        assert output[0] == 'Project A'
        assert output[1] == 'project b'
        assert output[2] == 'Project C'


if __name__ == '__main__':
    unittest.main()
