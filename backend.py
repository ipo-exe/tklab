import os


def timestamp_log():
    import datetime
    s_aux = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')[:-4]
    return s_aux


def timestamp(s_sep='-'):
    """
    Generates a string timestamp
    :param s_sep: string separator
    :return: string timestamp
    """
    import datetime
    def_now = datetime.datetime.now()
    yr = def_now.strftime('%Y')
    mth = def_now.strftime('%m')
    dy = def_now.strftime('%d')
    hr = def_now.strftime('%H')
    mn = def_now.strftime('%M')
    sg = def_now.strftime('%S')
    fm = def_now.strftime('%f')
    def_lst = [yr, mth, dy, hr, mn, sg, fm]
    def_s = str(s_sep.join(def_lst))
    return def_s


def create_rundir(label='', wkplc='C:'):
    """
    Create a run directory
    :param label: string label
    :param wkplc: string folder path
    :return: string path to directory
    """
    dir_nm = wkplc + '/' + label + '_' + timestamp()
    os.mkdir(dir_nm)
    return dir_nm


def status(msg='Status message', process=True):
    """
    status message routine
    :param msg: string message
    :param process: boolean to denote process
    :return: none
    """
    if process:
        print('\t>>> {:60}...'.format(msg))
    else:
        print('\n\t>>> {:60}\n'.format(msg))