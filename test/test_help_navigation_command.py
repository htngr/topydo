import unittest
from .command_testcase import CommandTest
from topydo.commands.HelpNavigationCommand import HelpNavigationCommand
import os


class HelpNavigationCommandTest(CommandTest):
    def test_help_navigation_command(self):
        command = HelpNavigationCommand([], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, 'Navigation\n'
                                      '        \n'
                                      '  KEY         ACTION        DESCRIPTION                                        \n'
                                      '    \n'
                                      '  j or ↓      down          Move one item down                                 \n'
                                      '  k or ↑      up            Move one item up                                   \n'
                                      '  l or →      next_column   Move to next column                                \n'
                                      '  h or ←      prev_column   Move to previous column                            \n'
                                      '  gg or Home  home          Move to top                                        \n'
                                      '  G or End    end           Move to bottom                                     \n'
                                      '  0           first_column  Move to first column                               \n'
                                      '  $           last_column   Move to last column                                \n'
                                      '  :                         Focus the commandline to execute custom commands.  \n'
                                      '\n')
        self.assertFalse(self.errors)

        os.system('topydo help nav > help_nav_cmd_output.txt')
        help_nav_cmd_output = open('help_nav_cmd_output.txt').readlines()

        self.assertListEqual(['Navigation\n',
                              '        \n',
                              '  KEY         ACTION        DESCRIPTION                                        \n',
                              '    \n',
                              '  j or ↓      down          Move one item down                                 \n',
                              '  k or ↑      up            Move one item up                                   \n',
                              '  l or →      next_column   Move to next column                                \n',
                              '  h or ←      prev_column   Move to previous column                            \n',
                              '  gg or Home  home          Move to top                                        \n',
                              '  G or End    end           Move to bottom                                     \n',
                              '  0           first_column  Move to first column                               \n',
                              '  $           last_column   Move to last column                                \n',
                              '  :                         Focus the commandline to execute custom commands.  \n',
                              '\n'], help_nav_cmd_output)

        os.system('topydo helpnav > help_nav_cmd_output.txt')
        help_nav_cmd_output = open('help_nav_cmd_output.txt').readlines()

        self.assertListEqual(['Navigation\n',
                              '        \n',
                              '  KEY         ACTION        DESCRIPTION                                        \n',
                              '    \n',
                              '  j or ↓      down          Move one item down                                 \n',
                              '  k or ↑      up            Move one item up                                   \n',
                              '  l or →      next_column   Move to next column                                \n',
                              '  h or ←      prev_column   Move to previous column                            \n',
                              '  gg or Home  home          Move to top                                        \n',
                              '  G or End    end           Move to bottom                                     \n',
                              '  0           first_column  Move to first column                               \n',
                              '  $           last_column   Move to last column                                \n',
                              '  :                         Focus the commandline to execute custom commands.  \n',
                              '\n'], help_nav_cmd_output)

        os.remove('help_nav_cmd_output.txt')

    def test_helpnavigation_name(self):
        name = HelpNavigationCommand.name()

        self.assertEqual(name, 'helpnavigation')

    def test_help(self):
        command = HelpNavigationCommand(['help'], None, self.out, self.error)
        command.execute()

        self.assertEqual(self.output, '')
        self.assertEqual(self.errors, command.usage() + '\n\n' + command.help() + '\n')


if __name__ == '__main__':
    unittest.main()
