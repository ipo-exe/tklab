import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import END, RIGHT, LEFT, BooleanVar, DISABLED, NORMAL
import webbrowser
import pandas as pd
import backend


def load_metadata():
    print('todo')


def clear_metadata():
    print('todo')
    # clear entries
    for k in dct_etr_wplc:
        dct_etr_wplc[k].delete(0, END)
    for k in dct_etr_input:
        dct_etr_input[k].delete(0, END)
    # update dataframe
    get_entry_metadata()
    # clear log
    listbox_log.config(state=NORMAL)
    listbox_log.delete(0, END)
    listbox_log.config(state=DISABLED)
    print_log_header()


def run():
    global df_meta, b_ok_to_run
    authorize()
    if b_ok_to_run:
        # freeze button
        button_run.config(state=DISABLED)
        # report
        listbox_log.config(state=NORMAL)
        s_report = '{} >> Run : Processing...'.format(backend.timestamp_log())
        listbox_log.insert(END, s_report)
        listbox_log.config(state=DISABLED)
        # run things
        s_lcl_wkplc = df_meta[df_meta['Metadata'] == 'Run Folder']['Value'].values[0]
        s_folder =  backend.create_rundir(label='BASIC', wkplc=s_lcl_wkplc)
        df_meta.to_csv('{}/meta.txt'.format(s_folder), sep=';', index=False)
        # enable button
        button_run.config(state=NORMAL)
        # report
        listbox_log.config(state=NORMAL)
        s_report = '{} >> Run : Task done'.format(backend.timestamp_log())
        listbox_log.insert(END, s_report)
        s_report = '{} >> Run : Results at {}'.format(backend.timestamp_log(), s_folder)
        listbox_log.insert(END, s_report)
        listbox_log.config(state=DISABLED)


def get_entry_metadata():
    """
    get from entries all metadata
    :return:
    """
    global df_meta
    lst_metadata = list()
    lst_values = list()
    lst_metadata.append('Timestamp')
    lst_values.append(backend.timestamp())
    for keys in dct_etr_wplc:
        lst_metadata.append(keys)
        lst_values.append(dct_etr_wplc[keys].get())
    for keys in dct_etr_input:
        lst_metadata.append(keys)
        lst_values.append(dct_etr_input[keys].get())
    for keys in dct_var_params:
        lst_metadata.append(keys)
        lst_values.append(dct_var_params[keys].get())
    df_meta = pd.DataFrame({'Metadata': lst_metadata, 'Value':lst_values})


def authorize():
    """
    evaluate if is ok to run -- all metadata must be on
    :return:
    """
    global b_ok_to_run, df_meta
    b_ok_to_run = True
    # update metadata dataframe
    get_entry_metadata()
    # compute
    for i in range(len(df_meta)):
        if df_meta['Value'].values[i] == '':
            b_lcl = False
        else:
            b_lcl = True
        b_ok_to_run = b_ok_to_run * b_lcl
    if b_ok_to_run:
        button_run.config(state=NORMAL)
    else:
        button_run.config(state=DISABLED)


def open_about(n_entry=0):
    webbrowser.open(url=lst_urls_inpfiles[n_entry])


def update_folder(n_entry=0):
    global df_meta
    # update run status
    authorize()
    s_folderpath = dct_etr_wplc[lst_labels_wplc[n_entry]].get()
    if len(s_folderpath) == 0:
        s_folderpath = 'Empty'
    # report
    listbox_log.config(state=NORMAL)
    s_report = '{} >> {} : {}'.format(backend.timestamp_log(), lst_labels_wplc[n_entry], s_folderpath)
    listbox_log.insert(END, s_report)
    listbox_log.config(state=DISABLED)


def update_file(n_entry=0):
    global df_meta
    # update run status
    authorize()
    s_filepath = dct_etr_input[lst_lbls_inpfiles[n_entry]].get()
    if len(s_filepath) == 0:
        s_filepath = 'Empty'
    # report
    listbox_log.config(state=NORMAL)
    s_report = '{} >> {} : {}'.format(backend.timestamp_log(), lst_lbls_inpfiles[n_entry], s_filepath)
    listbox_log.insert(END, s_report)
    listbox_log.config(state=DISABLED)


