from topydo.lib.Command import Command
from columnar import columnar


class HelpNavigationCommand(Command):
    def __init__(self, p_args, p_todolist, #pragma: no branch
                 p_out=lambda a: None,
                 p_err=lambda a: None,
                 p_prompt=lambda a: None):
        super().__init__(p_args, p_todolist, p_out, p_err, p_prompt)

    def execute(self):
        if not super().execute():
            return False

        headers = ['Key', 'Action', 'Description']
        rows = [
            ['j or ↓', 'down', 'Move one item down'],
            ['k or ↑', 'up', 'Move one item up'],
            ['l or →', 'next_column', 'Move to next column'],
            ['h or ←', 'prev_column', 'Move to previous column'],
            ['gg or Home', 'home', 'Move to top'],
            ['G or End', 'end', 'Move to bottom'],
            ['0', 'first_column', 'Move to first column'],
            ['$', 'last_column', 'Move to last column'],
            [':', '', 'Focus the commandline to execute custom commands.']
        ]
        help_text = columnar(rows, headers, no_borders=True)
        self.out(f'Navigation\n{help_text}')

    def usage(self):
        return """\
Synopsis: help nav
          helpnav\
"""

    def help(self):
        return """Lists default keyboard shortcuts for navigation in the Column UI."""
