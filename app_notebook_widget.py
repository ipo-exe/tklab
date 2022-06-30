import tkinter
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
# geometry setup
n_height = 650
n_width = 800
n_entry_width = 52
n_frame_padx = 5
n_frame_pady = 2

root.geometry('{}x{}'.format(int(n_width), int(n_height)))
root.resizable(0,0)

# color setup
color_bg = '#343434'
color_bg_alt = '#484848'
color_actbg = '#df4a16'
color_fg = 'white'
root.config(bg=color_bg)

root.title('Notebook Demo')

frame0 = tkinter.LabelFrame(root, text='OK', width=200, bg=color_bg_alt)
frame0.pack(fill='both', expand=True)
lbl = tkinter.Label(frame0, text='label')
lbl.pack()

style_notebook = ttk.Style()
style_notebook.configure("TNotebook", background=color_bg_alt, )
style_notebook.configure("TNotebook.Tab", background=color_bg, foreground=color_fg, bd=0)
style_notebook.map("TNotebook", background=[("selected", 'red'), ('!active', color_bg), ('active', 'green')])
# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', pady=10, padx=10, expand=True)


# create frames
frame_notebook1 = tkinter.Frame(notebook, bg=color_bg_alt)
frame_notebook2 = tkinter.Frame(notebook, bg=color_bg_alt)

frame_notebook1.pack(fill='both', expand=True)
frame_notebook2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame_notebook1, text='General Information')
notebook.add(frame_notebook2, text='Profile            ')


label = tkinter.Label(frame_notebook1, text='OK')
label.pack()

root.mainloop()