import tkinter as tk
from chat import Chat


class Messager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1200x500")
        self.title("Chat App")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.chat_frame = Chat(self)
        self.chat_frame.grid(row=0, column=0, sticky='nsew')

        self.mainloop()

Messager()