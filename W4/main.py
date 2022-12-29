import tkinter as tk
from typing import Callable

"""
A few quick notes:
- Buttons on MacOS can not be simply changed it's fg and bg color using built-in components.
"""
class Application(tk.Tk):
    def __init__(self, config: dict):
        self.__config = config
        self.title = config.pop('title', 'My Application')
        super().__init__(**self.__config)

    def add_button(
        self,
        row: int, 
        column: int, 
        text = 'Button', 
        callback: Callable = None,
        grid_config: dict = {},
        **kwargs
    ):
        new_btn = tk.Button(self, text=text, **kwargs)
        new_btn.grid(row=row, column=column, **grid_config)


def run_application():
    config = {
        'screenName': None,
        'baseName': None,
        'className': 'Tk',
        'useTk': True,
        'sync': False,
        'use': None,
        'title': 'Myyyy'
    }

    app = Application(config=config)

    btn = tk.Button(app, text='My Text')

    btn.pack()
    switch = tk.IntVar(app)
    switch.set(1)

    app.mainloop()


if __name__ == '__main__':
    run_application()
