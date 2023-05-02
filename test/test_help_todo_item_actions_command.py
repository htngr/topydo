import unittest
from .command_testcase import CommandTest
from topydo.commands.HelpTodoItemActionsCommand import HelpTodoItemActionsCommand
import os


class HelpTodoItemActionsCommandTest(CommandTest):
    def test_help_todo_item_actions_command1(self):
        command = HelpTodoItemActionsCommand([], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Todo item actions\n'
                                      '        \n'
                                      '  KEY           ACTION       DESCRIPTION                                        \n'
                                      '    \n'
                                      "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n"
                                      "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n"
                                      '  m             mark         Mark current item (for performing actions on mult  \n'
                                      '                             iple items simultaneously)                         \n'
                                      "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n"
                                      '                             th the given period                                \n'
                                      "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n"
                                      '                             e given priority                                   \n'
                                      "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n"
                                      '                             hted item(s) with the given period                 \n'
                                      "  u             cmd revert   Executes 'revert'                                  \n"
                                      "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n"
                                      '  .             repeat       Repeats the last command on the current item. Whe  \n'
                                      '                             n the last command was entered on the commandline  \n'
                                      '                             ,                                                  \n'
                                      "                             that command should have the '{}' placeholder to   \n"
                                      '                             insert the current item.                           \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_todo_item_actions_command2(self):
        command = HelpTodoItemActionsCommand([''], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Todo item actions\n'
                                      '        \n'
                                      '  KEY           ACTION       DESCRIPTION                                        \n'
                                      '    \n'
                                      "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n"
                                      "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n"
                                      '  m             mark         Mark current item (for performing actions on mult  \n'
                                      '                             iple items simultaneously)                         \n'
                                      "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n"
                                      '                             th the given period                                \n'
                                      "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n"
                                      '                             e given priority                                   \n'
                                      "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n"
                                      '                             hted item(s) with the given period                 \n'
                                      "  u             cmd revert   Executes 'revert'                                  \n"
                                      "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n"
                                      '  .             repeat       Repeats the last command on the current item. Whe  \n'
                                      '                             n the last command was entered on the commandline  \n'
                                      '                             ,                                                  \n'
                                      "                             that command should have the '{}' placeholder to   \n"
                                      '                             insert the current item.                           \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_todo_item_actions_command3(self):
        command = HelpTodoItemActionsCommand([None], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Todo item actions\n'
                                      '        \n'
                                      '  KEY           ACTION       DESCRIPTION                                        \n'
                                      '    \n'
                                      "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n"
                                      "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n"
                                      '  m             mark         Mark current item (for performing actions on mult  \n'
                                      '                             iple items simultaneously)                         \n'
                                      "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n"
                                      '                             th the given period                                \n'
                                      "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n"
                                      '                             e given priority                                   \n'
                                      "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n"
                                      '                             hted item(s) with the given period                 \n'
                                      "  u             cmd revert   Executes 'revert'                                  \n"
                                      "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n"
                                      '  .             repeat       Repeats the last command on the current item. Whe  \n'
                                      '                             n the last command was entered on the commandline  \n'
                                      '                             ,                                                  \n'
                                      "                             that command should have the '{}' placeholder to   \n"
                                      '                             insert the current item.                           \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_todo_item_actions_command4(self):
        command = HelpTodoItemActionsCommand(None, None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Todo item actions\n'
                                      '        \n'
                                      '  KEY           ACTION       DESCRIPTION                                        \n'
                                      '    \n'
                                      "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n"
                                      "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n"
                                      '  m             mark         Mark current item (for performing actions on mult  \n'
                                      '                             iple items simultaneously)                         \n'
                                      "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n"
                                      '                             th the given period                                \n'
                                      "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n"
                                      '                             e given priority                                   \n'
                                      "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n"
                                      '                             hted item(s) with the given period                 \n'
                                      "  u             cmd revert   Executes 'revert'                                  \n"
                                      "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n"
                                      '  .             repeat       Repeats the last command on the current item. Whe  \n'
                                      '                             n the last command was entered on the commandline  \n'
                                      '                             ,                                                  \n'
                                      "                             that command should have the '{}' placeholder to   \n"
                                      '                             insert the current item.                           \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_todo_item_actions_command5(self):
        command = HelpTodoItemActionsCommand(['foo'], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Todo item actions\n'
                                      '        \n'
                                      '  KEY           ACTION       DESCRIPTION                                        \n'
                                      '    \n'
                                      "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n"
                                      "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n"
                                      '  m             mark         Mark current item (for performing actions on mult  \n'
                                      '                             iple items simultaneously)                         \n'
                                      "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n"
                                      '                             th the given period                                \n'
                                      "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n"
                                      '                             e given priority                                   \n'
                                      "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n"
                                      '                             hted item(s) with the given period                 \n'
                                      "  u             cmd revert   Executes 'revert'                                  \n"
                                      "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n"
                                      '  .             repeat       Repeats the last command on the current item. Whe  \n'
                                      '                             n the last command was entered on the commandline  \n'
                                      '                             ,                                                  \n'
                                      "                             that command should have the '{}' placeholder to   \n"
                                      '                             insert the current item.                           \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_todo_item_actions_command6(self):
        command = HelpTodoItemActionsCommand(['foo', 'bar'], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Todo item actions\n'
                                      '        \n'
                                      '  KEY           ACTION       DESCRIPTION                                        \n'
                                      '    \n'
                                      "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n"
                                      "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n"
                                      '  m             mark         Mark current item (for performing actions on mult  \n'
                                      '                             iple items simultaneously)                         \n'
                                      "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n"
                                      '                             th the given period                                \n'
                                      "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n"
                                      '                             e given priority                                   \n'
                                      "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n"
                                      '                             hted item(s) with the given period                 \n'
                                      "  u             cmd revert   Executes 'revert'                                  \n"
                                      "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n"
                                      '  .             repeat       Repeats the last command on the current item. Whe  \n'
                                      '                             n the last command was entered on the commandline  \n'
                                      '                             ,                                                  \n'
                                      "                             that command should have the '{}' placeholder to   \n"
                                      '                             insert the current item.                           \n'
                                      '\n')
        self.assertFalse(self.errors)

    def test_help_todo_item_actions_command7(self):
        os.system('topydo help item > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo helpitem > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo help item foo > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo helpitem foo > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo help item foo bar > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo helpitem foo bar > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.remove('help_item_cmd_output.txt')

    def test_help_todo_item_actions_command8(self):
        os.system('topydo item help > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo itemhelp > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo item help foo > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo itemhelp foo > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo item help foo bar > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.system('topydo itemhelp foo bar > help_item_cmd_output.txt')
        help_item_cmd_output = open('help_item_cmd_output.txt').readlines()

        self.assertListEqual(['Todo item actions\n',
                              '        \n',
                              '  KEY           ACTION       DESCRIPTION                                        \n',
                              '    \n',
                              "  d             cmd del {}   Executes 'del' on highlighted item(s)              \n",
                              "  e             cmd edit {}  Executes 'edit' on highlighted item(s)             \n",
                              '  m             mark         Mark current item (for performing actions on mult  \n',
                              '                             iple items simultaneously)                         \n',
                              "  pp<period>    postpone     Executes 'postpone' on the highlighted item(s) wi  \n",
                              '                             th the given period                                \n',
                              "  pr<priority>  pri          Executes 'pri' on the highlighted item(s) with th  \n",
                              '                             e given priority                                   \n',
                              "  ps<period>    postpone_s   Executes 'postpone' in strict mode on the highlig  \n",
                              '                             hted item(s) with the given period                 \n',
                              "  u             cmd revert   Executes 'revert'                                  \n",
                              "  x             cmd do {}    Executes 'do' on highlighted item(s)               \n",
                              '  .             repeat       Repeats the last command on the current item. Whe  \n',
                              '                             n the last command was entered on the commandline  \n',
                              '                             ,                                                  \n',
                              "                             that command should have the '{}' placeholder to   \n",
                              '                             insert the current item.                           \n',
                              '\n'], help_item_cmd_output)

        os.remove('help_item_cmd_output.txt')

    def test_helptodoitemactions_name(self):
        name = HelpTodoItemActionsCommand.name()

        self.assertEqual(name, 'helptodoitemactions')

    def test_help(self):
        command = HelpTodoItemActionsCommand(['help'], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, '')
        self.assertEqual(self.errors, command.usage() + '\n\n' + command.help() + '\n')


if __name__ == '__main__':
    unittest.main()
