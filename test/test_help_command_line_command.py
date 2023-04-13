import unittest
from .command_testcase import CommandTest
from topydo.commands.HelpCommandLineCommand import HelpCommandLineCommand
import os


class HelpCommandLineCommandTest(CommandTest):
    def test_help_command_line_command(self):
        command = HelpCommandLineCommand([], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Commandline shortcuts\n'
                                      '\n'
                                      "The commandline, activated when pressing ':', supports the following keys:\n"
                                      '      \n'
                                      '  KEY     DESCRIPTION                              \n'
                                      '    \n'
                                      '  Ctrl-a  Move to the beginning                    \n'
                                      '  Ctrl-e  Move to the end                          \n'
                                      '  Ctrl-u  Delete from the cursor to the beginning  \n'
                                      '  Ctrl-k  Delete from the cursor up to the end     \n'
                                      '\n')
        self.assertFalse(self.errors)

        os.system('topydo help cl > help_cl_cmd_output.txt')
        help_cl_cmd_output = str(open('help_cl_cmd_output.txt').readlines())

        self.assertIn('Commandline shortcuts', help_cl_cmd_output)
        self.assertIn("The commandline, activated when pressing ':', supports the following keys:", help_cl_cmd_output)
        self.assertIn('KEY     DESCRIPTION', help_cl_cmd_output)
        self.assertIn('Ctrl-a  Move to the beginning', help_cl_cmd_output)
        self.assertIn('Ctrl-e  Move to the end', help_cl_cmd_output)
        self.assertIn('Ctrl-u  Delete from the cursor to the beginning', help_cl_cmd_output)
        self.assertIn('Ctrl-k  Delete from the cursor up to the end', help_cl_cmd_output)

        os.system('topydo helpcl > help_cl_cmd_output.txt')
        help_cl_cmd_output = str(open('help_cl_cmd_output.txt').readlines())

        self.assertIn('Commandline shortcuts', help_cl_cmd_output)
        self.assertIn("The commandline, activated when pressing ':', supports the following keys:", help_cl_cmd_output)
        self.assertIn('KEY     DESCRIPTION', help_cl_cmd_output)
        self.assertIn('Ctrl-a  Move to the beginning', help_cl_cmd_output)
        self.assertIn('Ctrl-e  Move to the end', help_cl_cmd_output)
        self.assertIn('Ctrl-u  Delete from the cursor to the beginning', help_cl_cmd_output)
        self.assertIn('Ctrl-k  Delete from the cursor up to the end', help_cl_cmd_output)

        os.remove('help_cl_cmd_output.txt')

    def test_helpcommandline_name(self):
        name = HelpCommandLineCommand.name()

        self.assertEqual(name, 'helpcommandline')

    def test_help(self):
        command = HelpCommandLineCommand(['help'], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, '')
        self.assertEqual(self.errors, command.usage() + '\n\n' + command.help() + '\n')


if __name__ == '__main__':
    unittest.main()
