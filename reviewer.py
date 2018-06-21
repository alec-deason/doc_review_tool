import tkinter as tk

from doc_reviewer.main import DocumentReviewer

root = tk.Tk()
root.geometry('1400x800')
root.title('Document Reviewer')
root.grid_columnconfigure(0, weight=1, pad=20)
root.grid_rowconfigure(0, weight=1, pad=20)
app = DocumentReviewer(root)
app.grid()
root.mainloop()