def pick_folder(n_entry=0):
    while True:
        s_folderpath = fd.askdirectory(title='Select a folder')
        if len(s_folderpath) == 0:
            break
        # confirm exit
        b_ans = tkinter.messagebox.askokcancel(title='Confirm folder', message=s_folderpath)
        if b_ans:
            # change entry
            dct_etr_wplc[lst_labels_wplc[n_entry]].delete(0, END) # clear
            dct_etr_wplc[lst_labels_wplc[n_entry]].insert(0, s_folderpath) # insert
            break
    # update run status
    authorize()
    # report
    listbox_log.config(state=NORMAL)
    s_report = '{} >> {} : {}'.format(backend.timestamp_log(), lst_labels_wplc[n_entry], s_folderpath)
    listbox_log.insert(END, s_report)
    listbox_log.config(state=DISABLED)


def pick_file(tpl_file_type, s_initialdir, n_entry=0):
    s_filepath = ''
    while True:
        tpl_filetypes = (tpl_file_type, ('All files', '*.*'))
        s_filepath = fd.askopenfilename(
            title='Open a file',
            initialdir=s_initialdir,
            filetypes=tpl_filetypes)
        if len(s_filepath) == 0:
            break
        # confirm exit
        b_ans = messagebox.askokcancel(title='Confirm file', message=s_filepath)
        if b_ans:
            # change entry
            dct_etr_input[lst_lbls_inpfiles[n_entry]].delete(0, END) # clear
            dct_etr_input[lst_lbls_inpfiles[n_entry]].insert(0, s_filepath) # insert
            update_file(n_entry=0)
            break


def print_log_header():
    # report
    listbox_log.config(state=NORMAL)
    listbox_log.insert(END, '************* Basic tool *************')
    s_report = '{} >>> Initiate session'.format(backend.timestamp_log())
    listbox_log.insert(END, s_report)
    listbox_log.config(state=DISABLED)


# >>> define window
root = tkinter.Tk()
s_title = 'Basic tool'
root.title(s_title)
# root.iconbitmap('wave.ico')  # use in Windows OS

# tool setup
lst_lbls_inpfiles = ['CSV Series 2']
lst_urls_inpfiles = ['https://www.google.com']
lst_types_inpfiles = [('Text CSV', '*.txt')]
lst_lbls_params = ['Plot results']

# geometry setup
n_height = 580
n_width = 800
n_entry_width = 52
root.geometry('{}x{}'.format(int(n_width), int(n_height)))
root.resizable(0,0)

# color setup
color_bg = '#343434'
color_bg_alt = '#484848'
color_actbg = '#df4a16'
color_fg = 'white'

# icons
img_open = tkinter.PhotoImage(file='figs/open.png')
img_about = tkinter.PhotoImage(file='figs/about.png')
img_run = tkinter.PhotoImage(file='figs/run.png')
img_save = tkinter.PhotoImage(file='figs/save.png')
img_exit = tkinter.PhotoImage(file='figs/exit.png')
img_file = tkinter.PhotoImage(file='figs/file.png')
img_update = tkinter.PhotoImage(file='figs/update.png')

root.config(bg=color_bg)

# >> set menus
menubar = tkinter.Menu(root, bg=color_bg, activeforeground=color_actbg, foreground=color_fg,
                       bd=0)
root.config(menu=menubar)

# >> create the file_menu
menu_file = tkinter.Menu(menubar, tearoff=0, bg=color_bg_alt, activebackground=color_actbg)
# add menu items to the File menu
menu_file.add_command(label='New ', image=img_file, compound=LEFT,
                      foreground=color_fg, activeforeground=color_fg,
                      command=clear_metadata)
menu_file.add_command(label='Open', image=img_open, compound=LEFT,
                      foreground=color_fg, activeforeground=color_fg,
                      command=load_metadata)
menu_file.add_command(label='Save', image=img_save, compound=LEFT, foreground=color_fg, activeforeground=color_fg)
menu_file.add_command(label='Save As', image=img_save, compound=LEFT, foreground=color_fg, activeforeground=color_fg)
menu_file.add_separator()
# add Exit menu item
menu_file.add_command(label='Exit', image=img_exit, compound=LEFT,
                      foreground=color_fg, activeforeground=color_fg, command=root.destroy)
# add the File menu to the menubar
menubar.add_cascade(label="File", menu=menu_file, activeforeground=color_fg, activebackground=color_actbg)


# frames layout
frame_header = tkinter.Frame(root, width=n_width, bg=color_bg)
frame_workplace = tkinter.LabelFrame(root, text='Workplace', width=n_width,
                                     bg=color_bg, foreground=color_fg, )
