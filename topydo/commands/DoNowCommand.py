from topydo.lib.DCommand import DCommand
from topydo.commands.TagCommand import TagCommand
import time


class DoNowCommand(DCommand):
    def __init__(self, p_args, p_todolist, #pragma: no branch
                 p_out=lambda a: None,
                 p_err=lambda a: None,
                 p_prompt=lambda a: None):
        super().__init__(p_args, p_todolist, p_out, p_err, p_prompt)

        self.todo_id = p_args[0]

    def prefix(self):
        return 'DOING: '

    def execute_specific_core(self, p_todo):
        # min_value = p_todo.tag_values('min')
        min_value = 0 if len(p_todo.tag_values('min')) == 0 else int(p_todo.tag_values('min')[0])
        # print(min_value)
        min_elapsed = 0

        try:
            while True:
                time.sleep(1 * 60)
                min_elapsed += 1
                # print(min_elapsed)
        except KeyboardInterrupt:
            TagCommand([self.todo_id, 'min', f'{min_value + min_elapsed}'], self.todolist).execute()
            self.out(f'\n{min_elapsed} MINUTE(S) PASSED\n'
                     f'UPDATED TODO: |{self.todo_id}| {self.printer.print_todo(p_todo)}')

    def execute_specific(self, p_todo):
        self.out(self.prefix() + self.printer.print_todo(p_todo))
        self.execute_specific_core(p_todo)

    def usage(self):
        return """Synopsis: donow <NUMBER>"""

    def help(self):
        return """Tracks total time in minutes spent on the todo item specified by NUMBER. Timer is stopped using CTRL+C."""
