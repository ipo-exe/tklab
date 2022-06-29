import pandas as pd


def open_df(s_filepath, s_sep=';', s_date_field='', s_mandatory_fields='',):
    """
    general dataframe openner
    :param s_filepath: string to file
    :param s_sep: string separator
    :param s_date_field: string datefield
    :param s_mandatory_fields: concat string of mandatory fields by ' & '
    :return: dict object with Error Report and dataframe
    """
    try:
        # handle date field
        if s_date_field == '':
            df_lcl = pd.read_csv(s_filepath, sep=s_sep, skipinitialspace=True)
        else:
            df_lcl = pd.read_csv(s_filepath, sep=s_sep, parse_dates=[s_date_field], skipinitialspace=True)
        # handle mandatory fields:
        if s_mandatory_fields == '':
            pass
        else:
            lst_fields = s_mandatory_fields.split(' & ')
            for f in lst_fields:
                try:
                    df_aux = df_lcl[f]
                except KeyError:
                    return {'Error Report': 'Invalid formatting.', 'OK Flag': False}
        return {'df': df_lcl, 'Error Report': 'File OK', 'OK Flag': True}
    except FileNotFoundError:
        return {'Error Report': 'File not found', 'OK Flag': False}
    except ValueError:
        return {'Error Report': 'Invalid formatting', 'OK Flag': False}