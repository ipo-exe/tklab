import os
import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import END, RIGHT, LEFT, BooleanVar, DISABLED, NORMAL
import webbrowser
import pandas as pd
import backend, inp


def callsub():

    import subprocess
    subprocess.run(["inkscape"])


def quit():
    """
    smart exit function
    :return:
    """
    b_ans = messagebox.askyesno(title='Exit', message='Confirm exit?')
    if b_ans:
        root.destroy()


def save():
    """
    save file
    :return:
    """
    global s_metadata_filepath, df_meta
    get_entry_metadata()
    # export to file
    df_meta.to_csv(s_metadata_filepath, sep=';', index=False)
    print_report_msg(s_msg='Save : Saved to {}'.format(s_metadata_filepath))


def save_as():
    """
    save as file routine
    :return:
    """
    global s_metadata_filepath
    s_ans = fd.asksaveasfilename(title='Save As',
                                 initialdir=dct_etr_wplc['Input Folder'].get(),
                                 filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
    if str(s_ans) == '()' or s_ans == '':
        pass
    else:
        s_metadata_filepath = s_ans
        save()
        # enable save
        menu_file.entryconfig(2, state=NORMAL)


def print_report_msg(s_msg):
    """
    report string message to log listbox
    :param s_msg:
    :return:
    """
    # report
    listbox_log.config(state=NORMAL)
    s_report = ' {} >>> {}'.format(backend.timestamp_log(), s_msg)
    listbox_log.insert(END, s_report)
    listbox_log.config(state=DISABLED)


def reload_entries():
    """
    Reload entries from tool metadata dataframe
    :return:
    """
    # workplace
    for k in dct_etr_wplc:
        df_lcl = df_meta.query('Metadata == "{}"'.format(k))
        # retrieve value from metadata
        s_reload = df_lcl['Value'].values[0]
        if pd.isna(s_reload):
            print(s_reload)
            s_reload = ''
        # clear first
        dct_etr_wplc[k].delete(0, END)
        # insert
        dct_etr_wplc[k].insert(0, s_reload)
    # input files
    for k in dct_etr_input:
        df_lcl = df_meta.query('Metadata == "{}"'.format(k))
        # retrieve value from metadata
        s_reload = df_lcl['Value'].values[0]
        if pd.isna(s_reload):
            print(s_reload)
            s_reload = ''
        # clear first
        dct_etr_input[k].delete(0, END)
        # insert
        dct_etr_input[k].insert(0, s_reload)
    # parameters
    for k in dct_var_params:
        df_lcl = df_meta.query('Metadata == "{}"'.format(k))
        # retrieve value from metadata
        s_reload = df_lcl['Value'].values[0]
        # set
        dct_var_params[k].set(bool(s_reload))


def new_session():
    """
    start new session
    :return:
    """
    b_ans = messagebox.askokcancel(title='New Session', message='Confirm new?')
    if b_ans:
        clear_metadata()
        # fix colors
        for k in dct_lbls_wplc:
            dct_lbls_wplc[k].config(foreground=color_fg)
        for k in dct_lbls_input:
            dct_lbls_input[k].config(foreground=color_fg)
        # disable save
        menu_file.entryconfig(2, state=DISABLED)
        reset_status()
        get_entry_metadata()
        authorize()


def clear_metadata():
    """
    flush out tool metadata
    :return:
    """
    # clear entries
    for k in dct_etr_wplc:
        dct_etr_wplc[k].delete(0, END)
    for k in dct_etr_input:
        dct_etr_input[k].delete(0, END)
    for k in dct_var_params:
        dct_var_params[k].set(False)
    # update dataframe
    get_entry_metadata()
    # clear log
    listbox_log.config(state=NORMAL)
    listbox_log.delete(0, END)
    listbox_log.config(state=DISABLED)
    print_report_header()


def run():
    """
    run button routine
    :return:
    """
    global df_meta, b_ok_to_run
    # report
    print_report_msg(s_msg='Run : Processing...')
    # update things
    update_all_entries(b_popup=False, b_report_error=True, b_report_update=False, b_silent=True)
    if b_ok_to_run:
        # freeze button
        button_run.config(state=DISABLED)

        # run things
        s_lcl_wkplc = df_meta[df_meta['Metadata'] == 'Run Folder']['Value'].values[0]
        s_folder =  backend.create_rundir(label='BASIC', wkplc=s_lcl_wkplc)
        df_meta.to_csv('{}/meta.txt'.format(s_folder), sep=';', index=False)


        # enable button
        button_run.config(state=NORMAL)
        # report
        print_report_msg(s_msg='Run : Task done')
        print_report_msg(s_msg='Run : Results at {}'.format(s_folder))


def get_entry_metadata():
    """
    get from entries all metadata
    :return:
    """
    global df_meta, lst_lbls_wplc, dct_etr_wplc, lst_lbls_inpfiles, dct_etr_input, lst_lbls_params, dct_var_params
    lst_metadata = list()
    lst_entry_n = list()
    lst_category = list()
    lst_values = list()
    lst_status = list()
    # append timestamp
    lst_metadata.append('Timestamp')
    lst_entry_n.append('-')
    lst_category.append('last update')
    lst_values.append(backend.timestamp_log())
    lst_status.append(True)
    # update folders
    for i in range(len(lst_lbls_wplc)):
        s_lcl_key = lst_lbls_wplc[i]
        lst_metadata.append(s_lcl_key)
        lst_entry_n.append(str(i))
        lst_category.append('directory')
        lst_values.append(dct_etr_wplc[s_lcl_key].get())
    # update files
    for i in range(len(lst_lbls_inpfiles)):
        s_lcl_key = lst_lbls_inpfiles[i]
        lst_metadata.append(s_lcl_key)
        lst_entry_n.append(str(i))
        lst_category.append('file')
        lst_values.append(dct_etr_input[s_lcl_key].get())
    # update params
    for i in range(len(lst_lbls_params)):
        s_lcl_key = lst_lbls_params[i]
        lst_metadata.append(s_lcl_key)
        lst_entry_n.append(str(i))
        lst_category.append('parameter')
        lst_values.append(dct_var_params[s_lcl_key].get())
    # re-instantiate dataframe
    df_meta = pd.DataFrame({'Metadata': lst_metadata,
                            'Category': lst_category,
                            'Entry': lst_entry_n,
                            'Value':lst_values})


def authorize():
    """
    evaluate if is ok to run -- all metadata must be OK
    :return:
    """
    global b_ok_to_run
    b_ok_to_run = True
    for k in dct_status:
        b_ok_to_run = b_ok_to_run * dct_status[k]
    if b_ok_to_run:
        button_run.config(state=NORMAL)
    else:
        button_run.config(state=DISABLED)


def open_about_input(n_entry=0):
    """
    open doc link of input file
    :param n_entry:
    :return:
    """
    webbrowser.open(url=lst_urls_inpfiles[n_entry])


def reset_status():
    """
    reset run status
    :return:
    """
    global dct_status
    # status setup
    dct_status = dict()
    for k in lst_lbls_wplc:
        dct_status[k] = False
    for k in lst_lbls_inpfiles:
        dct_status[k] = False


def update_all_entries(b_popup=True, b_report_error=True, b_report_update=True, b_silent=False):
    """
    Update all entries
    :return:
    """
    if b_silent:
        # report
        print_report_msg(s_msg='Update')
    # workplace
    for i in range(len(lst_lbls_wplc)):
        update_folder(n_entry=i,
                      b_popup=b_popup,
                      b_report_error=b_report_error,
                      b_report_update=b_report_update)
    # input files
    for i in range(len(lst_lbls_inpfiles)):
        update_file(n_entry=i,
                      b_popup=b_popup,
                      b_report_error=b_report_error,
                      b_report_update=b_report_update)


def update_folder(n_entry=0, b_popup=True, b_report_error=True, b_report_update=True):
    """
    Update folder entry
    :param n_entry: int index of entry
    :return:
    """
    global df_meta, lst_lbls_wplc
    s_lcl_key = lst_lbls_wplc[n_entry]
    s_path = dct_etr_wplc[s_lcl_key].get()
    if len(s_path) == 0:
        # change color
        dct_lbls_wplc[s_lcl_key].config(foreground='red')
        # change status
        dct_status[s_lcl_key] = False
        # message
        if b_popup:
            messagebox.showerror(title='Error', message='{}: empty entry'.format(s_lcl_key))
        if b_report_error:
            # report
            print_report_msg(s_msg='{} : Error -- empty entry'.format(s_lcl_key))
    else:
        if os.path.isdir(s_path):
            # change color
            dct_lbls_wplc[s_lcl_key].config(foreground=color_fg)
            # change status
            dct_status[s_lcl_key] = True
            if b_popup:
                tkinter.messagebox.showinfo(message='{}: updated'.format(s_lcl_key))
            if b_report_update:
                # report
                print_report_msg(s_msg='{} : Updated {}'.format(s_lcl_key, s_path))
        else:
            # change color
            dct_lbls_wplc[s_lcl_key].config(foreground='red')
            # change status
            dct_status[s_lcl_key] = False
            if b_popup:
                tkinter.messagebox.showerror(title='Error', message='{}: not found'.format(s_lcl_key))
            if b_report_error:
                # report
                print_report_msg(s_msg='{} : Error -- empty entry'.format(s_lcl_key))
    # get entry metadata
    get_entry_metadata()
    # authorize run
    authorize()


def update_file(n_entry=0, b_popup=True, b_report_error=True, b_report_update=True):
    """
    Update file entry
    :param n_entry: int index of entry
    :return:
    """
    global df_meta, lst_lbls_inpfiles
    s_lcl_key = lst_lbls_inpfiles[n_entry]
    s_path = dct_etr_input[s_lcl_key].get()
    if len(s_path) == 0:
        # change color
        dct_lbls_input[s_lcl_key].config(foreground='red')
        # change status
        dct_status[s_lcl_key] = False
        # message
        if b_popup:
            messagebox.showerror(title='Error', message='{}: empty entry'.format(s_lcl_key))
        if b_report_error:
            # report
            print_report_msg(s_msg='{} : Error -- empty entry'.format(s_lcl_key))
    else:
        if os.path.isfile(s_path):
            # reset color
            dct_lbls_input[s_lcl_key].config(foreground=color_fg)
            # change status
            dct_status[s_lcl_key] = True
            # message
            if b_popup:
                tkinter.messagebox.showinfo(message='{}: updated'.format(s_lcl_key))
            if b_report_update:
                # report
                print_report_msg(s_msg='{} : Updated {}'.format(s_lcl_key, s_path))
        else:
            # change color
            dct_lbls_input[s_lcl_key].config(foreground='red')
            # change status
            dct_status[s_lcl_key] = False
            # message
            if b_popup:
                tkinter.messagebox.showerror(title='Error', message='{}: not found'.format(s_lcl_key))
            if b_report_error:
                # report
                print_report_msg(s_msg='{} : Error -- not found'.format(s_lcl_key))
    # get entry metadata
    get_entry_metadata()
    # authorize run
    authorize()


def pick_folder(n_entry=0):
    """
    pick folder helper
    :param n_entry: int index of folder entry
    :return:
    """
    global lst_lbls_wplc
    while True:
        s_folderpath = fd.askdirectory(title='Select a folder')
        if len(s_folderpath) == 0:
            break
        # confirm exit
        b_ans = tkinter.messagebox.askokcancel(title='Confirm folder', message=s_folderpath)
        if b_ans:
            # change entry
            dct_etr_wplc[lst_lbls_wplc[n_entry]].delete(0, END) # clear
            dct_etr_wplc[lst_lbls_wplc[n_entry]].insert(0, s_folderpath) # insert
            update_folder(n_entry=n_entry)
            break


def pick_file(tpl_file_type, s_initialdir, n_entry=0):
    """
    pick file helper
    :param tpl_file_type: tuple of file type
    :param s_initialdir: string path to initial dir
    :param n_entry:
    :return:
    """
    global lst_lbls_inpfiles
    while True:
        tpl_filetypes = (tpl_file_type, ('All files', '*.*'))
        s_filepath = fd.askopenfilename(title='Select a file',
                                        initialdir=s_initialdir,
                                        filetypes=tpl_filetypes)

        if len(s_filepath) == 0:
            break
        # confirm exit
        b_ans = messagebox.askokcancel(title='Confirm file', message=s_filepath)
        if b_ans:
            # change entry
            dct_etr_input[lst_lbls_inpfiles[n_entry]].delete(0, END)  # clear
            dct_etr_input[lst_lbls_inpfiles[n_entry]].insert(0, s_filepath)  # insert
            update_file(n_entry=n_entry)
            break


def load_tool_file():
    global dct_etr_wplc, lst_lbls_wplc
    global s_metadata_filepath
    s_initialdir = dct_etr_wplc[lst_lbls_wplc[0]].get()
    tpl_filetypes = (('Text File', '*.txt'), ('All files', '*.*'))
    s_filepath = fd.askopenfilename(title='Select a file',
                                    initialdir=s_initialdir,
                                    filetypes=tpl_filetypes)
    if len(s_filepath) == 0:
            pass
    else:
        s_metadata_filepath = s_filepath
        load_metadata()
        # enable save
        menu_file.entryconfig(2, state=NORMAL)


def load_metadata():
    """
    load metadata from file
    :return:
    """
    global s_metadata_filepath, df_meta
    if os.path.isfile(s_metadata_filepath):
        s_fields = 'Metadata & Category & Entry & Value'
        dct_inp = inp.open_df(s_filepath=s_metadata_filepath, s_mandatory_fields=s_fields)
        if dct_inp['OK Flag']:
            # check more things
            df_loaded = dct_inp['df']
            # check length
            if len(df_loaded) != len(df_meta):
                messagebox.showerror(title='Error', message='Invalid Formatting')
            # check static values match
            else:
                sr_aux = (df_loaded[['Metadata','Category','Entry']] == df_meta[['Metadata','Category','Entry']])
                b_aux = sr_aux.min().min().min()
                if b_aux:
                    df_meta = df_loaded
                    # report
                    print_report_msg(s_msg='Open : {}'.format(s_metadata_filepath))
                    reload_entries()
                    update_all_entries(b_popup=False)
                else:
                    messagebox.showerror(title='Error', message='Invalid Formatting')
        else:
            messagebox.showerror(title='Error', message=dct_inp['Error Report'])
            # report
            print_report_msg(s_msg='Open : Error -- {}'.format(dct_inp['Error Report']))


def print_report_header():
    print_report_msg(s_msg=' {} Basic Tool {} '.format('*' * 30, '*' * 30))
    print_report_msg(s_msg='Initiate session')


# >>> define window
root = tkinter.Tk()

# tool setup
lst_lbls_wplc = ['Input Folder', 'Run Folder']
lst_lbls_inpfiles = ['CSV Table 1', 'CSV Table 2', 'CSV Table 3']
lst_urls_inpfiles = ['https://www.google.com', 'https://www.google.com', 'https://www.google.com']
lst_types_inpfiles = [('Text File', '*.txt'), ('Text File', '*.txt'), ('Text File', '*.txt')]
lst_lbls_params = ['Plot results', 'Compute Stats']

# status
reset_status()


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

# icons setup
img_logo = tkinter.PhotoImage(file='figs/logo_color_70x70.png')
img_open = tkinter.PhotoImage(file='figs/open.png')
img_about = tkinter.PhotoImage(file='figs/info.png')
img_play = tkinter.PhotoImage(file='figs/play.png')
img_save = tkinter.PhotoImage(file='figs/save.png')
img_exit = tkinter.PhotoImage(file='figs/exit.png')
img_file = tkinter.PhotoImage(file='figs/file.png')
img_update = tkinter.PhotoImage(file='figs/update.png')

# files setup
s_title = 'Basic Tool'
root.title(s_title)

# >> set menus
menubar = tkinter.Menu(root, bg=color_bg, activeforeground=color_actbg, foreground=color_fg,
                       bd=0)
root.config(menu=menubar)

# >> create the file_menu
menu_file = tkinter.Menu(menubar, tearoff=0, bg=color_bg_alt, activebackground=color_actbg)
# add menu items to the File menu
menu_file.add_command(label='New ', image=img_file, compound=LEFT,
                      foreground=color_fg, activeforeground=color_fg,
                      command=new_session)
menu_file.add_command(label='Open', image=img_open, compound=LEFT,
                      foreground=color_fg, activeforeground=color_fg,
                      command=load_tool_file)
menu_file.add_command(label='Save', image=img_save, compound=LEFT, foreground=color_fg, activeforeground=color_fg,
                      command=save)
# disable save
menu_file.entryconfig(2, state=DISABLED)
menu_file.add_command(label='Save As', image=img_save, compound=LEFT, foreground=color_fg, activeforeground=color_fg,
                      command=save_as)
menu_file.add_separator()
# add Exit menu item
menu_file.add_command(label='Exit', image=img_exit, compound=LEFT,
                      foreground=color_fg, activeforeground=color_fg, command=quit)
# add the File menu to the menubar
menubar.add_cascade(label="File", menu=menu_file, activeforeground=color_fg, activebackground=color_actbg)


# frames layout

frame_header = tkinter.Frame(root, width=n_width, bg=color_bg)
frame_info = tkinter.Frame(frame_header, bg=color_bg)
frame_logo = tkinter.Frame(frame_header, bg=color_bg)
frame_workplace = tkinter.LabelFrame(root, text='Workplace', width=n_width,
                                     bg=color_bg, foreground=color_fg, )
frame_inputfiles = tkinter.LabelFrame(root, text='Input files', width=n_width,
                                      bg=color_bg, foreground=color_fg)
frame_runparams = tkinter.LabelFrame(root, text='Options', width=n_width,
                                     bg=color_bg, foreground=color_fg)
frame_board = tkinter.Frame(root, width=n_width, bg=color_bg)
frame_reports = tkinter.Frame(root, width=n_width)

frame_header.pack(fill='x', padx=n_frame_padx)
frame_logo.pack(fill='x', padx=n_frame_padx, side=RIGHT)
frame_info.pack(fill='y', padx=n_frame_padx, side=RIGHT)
frame_workplace.pack(fill='x', padx=n_frame_padx, pady=n_frame_pady)
frame_inputfiles.pack(fill='x', padx=n_frame_padx, pady=n_frame_pady)
frame_runparams.pack(fill='x', padx=n_frame_padx, pady=n_frame_pady)
frame_board.pack(padx=n_frame_padx, pady=n_frame_pady)
frame_reports.pack(padx=n_frame_padx, pady=n_frame_pady)


# >> Header layout

label_logo = tkinter.Label(frame_logo, image=img_logo, width=70,
                           bg=color_bg, activebackground=color_actbg,
                           foreground=color_fg, activeforeground=color_fg)
label_logo.pack(side=RIGHT)

s_head_msg = 'Basic Tool'
label_infos = tkinter.Label(frame_info, text=s_head_msg, width=n_width, anchor='w',
                            bg=color_bg, activebackground=color_actbg,
                            foreground=color_fg, activeforeground=color_fg)
label_infos.pack()

# >> Workplace Frame layout

# place widgets
dct_lbls_wplc = dict()
dct_etr_wplc = dict()
dct_btn_update_wplc = dict()
dct_btn_search_wplc = dict()
for i in range(len(lst_lbls_wplc)):
    s_lcl_key = lst_lbls_wplc[i]
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

# >> Main Board
n_lcl_width = 70
# run button
button_run = tkinter.Button(frame_board, text='Run', image=img_play, compound=LEFT, width=n_lcl_width)
button_run.config(bg=color_bg_alt, activebackground=color_actbg, disabledforeground='grey',
                  foreground=color_fg, activeforeground=color_fg, highlightbackground=color_bg, bd=0)
button_run.config(command=run)
button_run.config(state=DISABLED)
button_run.pack(side=RIGHT, padx=2)
# update button
button_update_entries = tkinter.Button(frame_board, text='Update', image=img_update, compound=LEFT, width=n_lcl_width)
button_update_entries.config(bg=color_bg_alt, activebackground=color_actbg, disabledforeground='grey',
                             foreground=color_fg, activeforeground=color_fg, highlightbackground=color_bg, bd=0)
button_update_entries.config(command=lambda : update_all_entries(b_popup=False))
button_update_entries.pack(side=RIGHT, padx=2)


# Report Log frame widgets
scrollbar_log_y = tkinter.Scrollbar(frame_reports, bg=color_bg_alt, bd=0, activebackground=color_actbg)
scrollbar_log_x = tkinter.Scrollbar(frame_reports, orient='horizontal', bg=color_bg_alt, bd=0, activebackground=color_actbg)
listbox_log = tkinter.Listbox(frame_reports, height=12, width=94,
                              borderwidth=0, bd=0,
                              bg='black', foreground=color_fg, highlightbackground=color_bg,
                              yscrollcommand=scrollbar_log_y.set,
                              xscrollcommand=scrollbar_log_x.set)
scrollbar_log_y.config(command=listbox_log.yview)
scrollbar_log_x.config(command=listbox_log.xview)
listbox_log.grid(row=0, column=0)
scrollbar_log_y.grid(row=0, column=1, sticky='NS')
scrollbar_log_x.grid(row=1, column=0, sticky='WE')
listbox_log.config(state=DISABLED)
print_report_header()

# >>> Commands

# config workplace search buttons commmands
dct_btn_search_wplc['Input Folder'].config(command=lambda : pick_folder(n_entry=0))
dct_btn_search_wplc['Run Folder'].config(command=lambda : pick_folder(n_entry=1))
dct_btn_update_wplc['Input Folder'].config(command=lambda : update_folder(n_entry=0))
dct_btn_update_wplc['Run Folder'].config(command=lambda : update_folder(n_entry=1))

# config input update buttons commmands
dct_btn_update[lst_lbls_inpfiles[0]].config(command=lambda : update_file(n_entry=0))
dct_btn_update[lst_lbls_inpfiles[1]].config(command=lambda : update_file(n_entry=1))
dct_btn_update[lst_lbls_inpfiles[2]].config(command=lambda : update_file(n_entry=2))

# config input search buttons commmands
dct_btn_input[lst_lbls_inpfiles[0]].config(command=lambda : pick_file(n_entry=0, tpl_file_type=lst_types_inpfiles[0],
                                                                      s_initialdir=dct_etr_wplc['Input Folder'].get()))
dct_btn_input[lst_lbls_inpfiles[1]].config(command=lambda : pick_file(n_entry=1, tpl_file_type=lst_types_inpfiles[1],
                                                                      s_initialdir=dct_etr_wplc['Input Folder'].get()))
dct_btn_input[lst_lbls_inpfiles[2]].config(command=lambda : pick_file(n_entry=2, tpl_file_type=lst_types_inpfiles[2],
                                                                      s_initialdir=dct_etr_wplc['Input Folder'].get()))
# config input about buttons commands
dct_btn_about[lst_lbls_inpfiles[0]].config(command=lambda : open_about_input(n_entry=0))
dct_btn_about[lst_lbls_inpfiles[1]].config(command=lambda : open_about_input(n_entry=1))
dct_btn_about[lst_lbls_inpfiles[2]].config(command=lambda : open_about_input(n_entry=2))


get_entry_metadata()

# run root window
root.mainloop()