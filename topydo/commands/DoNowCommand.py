from topydo.lib.Command import Command, InvalidCommandArgument
from topydo.lib.TodoListBase import InvalidTodoException
from topydo.commands.TagCommand import TagCommand
import time


class DoNowCommand(Command):
    def __init__(self, p_args, p_todolist, #pragma: no branch
                 p_out=lambda a: None,
                 p_err=lambda a: None,
                 p_prompt=lambda a: None):
        super().__init__(p_args, p_todolist, p_out, p_err, p_prompt)

    def execute(self):
        if not super().execute():
            return False

        try:
            todo_id = self.argument(0)
            todo = self.todolist.todo(todo_id)

            self.out(f'DOING: {self.printer.print_todo(todo)}')

            min_value = 0 if len(todo.tag_values('min')) == 0 else int(todo.tag_values('min')[0])
            min_elapsed = 0

            try:
                while True:
                    time.sleep(1 * 60)
                    min_elapsed += 1
            except KeyboardInterrupt:
                TagCommand([todo_id, 'min', f'{min_value + min_elapsed}'], self.todolist).execute()
                self.out(f'\n{min_elapsed} MINUTE(S) PASSED\n'
                         f'UPDATED TODO: |{todo_id}| {self.printer.print_todo(todo)}')
        except InvalidCommandArgument:
            self.error(self.usage())
        except InvalidTodoException:
            self.error("Invalid todo number given.")

    def usage(self):
        return """Synopsis: donow <NUMBER>"""

    def help(self):
        return """Tracks total time in minutes spent on the todo item specified by NUMBER. Timer is stopped using CTRL+C."""