frame_inputfiles = tkinter.LabelFrame(root, text='Input files', width=n_width,
                                      bg=color_bg, foreground=color_fg)
frame_runparams = tkinter.LabelFrame(root, text='Options', width=n_width,
                                     bg=color_bg, foreground=color_fg)
frame_board = tkinter.Label(root, width=n_width,
                            bg=color_bg, foreground=color_fg)
frame_log = tkinter.Frame(root, width=n_width)
frame_header.pack(fill='x', padx=5, pady=5)
frame_workplace.pack(fill='x', padx=5, pady=5)
frame_inputfiles.pack(fill='x', padx=5, pady=5)
frame_runparams.pack(fill='x', padx=5, pady=5)
frame_board.pack(fill='x', padx=5, pady=5)
frame_log.pack(padx=5, pady=5)


# >> Header
label_head = tkinter.Label(frame_header, text=s_title, width=15,
                           bg=color_bg, activebackground=color_actbg,
                           foreground=color_fg, activeforeground=color_fg)
label_head.grid(row=0, column=0, padx=5, pady=5)

# >> Workplace
lst_labels_wplc = ['Input Folder', 'Run Folder']
# place widgets
dct_lbls_wplc = dict()
dct_etr_wplc = dict()
dct_btn_update_wplc = dict()
dct_btn_search_wplc = dict()
for i in range(len(lst_labels_wplc)):
    s_lcl_key = lst_labels_wplc[i]
    # labels
    dct_lbls_wplc[s_lcl_key] = tkinter.Label(frame_workplace, text=s_lcl_key, width=15, anchor="e",
                                             bg=color_bg, activebackground=color_actbg,
                                             foreground=color_fg, activeforeground=color_fg)
    dct_lbls_wplc[s_lcl_key].grid(row=i, column=0, pady=2, padx=2)
    # entries
    dct_etr_wplc[s_lcl_key] = tkinter.Entry(frame_workplace, width=n_entry_width,
                                            bg=color_bg_alt, foreground=color_fg,
                                            selectbackground=color_actbg, selectforeground=color_fg,
                                            highlightbackground=color_bg_alt, bd=1)
    dct_etr_wplc[s_lcl_key].grid(row=i, column=1, pady=2, padx=2)
    # update button
    dct_btn_update_wplc[s_lcl_key] = tkinter.Button(frame_workplace, image=img_update,
                                               bg=color_bg, activebackground=color_actbg,
                                               foreground=color_fg, activeforeground=color_fg,
                                               highlightbackground=color_bg, bd=0)
    dct_btn_update_wplc[s_lcl_key].grid(row=i, column=2, pady=2, padx=0)
    # search buttons
    dct_btn_search_wplc[s_lcl_key] = tkinter.Button(frame_workplace, text='Search', image=img_open, compound=LEFT,
                                                    bg=color_bg_alt, activebackground=color_actbg,
                                                    foreground=color_fg, activeforeground=color_fg,
                                                    highlightbackground=color_bg_alt, bd=0)
    dct_btn_search_wplc[s_lcl_key].grid(row=i, column=3, pady=2, padx=2)

# >> Input files

# place widgets
dct_lbls_input = dict()
dct_etr_input = dict()
dct_btn_update = dict()
dct_btn_input = dict()
dct_btn_about = dict()
for i in range(len(lst_lbls_inpfiles)):
    s_lcl_key = lst_lbls_inpfiles[i]
    # label
    dct_lbls_input[s_lcl_key] = tkinter.Label(frame_inputfiles, text=s_lcl_key, width=15, anchor="e",
                                              bg=color_bg, activebackground=color_actbg,
                                              foreground=color_fg, activeforeground=color_fg
                                              )
    dct_lbls_input[s_lcl_key].grid(row=i, column=0, pady=2, padx=2)
    # entry
    dct_etr_input[s_lcl_key] = tkinter.Entry(frame_inputfiles, width=n_entry_width,
                                             bg=color_bg_alt, foreground=color_fg,
                                             selectbackground=color_actbg, selectforeground=color_fg,
                                             highlightbackground=color_bg_alt, bd=1)
    dct_etr_input[s_lcl_key].grid(row=i, column=1, pady=2, padx=2)
    # update button
    dct_btn_update[s_lcl_key] = tkinter.Button(frame_inputfiles, image=img_update,
                                              bg=color_bg, activebackground=color_actbg,
                                              foreground=color_fg, activeforeground=color_fg,
                                              highlightbackground=color_bg, bd=0)
    dct_btn_update[s_lcl_key].grid(row=i, column=2, pady=2, padx=0)
    # search button
    dct_btn_input[s_lcl_key] = tkinter.Button(frame_inputfiles, text='Search', image=img_open, compound=LEFT,
                                              bg=color_bg_alt, activebackground=color_actbg,
                                              foreground=color_fg, activeforeground=color_fg,
                                              highlightbackground=color_bg_alt, bd=0)
    dct_btn_input[s_lcl_key].grid(row=i, column=3, pady=2, padx=2)
    # about button
    dct_btn_about[s_lcl_key] = tkinter.Button(frame_inputfiles, text='About', image=img_about, compound=LEFT,
                                              bg=color_bg_alt, activebackground=color_actbg,
                                              foreground=color_fg, activeforeground=color_fg,
                                              highlightbackground=color_bg_alt, bd=0)
    dct_btn_about[s_lcl_key].grid(row=i, column=4, pady=2, padx=2)

