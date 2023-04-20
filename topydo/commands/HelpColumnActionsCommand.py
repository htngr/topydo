from topydo.lib.Command import Command
from columnar import columnar


class HelpColumnActionsCommand(Command):
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
            ['A', 'append_column', 'Add/append column (at the right)'],
            ['I', 'insert_column', 'Insert new column before the current column'],
            ['E', 'edit_column', 'Edit the current column definition'],
            ['D', 'delete_column', 'Delete the current column'],
            ['Y', 'copy_column', 'Copy (yank) the current column'],
            ['L', 'swap_left', 'Swap current column with left neighbouring column'],
            ['R', 'swap_right', 'Swap current column with right neighbouring column'],
            ['Ctrl-a', 'mark_all', 'Marks all items in the current column']
        ]
        help_text = columnar(rows, headers, no_borders=True)
        self.out(f'Column actions\n{help_text}')

    def usage(self):
        return """\
Synopsis: help col
          helpcol
          col help
          colhelp\
"""

    def help(self):
        return """Lists default keyboard shortcuts for column actions in the Column UI."""
