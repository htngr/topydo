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

from topydo.Commands import get_subcommand
from topydo.commands.AddCommand import AddCommand
from topydo.commands.DeleteCommand import DeleteCommand
from topydo.commands.HelpColumnActionsCommand import HelpColumnActionsCommand
from topydo.commands.HelpCommandLineCommand import HelpCommandLineCommand
from topydo.commands.HelpNavigationCommand import HelpNavigationCommand
from topydo.commands.HelpTodoItemActionsCommand import HelpTodoItemActionsCommand
from topydo.commands.ListCommand import ListCommand
from topydo.commands.TagCommand import TagCommand
from topydo.commands.DoNowCommand import DoNowCommand
from topydo.lib.Config import ConfigError, config

from .topydo_testcase import TopydoTest


class GetSubcommandTest(TopydoTest):
    def test_normal_cmd(self):
        args = ["add"]
        real_cmd, _ = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, AddCommand))

    def test_donow_cmd(self):
        args = ['donow', '1']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, DoNowCommand))
        self.assertEqual(final_args, ['1'])

    def test_cmd_help(self):
        args = ["help", "add"]
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, AddCommand))
        self.assertEqual(final_args, ["help"])

    def test_cmd_help_col(self):
        args = ['help', 'col']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpColumnActionsCommand))
        self.assertEqual(final_args, [])

        args = ['helpcol']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpColumnActionsCommand))
        self.assertEqual(final_args, [])

        args = ['col', 'help']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpColumnActionsCommand))
        self.assertEqual(final_args, [])

        args = ['colhelp']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpColumnActionsCommand))
        self.assertEqual(final_args, [])

        args = ['col']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['col'])

        args = ['help', 'col', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpColumnActionsCommand))
        self.assertEqual(final_args, [])

        args = ['helpcol', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpColumnActionsCommand))
        self.assertEqual(final_args, ['foo'])

        args = ['col', 'help', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpColumnActionsCommand))
        self.assertEqual(final_args, [])

        args = ['colhelp', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpColumnActionsCommand))
        self.assertEqual(final_args, [])

        args = ['foo', 'help', 'col']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'help', 'col'])

        args = ['foo', 'helpcol']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'helpcol'])

        args = ['foo', 'col', 'help']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'col', 'help'])

        args = ['foo', 'colhelp']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'colhelp'])

    def test_cmd_help_cl(self):
        args = ['help', 'cl']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpCommandLineCommand))
        self.assertEqual(final_args, [])

        args = ['helpcl']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpCommandLineCommand))
        self.assertEqual(final_args, [])

        args = ['cl', 'help']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpCommandLineCommand))
        self.assertEqual(final_args, [])

        args = ['clhelp']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpCommandLineCommand))
        self.assertEqual(final_args, [])

        args = ['cl']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['cl'])

        args = ['help', 'cl', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpCommandLineCommand))
        self.assertEqual(final_args, [])

        args = ['helpcl', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpCommandLineCommand))
        self.assertEqual(final_args, ['foo'])

        args = ['cl', 'help', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpCommandLineCommand))
        self.assertEqual(final_args, [])

        args = ['clhelp', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpCommandLineCommand))
        self.assertEqual(final_args, [])

        args = ['foo', 'help', 'cl']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'help', 'cl'])

        args = ['foo', 'helpcl']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'helpcl'])

        args = ['foo', 'cl', 'help']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'cl', 'help'])

        args = ['foo', 'clhelp']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'clhelp'])

    def test_cmd_help_nav(self):
        args = ['help', 'nav']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpNavigationCommand))
        self.assertEqual(final_args, [])

        args = ['helpnav']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpNavigationCommand))
        self.assertEqual(final_args, [])

        args = ['nav', 'help']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpNavigationCommand))
        self.assertEqual(final_args, [])

        args = ['navhelp']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpNavigationCommand))
        self.assertEqual(final_args, [])

        args = ['nav']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['nav'])

        args = ['help', 'nav', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpNavigationCommand))
        self.assertEqual(final_args, [])

        args = ['helpnav', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpNavigationCommand))
        self.assertEqual(final_args, ['foo'])

        args = ['nav', 'help', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpNavigationCommand))
        self.assertEqual(final_args, [])

        args = ['navhelp', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpNavigationCommand))
        self.assertEqual(final_args, [])

        args = ['foo', 'help', 'nav']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'help', 'nav'])

        args = ['foo', 'helpnav']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'helpnav'])

        args = ['foo', 'nav', 'help']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'nav', 'help'])

        args = ['foo', 'navhelp']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'navhelp'])

    def test_cmd_help_item(self):
        args = ['help', 'item']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpTodoItemActionsCommand))
        self.assertEqual(final_args, [])

        args = ['helpitem']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpTodoItemActionsCommand))
        self.assertEqual(final_args, [])

        args = ['item', 'help']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpTodoItemActionsCommand))
        self.assertEqual(final_args, [])

        args = ['itemhelp']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpTodoItemActionsCommand))
        self.assertEqual(final_args, [])

        args = ['item']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['item'])

        args = ['help', 'item', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpTodoItemActionsCommand))
        self.assertEqual(final_args, [])

        args = ['helpitem', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpTodoItemActionsCommand))
        self.assertEqual(final_args, ['foo'])

        args = ['item', 'help', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpTodoItemActionsCommand))
        self.assertEqual(final_args, [])

        args = ['itemhelp', 'foo']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, HelpTodoItemActionsCommand))
        self.assertEqual(final_args, [])

        args = ['foo', 'help', 'item']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'help', 'item'])

        args = ['foo', 'helpitem']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'helpitem'])

        args = ['foo', 'item', 'help']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'item', 'help'])

        args = ['foo', 'itemhelp']
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ['foo', 'itemhelp'])

    def test_alias01(self):
        config("test/data/aliases.conf")

        args = ["foo"]
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, DeleteCommand))
        self.assertEqual(final_args, ["-f", "test"])

    def test_alias02(self):
        config("test/data/aliases.conf")

        args = ["format"]
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ["-F", "|I| x c d {(}p{)} s k", "-n", "25"])

    def test_alias03(self):
        config("test/data/aliases.conf")

        args = ["smile"]
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, [u"\u263b"])

    def test_alias04(self):
        config("test/data/aliases.conf")

        args = ["star", "foo"]
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, TagCommand))
        self.assertEqual(final_args, ["foo", "star", "1"])

    def test_default_cmd01(self):
        args = ["bar"]
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, ["bar"])

    def test_default_cmd02(self):
        args = []
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, ListCommand))
        self.assertEqual(final_args, [])

    def test_alias_default_cmd01(self):
        config("test/data/aliases.conf", {('topydo', 'default_command'): 'foo'})

        args = ["bar"]
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, DeleteCommand))
        self.assertEqual(final_args, ["-f", "test", "bar"])

    def test_alias_default_cmd02(self):
        config("test/data/aliases.conf", {('topydo', 'default_command'): 'foo'})

        args = []
        real_cmd, final_args = get_subcommand(args)
        self.assertTrue(issubclass(real_cmd, DeleteCommand))
        self.assertEqual(final_args, ["-f", "test"])

    def test_alias_default_cmd03(self):
        config("test/data/aliases.conf", {('topydo', 'default_command'): 'nonexisting_default'})

        args = ['nonexisting']
        real_cmd, final_args = get_subcommand(args)
        self.assertFalse(real_cmd)
        self.assertEqual(final_args, ['nonexisting'])

    def test_alias_default_cmd04(self):
        config("test/data/aliases.conf", {('topydo', 'default_command'): 'nonexisting_default'})

        args = []
        real_cmd, final_args = get_subcommand(args)
        self.assertFalse(real_cmd)
        self.assertEqual(final_args, [])

    def test_wrong_alias(self):
        config("test/data/aliases.conf")

        args = ["baz"]
        real_cmd, _ = get_subcommand(args)
        self.assertEqual(real_cmd, None)

    def test_alias_quotation(self):
        config("test/data/aliases.conf")

        args = ["quot"]
        with self.assertRaises(ConfigError) as ce:
            get_subcommand(args)

        self.assertEqual(str(ce.exception), 'No closing quotation')

    def test_help(self):
        real_cmd, final_args = get_subcommand(['help', 'nonexisting'])
        self.assertFalse(real_cmd)
        self.assertEqual(final_args, ['help', 'nonexisting'])

if __name__ == '__main__':
    unittest.main()
