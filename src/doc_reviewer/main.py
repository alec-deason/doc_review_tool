
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from .data import DataModel
from .view import TaskQueryView

LARGE_FONT = ('Sans', 20, 'bold')


class DocumentReviewer(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid()

        self.data_model = None
        self.task_model = None

        self.frames = {'start': None,
                       'query': None,
                       'task': None}

        self.active_frame = None

        self.create_widgets()

    def create_widgets(self):
        top = self.winfo_toplevel()
        self.menu_bar = DocReviewerMenuBar(self)
        top['menu'] = self.menu_bar

        self.frames['start'] = StartPage(self)

        self.show('start')

    def load(self, file_name):
        self.data_model = DataModel(file_name)
        self.frames['query'] = TaskQueryView(self, self.data_model)
        self.show('query')

    def show(self, frame_name):
        if self.active_frame:
            self.active_frame.forget()
        self.active_frame = self.frames[frame_name]
        self.active_frame.grid(row=0, column=0)
        self.active_frame.tkraise()


class DocReviewerMenuBar(tk.Menu):

    def __init__(self, parent: DocumentReviewer):
        super().__init__(parent)
        self.parent = parent
        self.create_submenus()

    def create_submenus(self):
        self.file_menu = tk.Menu(self)
        self.file_menu.add_command(label='Open', command=self._open_handler)
        self.file_menu.add_command(label='Save', command=self._save_handler)

        self.add_cascade(label='File', menu=self.file_menu)

    def _open_handler(self):
        file_name = askopenfilename()
        self.parent.load(file_name)

    def _save_handler(self):
        pass


class StartPage(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text='doc_reviewer', font=LARGE_FONT)
        self.label.grid()
