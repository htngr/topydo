from topydo.lib.Command import Command
from columnar import columnar


class HelpTodoItemActionsCommand(Command):
    def __init__(self, p_args, p_todolist, #pragma: no branch
                 p_out=lambda a: None,
                 p_err=lambda a: None,
                 p_prompt=lambda a: None):
        super().__init__(p_args, p_todolist, p_out, p_err, p_prompt)

    def execute(self):
        if not super().execute():
            return False

        headers = ['Key', 'Action', 'Description']
        shortcuts = [
            ['d', 'cmd del {}', "Executes 'del' on highlighted item(s)"],
            ['e', 'cmd edit {}', "Executes 'edit' on highlighted item(s)"],
            ['m', 'mark', 'Mark current item (for performing actions on multiple items simultaneously)'],
            ['pp<period>', 'postpone', "Executes 'postpone' on the highlighted item(s) with the given period"],
            ['pr<priority>', 'pri', "Executes 'pri' on the highlighted item(s) with the given priority"],
            ['ps<period>', 'postpone_s', "Executes 'postpone' in strict mode on the highlighted item(s) with the given period"],
            ['u', 'cmd revert', "Executes 'revert'"],
            ['x', 'cmd do {}', "Executes 'do' on highlighted item(s)"],
            ['.', 'repeat', "Repeats the last command on the current item. When the last command was entered on the commandline,\n"
                            "that command should have the '{}' placeholder to insert the current item."]
        ]
        todo_item_actions_table = columnar(shortcuts, headers, no_borders=True)
        self.out(f'Todo item actions\n'
                 f'{todo_item_actions_table}')

    def usage(self):
        return """\
Synopsis: help item
          helpitem
          item help
          itemhelp\
"""

    def help(self):
        return """Lists default keyboard shortcuts for todo item actions in the Column UI."""
