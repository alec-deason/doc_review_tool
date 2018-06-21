import tkinter as tk
from tkinter import ttk


class TaskQueryView(ttk.Frame):

    def __init__(self, parent, data_model):
        super().__init__(parent)

        self.create_widgets(data_model)

    def create_widgets(self, data_model):
        self.check_bar = ColumnCheckBar(self, data_model.columns)
        self.check_bar.grid(row=0, column=0, padx=10, rowspan=1)
        self.new_column_entry = NewColumnEntry(self)
        self.new_column_entry.grid(row=0, column=1)


class ColumnCheckBar(ttk.Frame):

    def __init__(self, parent, columns):
        super().__init__(parent)
        self._columns = {o: tk.BooleanVar() for o in columns}

        self.create_widgets()

    def create_widgets(self):

        for i, (column, var) in enumerate(self._columns.items()):
            c = ttk.Checkbutton(self, text=column, variable=var)
            c.grid(row=i, column=0, ipadx=10, ipady=4, sticky='ew')

    def get_state(self):
        return [o for o, v in self._columns.items() if v.get()]


class NewColumnEntry(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.entries = []
        self.create_widgets()

    def create_widgets(self):
        self.instructions = ttk.Label(self, text="""
        Please enter the names of the new columns you wish to create.
        """)
        self.instructions.grid(row=0)
        self.entry = ColumnEntryField(self)
        self.entry.grid(row=1)

    def add_selection(self, text):
        self.clear()
        self.entries.append(SelectedNewColumn(self, text))
        self.repaint()

    def clear(self):
        self.entry.grid_forget()
        for entry in self.entries:
            entry.grid_forget()

    def repaint(self):
        for i, entry in enumerate(self.entries):
            entry.grid(row=i+1)
        self.entry.grid(row=len(self.entries) + 1)

    def remove_selection(self, entry):
        self.clear()
        self.entries.remove(entry)
        self.repaint()


class ColumnEntryField(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.entry_field = ttk.Entry(self)
        self.entry_field.grid(row=0, column=0, columnspan=3)
        button = ttk.Button(self, text='Confirm', command=self.on_confirm)
        button.grid(row=0, column=3)

    def on_confirm(self):
        self.parent.add_selection(self.entry_field.get())


class SelectedNewColumn(ttk.Frame):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.parent = parent
        self.name = name
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text=self.name)
        label.grid(row=0, column=0)
        button = ttk.Button(self, text='Cancel', command=self.on_cancel)
        button.grid(row=0, column=1)

    def on_cancel(self):
        self.parent.remove_selection(self)
