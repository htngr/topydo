from topydo.lib.Command import Command, InvalidCommandArgument
from topydo.lib.TodoListBase import InvalidTodoException
from topydo.commands.TagCommand import TagCommand
import time


class DoNowCommand(Command):
    def __init__(self, p_args, p_todolist,  #pragma: no branch
                 p_out=lambda a: None,
                 p_err=lambda a: None,
                 p_prompt=lambda a: None,
                 testing=False,
                 testing_value=None):
        super().__init__(p_args, p_todolist, p_out, p_err, p_prompt)

        self.testing = testing
        self.testing_value = testing_value

    def execute(self):
        if not super().execute():
            return False

        todo_id = None
        todo = None
        min_value = None
        min_elapsed = 0
        unit_of_time = 1 if self.testing else 60

        try:
            todo_id = self.argument(0)
            todo = self.todolist.todo(todo_id)

            self.out(f'WORKING ON: {self.printer.print_todo(todo)}')

            min_value = 0 if len(todo.tag_values('min')) == 0 else int(todo.tag_values('min')[0])

            if self.testing and self.testing_value == 0:
                raise KeyboardInterrupt

            while True:
                time.sleep(1 * unit_of_time)
                min_elapsed += 1
                if self.testing and min_elapsed == self.testing_value:
                    raise KeyboardInterrupt
        except KeyboardInterrupt:
            TagCommand([todo_id, 'min', f'{min_value + min_elapsed}'], self.todolist).execute()
            self.out(f'\nMINUTE(S) PASSED: {min_elapsed}\n'
                     f'UPDATED TODO: |{todo_id}| {self.printer.print_todo(todo)}')
        except InvalidCommandArgument:
            self.error(self.usage())
        except InvalidTodoException:
            self.error('Invalid todo number.')

    def usage(self):
        return """Synopsis: donow <NUMBER>"""

    def help(self):
        return """\
Tracks total time in minutes spent on the todo item specified by NUMBER.
Timer is stopped using CTRL+C.\
"""