# >> Tools Parameters

# place checkbuttons
dct_labels_params = dict()
dct_checks_params = dict()
dct_var_params = dict()
for i in range(len(lst_lbls_params)):
    s_lcl_key = lst_lbls_params[i]
    dct_var_params[s_lcl_key] = BooleanVar()
    dct_labels_params[s_lcl_key] = tkinter.Label(frame_runparams, text=s_lcl_key, width=20, anchor="e",
                                                 bg=color_bg, activebackground=color_actbg,
                                                 foreground=color_fg, activeforeground=color_fg
                                                 )
    dct_checks_params[s_lcl_key] = tkinter.Checkbutton(frame_runparams, variable=dct_var_params[s_lcl_key], width=2,
                                                       bg=color_bg, activebackground=color_actbg,
                                                       highlightbackground=color_bg, bd=0
                                                       )
    dct_labels_params[s_lcl_key].grid(row=i, column=0, pady=1, padx=10)
    dct_checks_params[s_lcl_key].grid(row=i, column=1, pady=1)

# >> Board
button_run = tkinter.Button(frame_board, text='Run', width=10)
button_run.config(bg=color_bg_alt, activebackground=color_actbg, disabledforeground='grey',
                  foreground=color_fg, activeforeground=color_fg, highlightbackground=color_bg, bd=0)
button_run.pack(anchor='e', side=RIGHT)
label_runicon = tkinter.Label(frame_board, image=img_run, compound=LEFT, bg=color_bg, activebackground=color_actbg,
                                                 foreground=color_fg, activeforeground=color_fg)
label_runicon.pack(anchor='e', side=RIGHT)

# log pannel
scrollbar_log = tkinter.Scrollbar(frame_log, width=10, bg=color_bg_alt, bd=0, activebackground=color_actbg)
listbox_log = tkinter.Listbox(frame_log, height=13, width=94,
                              borderwidth=0, bd=0,
                              bg='black', foreground=color_fg, highlightbackground=color_bg,
                              yscrollcommand=scrollbar_log.set)
scrollbar_log.config(command=listbox_log.yview)
listbox_log.grid(row=0, column=0)
scrollbar_log.grid(row=0, column=1, sticky='NS')
listbox_log.config(state=DISABLED)
print_log_header()

# >>> Commands

# config workplace search buttons commmands
dct_btn_search_wplc['Input Folder'].config(command=lambda : pick_folder(n_entry=0))
dct_btn_search_wplc['Run Folder'].config(command=lambda : pick_folder(n_entry=1))
dct_btn_update_wplc['Input Folder'].config(command=lambda : update_folder(n_entry=0))
dct_btn_update_wplc['Run Folder'].config(command=lambda : update_folder(n_entry=1))

# config input search buttons commmands
dct_btn_update[lst_lbls_inpfiles[0]].config(command=lambda : update_file(n_entry=0))
dct_btn_input[lst_lbls_inpfiles[0]].config(command=lambda : pick_file(n_entry=0, tpl_file_type=lst_types_inpfiles[0],
                                                                      s_initialdir=dct_etr_wplc['Input Folder'].get()))
# config input about buttons commands
dct_btn_about[lst_lbls_inpfiles[0]].config(command=lambda : open_about(n_entry=0))
authorize()
button_run.config(command=run)

# run root window
root.mainloop()