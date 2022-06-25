import tkinter
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('600x600')
root.title('Notebook Demo')

frame0 = tkinter.LabelFrame(root, text='OK', width=200, bg='red')
frame0.pack(fill='both', expand=True)
lbl = tkinter.Label(frame0, text='label')
lbl.pack()

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')


root.mainloop()