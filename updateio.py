import pandas as pd
import inp
import os

def basic_table():
    global lst_file
    lst_file.append('\t - Field separator: semicolon `;`;\n')
    lst_file.append('\t - Decimal separator: period `.`;\n')

def basic_series():
    global lst_file
    lst_file.append('\t - Field separator: semicolon `;`;\n')
    lst_file.append('\t - Decimal separator: period `.`;\n')
    lst_file.append('\t - Time resolution: daily timesteps;\n')
    lst_file.append('\t - Date format: `YYYY-MM-DD`;\n')


def basic_map():
    lst_file.append('\t - Void cells value: not allowed - all grid cells must be filled with data;\n')
    lst_file.append('\t - Rows and columns must match the same size of other related raster maps;\n')
    lst_file.append('\t - CRS must be projected (coordinates in meters);\n')
    lst_file.append('\t - Grid cells must be squared;\n')


def append_fields(lst_fields):
    global df_keys, lst_file
    for f in lst_fields:
        df_lcl = df_keys.query('Name == "{}"'.format(f.strip()))
        s_field_dtype = df_lcl['Dtype'].values[0]
        s_field_descrp = df_lcl['Description'].values[0]
        s_field_units = df_lcl['Units'].values[0]
        s_aux = '\t - `{}` [{}]: {} [{}];\n'.format(f, s_field_dtype, s_field_descrp, s_field_units)
        lst_file.append(s_aux)


def append_fields_head(s_fields, s_msg):
    global lst_file
    if s_fields == 'none':
        pass
    else:
        lst_file.append(' - **{}**:\n'.format(s_msg))
        append_fields(lst_fields=s_fields.split('&'))


#to get the current working directory
directory = os.getcwd()
print(directory)
df_io = pd.read_csv('iofiles.csv', sep=';')

df_import = df_io.query('Source == "imported by user"')
df_output = df_import.query('Source == "process output"')
df_keys = pd.read_csv('keys.csv', sep=';')

s_dir_samples_url = 'https://github.com/ipo-exe/tklab/blob/main/samples'

lst_file = list()


# file index
s_file_url =  'https://github.com/ipo-exe/tklab/blob/main/iofiles.md'
lst_file.append(' - [Imported files]({}#imported-files)\n'.format(s_file_url))

lst_file.append('# Imported files')

for i in range(len(df_import)):
    s_filename = df_import['Name'].values[i]
    s_extension = df_import['Extension'].values[i]
    s_source = df_import['Source'].values[i]
    s_format = df_import['Format'].values[i]
    s_descrp = df_import['Description'].values[i]
    s_special = df_import['Special'].values[i]
    s_mand_fields = df_import['Mandatory Fields'].values[i]
    s_opti_fields = df_import['Optional Fields'].values[i]

    s_title = '## `{}.{}`'.format(s_filename, s_extension)
    lst_file.append('\n{}'.format(s_title))
    lst_file.append('\n')

    lst_file.append(' - **Source**: {};\n'.format(s_source))
    lst_file.append(' - **Format**: {};\n'.format(s_format))
    lst_file.append(' - **Description**: {};\n'.format(s_descrp))
    lst_file.append(' - **Requirements**:\n')

    if s_format == 'Data Table':
        basic_table()
        append_fields_head(s_fields=s_mand_fields, s_msg='Mandatory Fields')
        append_fields_head(s_fields=s_opti_fields, s_msg='Optional Fields')
    elif s_format == 'Time Series':
        basic_series()
        append_fields_head(s_fields=s_mand_fields, s_msg='Mandatory Fields')
        append_fields_head(s_fields=s_opti_fields, s_msg='Optional Fields')
    elif s_format == 'Raster Map':
        basic_map()
    if s_special == 'none':
        pass


    lst_file.append(' - **File sample**: [{}.{}]({}/{}.{});\n'.format(s_filename, s_extension,
                                                                      s_dir_samples_url, s_filename, s_extension))
    lst_file.append(' - **Formating example**:\n'.format(s_descrp))
    if s_format == 'Time Series' or s_format == 'Data Table':
        s_path = './samples/{}.{}'.format(s_filename, s_extension)
        try:
            df_sample = pd.read_csv(s_path, sep=';', dtype=str)
            # rename columns fields
            lst_aux = list()
            for j in range(len(df_sample.columns)):
                if j < len(df_sample.columns) - 1:
                    lst_aux.append(df_sample.columns[j] + ';')
                else:
                    lst_aux.append(df_sample.columns[j])
            df_sample.columns = lst_aux
            # rename column values
            for j in range(len(df_sample.columns)):
                s_col = df_sample.columns[j]
                if j < len(df_sample.columns) - 1:
                    df_sample[s_col] = df_sample[s_col] + ';'

            if s_format == 'Time Series':
                s_example = df_sample.head(7).to_string(index=False)
            else:
                s_example = df_sample.to_string(index=False)
            lst_file.append('```\n{}\n```'.format(s_example))
        except FileNotFoundError:
            pass

fle_md = open('iofiles.md', 'w')
fle_md.writelines(lst_file)
fle_md.close()