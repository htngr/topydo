import unittest
from .command_testcase import CommandTest
from topydo.commands.HelpColumnActionsCommand import HelpColumnActionsCommand
import os


class HelpColumnActionsCommandTest(CommandTest):
    def test_help_column_actions_command1(self):
        command = HelpColumnActionsCommand([], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Column actions\n'
                                      '        \n'
                                      '  KEY     ACTION         DESCRIPTION                                         \n'
                                      '    \n'
                                      '  A       append_column  Add/append column (at the right)                    \n'
                                      '  I       insert_column  Insert new column before the current column         \n'
                                      '  E       edit_column    Edit the current column definition                  \n'
                                      '  D       delete_column  Delete the current column                           \n'
                                      '  Y       copy_column    Copy (yank) the current column                      \n'
                                      '  L       swap_left      Swap current column with left neighbouring column   \n'
                                      '  R       swap_right     Swap current column with right neighbouring column  \n'
                                      '  Ctrl-a  mark_all       Marks all items in the current column               \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_column_actions_command2(self):
        command = HelpColumnActionsCommand([''], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Column actions\n'
                                      '        \n'
                                      '  KEY     ACTION         DESCRIPTION                                         \n'
                                      '    \n'
                                      '  A       append_column  Add/append column (at the right)                    \n'
                                      '  I       insert_column  Insert new column before the current column         \n'
                                      '  E       edit_column    Edit the current column definition                  \n'
                                      '  D       delete_column  Delete the current column                           \n'
                                      '  Y       copy_column    Copy (yank) the current column                      \n'
                                      '  L       swap_left      Swap current column with left neighbouring column   \n'
                                      '  R       swap_right     Swap current column with right neighbouring column  \n'
                                      '  Ctrl-a  mark_all       Marks all items in the current column               \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_column_actions_command3(self):
        command = HelpColumnActionsCommand([None], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Column actions\n'
                                      '        \n'
                                      '  KEY     ACTION         DESCRIPTION                                         \n'
                                      '    \n'
                                      '  A       append_column  Add/append column (at the right)                    \n'
                                      '  I       insert_column  Insert new column before the current column         \n'
                                      '  E       edit_column    Edit the current column definition                  \n'
                                      '  D       delete_column  Delete the current column                           \n'
                                      '  Y       copy_column    Copy (yank) the current column                      \n'
                                      '  L       swap_left      Swap current column with left neighbouring column   \n'
                                      '  R       swap_right     Swap current column with right neighbouring column  \n'
                                      '  Ctrl-a  mark_all       Marks all items in the current column               \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_column_actions_command4(self):
        command = HelpColumnActionsCommand(['foo'], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Column actions\n'
                                      '        \n'
                                      '  KEY     ACTION         DESCRIPTION                                         \n'
                                      '    \n'
                                      '  A       append_column  Add/append column (at the right)                    \n'
                                      '  I       insert_column  Insert new column before the current column         \n'
                                      '  E       edit_column    Edit the current column definition                  \n'
                                      '  D       delete_column  Delete the current column                           \n'
                                      '  Y       copy_column    Copy (yank) the current column                      \n'
                                      '  L       swap_left      Swap current column with left neighbouring column   \n'
                                      '  R       swap_right     Swap current column with right neighbouring column  \n'
                                      '  Ctrl-a  mark_all       Marks all items in the current column               \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_column_actions_command5(self):
        command = HelpColumnActionsCommand(['foo', 'bar'], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Column actions\n'
                                      '        \n'
                                      '  KEY     ACTION         DESCRIPTION                                         \n'
                                      '    \n'
                                      '  A       append_column  Add/append column (at the right)                    \n'
                                      '  I       insert_column  Insert new column before the current column         \n'
                                      '  E       edit_column    Edit the current column definition                  \n'
                                      '  D       delete_column  Delete the current column                           \n'
                                      '  Y       copy_column    Copy (yank) the current column                      \n'
                                      '  L       swap_left      Swap current column with left neighbouring column   \n'
                                      '  R       swap_right     Swap current column with right neighbouring column  \n'
                                      '  Ctrl-a  mark_all       Marks all items in the current column               \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_column_actions_command6(self):
        os.system('topydo help col > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo helpcol > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo help col foo > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo helpcol foo > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo help col foo bar > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo helpcol foo bar > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.remove('help_col_cmd_output.txt')

    def test_help_column_actions_command7(self):
        os.system('topydo col help > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo colhelp > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo col help foo > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo colhelp foo > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo col help foo bar > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.system('topydo colhelp foo bar > help_col_cmd_output.txt')
        help_col_cmd_output = open('help_col_cmd_output.txt').readlines()

        self.assertListEqual(['Column actions\n',
                              '        \n',
                              '  KEY     ACTION         DESCRIPTION                                         \n',
                              '    \n',
                              '  A       append_column  Add/append column (at the right)                    \n',
                              '  I       insert_column  Insert new column before the current column         \n',
                              '  E       edit_column    Edit the current column definition                  \n',
                              '  D       delete_column  Delete the current column                           \n',
                              '  Y       copy_column    Copy (yank) the current column                      \n',
                              '  L       swap_left      Swap current column with left neighbouring column   \n',
                              '  R       swap_right     Swap current column with right neighbouring column  \n',
                              '  Ctrl-a  mark_all       Marks all items in the current column               \n',
                              '\n'], help_col_cmd_output)

        os.remove('help_col_cmd_output.txt')

    def test_helpcolumnactions_name(self):
        name = HelpColumnActionsCommand.name()

        self.assertEqual(name, 'helpcolumnactions')

    def test_help(self):
        command = HelpColumnActionsCommand(['help'], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, '')
        self.assertEqual(self.errors, command.usage() + '\n\n' + command.help() + '\n')


if __name__ == '__main__':
    unittest.main()
