from topydo.lib.DCommand import DCommand


class DoNowCommand(DCommand):
    def __init__(self, p_args, p_todolist, #pragma: no branch
                 p_out=lambda a: None,
                 p_err=lambda a: None,
                 p_prompt=lambda a: None):
        super().__init__(p_args, p_todolist, p_out, p_err, p_prompt)

    def prefix(self):
        return 'DOING: '

    def execute_specific_core(self, p_todo):
        print('=== EXECUTE DONOW CMD HERE ===')

    def execute_specific(self, p_todo):
        self.out(self.prefix() + self.printer.print_todo(p_todo))
        self.execute_specific_core(p_todo)

    def usage(self):
        return """Synopsis: donow <NUMBER>"""

    def help(self):
        return """Tracks total time spent on the todo item specified by NUMBER."""
