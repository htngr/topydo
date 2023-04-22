import unittest
from .command_testcase import CommandTest
from topydo.commands.HelpCommandLineCommand import HelpCommandLineCommand
import os


class HelpCommandLineCommandTest(CommandTest):
    def test_help_command_line_command1(self):
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

    def test_help_command_line_command2(self):
        command = HelpCommandLineCommand([''], None, self.out, self.error)
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

    def test_help_command_line_command3(self):
        command = HelpCommandLineCommand([None], None, self.out, self.error)
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

    def test_help_command_line_command4(self):
        command = HelpCommandLineCommand(None, None, self.out, self.error)
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

    def test_help_command_line_command5(self):
        command = HelpCommandLineCommand(['foo'], None, self.out, self.error)
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

    def test_help_command_line_command6(self):
        command = HelpCommandLineCommand(['foo', 'bar'], None, self.out, self.error)
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

    def test_help_command_line_command7(self):
        os.system('topydo help cl > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo helpcl > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo help cl foo > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo helpcl foo > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo help cl foo bar > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo helpcl foo bar > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.remove('help_cl_cmd_output.txt')

    def test_help_command_line_command8(self):
        os.system('topydo cl help > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo clhelp > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo cl help foo > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo clhelp foo > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo cl help foo bar > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

        os.system('topydo clhelp foo bar > help_cl_cmd_output.txt')
        help_cl_cmd_output = open('help_cl_cmd_output.txt').readlines()

        self.assertListEqual(['Commandline shortcuts\n',
                              '\n',
                              "The commandline, activated when pressing ':', supports the following keys:\n",
                              '      \n',
                              '  KEY     DESCRIPTION                              \n',
                              '    \n',
                              '  Ctrl-a  Move to the beginning                    \n',
                              '  Ctrl-e  Move to the end                          \n',
                              '  Ctrl-u  Delete from the cursor to the beginning  \n',
                              '  Ctrl-k  Delete from the cursor up to the end     \n',
                              '\n'], help_cl_cmd_output)

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
