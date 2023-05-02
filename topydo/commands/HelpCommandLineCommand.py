from topydo.lib.Command import Command
from columnar import columnar


class HelpCommandLineCommand(Command):
    def __init__(self, p_args, p_todolist, #pragma: no branch
                 p_out=lambda a: None,
                 p_err=lambda a: None,
                 p_prompt=lambda a: None):
        super().__init__(p_args, p_todolist, p_out, p_err, p_prompt)

    def execute(self):
        if not super().execute():
            return False

        headers = ['Key', 'Description']
        shortcuts = [
            ['Ctrl-a', 'Move to the beginning'],
            ['Ctrl-e', 'Move to the end'],
            ['Ctrl-u', 'Delete from the cursor to the beginning'],
            ['Ctrl-k', 'Delete from the cursor up to the end']
        ]
        command_line_table = columnar(shortcuts, headers, no_borders=True)
        self.out(f"Commandline shortcuts\n\n"
                 f"The commandline, activated when pressing ':', supports the following keys:\n"
                 f"{command_line_table}")

    def usage(self):
        return """\
Synopsis: help cl
          helpcl
          cl help
          clhelp\
"""

    def help(self):
        return """Lists default keyboard shortcuts for the command line in the Column UI."""
