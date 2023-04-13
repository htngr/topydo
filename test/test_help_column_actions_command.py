import unittest
from .command_testcase import CommandTest
from topydo.commands.HelpColumnActionsCommand import HelpColumnActionsCommand
import os


class HelpColumnActionsCommandTest(CommandTest):
    def test_help_column_actions_command(self):
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

        os.system('topydo help col > help_col_cmd_output.txt')
        help_col_cmd_output = str(open('help_col_cmd_output.txt').readlines())

        self.assertIn('Column actions', help_col_cmd_output)
        self.assertIn('KEY     ACTION         DESCRIPTION', help_col_cmd_output)
        self.assertIn('A       append_column  Add/append column (at the right)', help_col_cmd_output)
        self.assertIn('I       insert_column  Insert new column before the current column', help_col_cmd_output)
        self.assertIn('E       edit_column    Edit the current column definition', help_col_cmd_output)
        self.assertIn('D       delete_column  Delete the current column', help_col_cmd_output)
        self.assertIn('Y       copy_column    Copy (yank) the current column', help_col_cmd_output)
        self.assertIn('L       swap_left      Swap current column with left neighbouring column', help_col_cmd_output)
        self.assertIn('R       swap_right     Swap current column with right neighbouring column', help_col_cmd_output)
        self.assertIn('Ctrl-a  mark_all       Marks all items in the current column', help_col_cmd_output)

        os.system('topydo helpcol > help_col_cmd_output.txt')
        help_col_cmd_output = str(open('help_col_cmd_output.txt').readlines())

        self.assertIn('Column actions', help_col_cmd_output)
        self.assertIn('KEY     ACTION         DESCRIPTION', help_col_cmd_output)
        self.assertIn('A       append_column  Add/append column (at the right)', help_col_cmd_output)
        self.assertIn('I       insert_column  Insert new column before the current column', help_col_cmd_output)
        self.assertIn('E       edit_column    Edit the current column definition', help_col_cmd_output)
        self.assertIn('D       delete_column  Delete the current column', help_col_cmd_output)
        self.assertIn('Y       copy_column    Copy (yank) the current column', help_col_cmd_output)
        self.assertIn('L       swap_left      Swap current column with left neighbouring column', help_col_cmd_output)
        self.assertIn('R       swap_right     Swap current column with right neighbouring column', help_col_cmd_output)
        self.assertIn('Ctrl-a  mark_all       Marks all items in the current column', help_col_cmd_output)

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
