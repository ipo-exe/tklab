import pandas as pd
import inp
import os


def append_table(df):
    global lst_file

    def append_line(lst_items):
        s_main = ' | '.join(lst_items)
        lst_file.append('|{}|\n'.format(s_main))

    lst_headers = list(df.columns)
    append_line(lst_headers)
    append_line([':---'] * len(lst_headers))
    for i in range(len(df)):
        append_line(list(df.values[i]))


def append_basic_table_reqs():
    global lst_file
    lst_file.append('\t - Field separator: semicolon `;`;\n')
    lst_file.append('\t - Decimal separator: period `.`;\n')


def append_basic_series_reqs():
    global lst_file
    lst_file.append('\t - Field separator: semicolon `;`;\n')
    lst_file.append('\t - Decimal separator: period `.`;\n')
    lst_file.append('\t - Time resolution: daily timesteps;\n')
    lst_file.append('\t - Date format: `YYYY-MM-DD`;\n')


def append_basic_map_reqs():
    lst_file.append('\t - Void cells value: not allowed - all grid cells must be filled with data;\n')
    lst_file.append('\t - Rows and columns must match the same size of other related raster maps;\n')
    lst_file.append('\t - CRS must be projected (coordinates in meters);\n')
    lst_file.append('\t - Grid cells must be squared;\n')


def append_fields(lst_fields):
    global df_gloss, lst_file
    lst_lcl_field = list()
    lst_lcl_dtype = list()
    lst_lcl_descr = list()
    lst_lcl_units = list()
    for f in lst_fields:
        df_lcl = df_gloss.query('Name == "{}"'.format(f.strip()))
        lst_lcl_field.append('`{}`'.format(f))
        #s_field_dtype = df_lcl['Dtype'].values[0]
        lst_lcl_dtype.append(df_lcl['Dtype'].values[0])
        #s_field_descrp = df_lcl['Description'].values[0]
        lst_lcl_descr.append(df_lcl['Description'].values[0])
        #s_field_units = df_lcl['Units'].values[0]
        lst_lcl_units.append(df_lcl['Units'].values[0])
        #s_aux = '\t - `{}` [{}]: {} [{}];\n'.format(f, s_field_dtype, s_field_descrp, s_field_units)
        #lst_file.append(s_aux)
    df_lcl = pd.DataFrame({'Field Name': lst_lcl_field,
                           'Data Type': lst_lcl_dtype,
                           'Description': lst_lcl_descr,
                           'Units': lst_lcl_units})
    append_table(df=df_lcl)


def append_fields_head(s_fields, s_msg):
    global lst_file
    if s_fields == 'none':
        pass
    else:
        lst_file.append(' - **{}**:\n\n'.format(s_msg))
        append_fields(lst_fields=s_fields.split('&'))

#
lst_file = list()
s_dir_samples_url = 'https://github.com/ipo-exe/tklab/blob/main/samples'
s_file_url =  'https://github.com/ipo-exe/tklab/blob/main/iodocs.md'
# import
df_io = pd.read_csv('iofiles.csv', sep=';')
df_io['Source'] = df_io['Source'].str.strip()
df_io['File Name'] = df_io['Name'] + '.' + df_io['Extension']
df_io['File'] = '[' + df_io['File Name'] + '](' + s_file_url + '#' + df_io['Name'] + df_io['Extension'] + ')'

df_io['Sample_URL'] = s_dir_samples_url + '/' + df_io['File Name']
df_io['Sample'] = '[Sample file](' + s_dir_samples_url + '/' + df_io['File Name'] + ')'

df_import = df_io.query('Source == "imported by user"')
df_output = df_io.query('Source == "process output"')

lst_dfs = [df_import, df_output]
lst_heads = ['Imported files', 'Output files']
lst_links = ['imported-files', 'output-files']
lst_descr = ['These files must be prepared and sourced by the user. Samples are provided for proper formatting.',
             'These files are generated by the program. Note that the user may source it as input to other processes.']
lst_table = [['File', 'Source', 'Format', 'Sample'],
             ['File', 'Source', 'Format']]
df_gloss = pd.read_csv('glossary_plans.csv', sep=';')

lst_file.append('# I/O documentation\n')

for i in range(len(lst_heads)):
    lst_file.append(' - [{}]({}#{})\n'.format(lst_heads[i], s_file_url, lst_links[i]))
lst_file.append(' - [Glossary]({}#{})\n'.format(s_file_url, 'glossary'))
# files loop
for i in range(len(lst_dfs)):
    df = lst_dfs[i]
    print(df.to_string())
    lst_file.append('\n# {}\n'.format(lst_heads[i]))
    lst_file.append('{}\n\n'.format(lst_descr[i]))
    # table
    df_lcl = lst_dfs[i][lst_table[i]]
    append_table(df=df_lcl)

    for j in range(len(df)):
        # get local values
        s_filename = df['Name'].values[j]
        s_extension = df['Extension'].values[j]
        s_source = df['Source'].values[j]
        s_format = df['Format'].values[j]
        s_descrp = df['Description'].values[j]
        s_special = df['Special'].values[j]
        s_mand_fields = df['Mandatory Fields'].values[j]
        s_opti_fields = df['Optional Fields'].values[j]
        s_title = '## `{}.{}`'.format(s_filename, s_extension)

        # append to list
        lst_file.append('\n{}'.format(s_title))
        lst_file.append('\n')
        lst_file.append(' - **Description**: {};\n'.format(s_descrp))
        lst_file.append(' - **Source**: {};\n'.format(s_source))
        lst_file.append(' - **File sample**: [{}.{}]({}/{}.{});\n'.format(s_filename, s_extension,
                                                                          s_dir_samples_url, s_filename, s_extension))
        lst_file.append(' - **Format**: {};\n'.format(s_format))
        lst_file.append(' - **Formating example**:\n'.format(s_descrp))
        if s_format == 'Time Series' or s_format == 'Data Table':
            s_path = './samples/{}.{}'.format(s_filename, s_extension)
            try:
                df_sample = pd.read_csv(s_path, sep=';', dtype=str)
                # rename columns fields
                lst_aux = list()
                for k in range(len(df_sample.columns)):
                    if k < len(df_sample.columns) - 1:
                        lst_aux.append(df_sample.columns[k] + ';')
                    else:
                        lst_aux.append(df_sample.columns[k])
                df_sample.columns = lst_aux
                # rename column values
                for k in range(len(df_sample.columns)):
                    s_col = df_sample.columns[k]
                    if k < len(df_sample.columns) - 1:
                        df_sample[s_col] = df_sample[s_col] + ';'
                if s_format == 'Time Series':
                    s_example = df_sample.head(7).to_string(index=False)
                else:
                    s_example = df_sample.to_string(index=False)
                lst_file.append('```\n{}\n```\n'.format(s_example))
            except FileNotFoundError:
                pass

        lst_file.append(' - **Requirements**:\n')

        if s_format == 'Data Table':
            append_basic_table_reqs()
            append_fields_head(s_fields=s_mand_fields, s_msg='Mandatory Fields')
            append_fields_head(s_fields=s_opti_fields, s_msg='Optional Fields')
        elif s_format == 'Time Series':
            append_basic_series_reqs()
            append_fields_head(s_fields=s_mand_fields, s_msg='Mandatory Fields')
            append_fields_head(s_fields=s_opti_fields, s_msg='Optional Fields')
        elif s_format == 'Raster Map':
            append_basic_map_reqs()
        if s_special == 'none':
            pass

lst_file.append('\n## Glossary\n')

df_gloss['Keyword'] = '`' + df_gloss['Name'] + '`'
df_gloss['Data Type'] = df_gloss['Dtype']

lst_file.append('\n### By A-Z order\n')
df_gloss = df_gloss.sort_values(by='Name')
append_table(df=df_gloss[['Keyword', 'Data Type', 'Description', 'Units', 'Category']])
lst_file.append('\n### By category\n')
lst_cats = list(df_gloss['Category'].unique())
for cat in lst_cats:
    lst_file.append('\n#### {}\n'.format(cat.title()))
    df_lcl = df_gloss.query('Category == "{}"'.format(cat))
    df_lcl = df_lcl.sort_values(by='Name')
    append_table(df=df_lcl[['Keyword', 'Data Type', 'Description', 'Units', 'Category']])

fle_md = open('iodocs.md', 'w')
fle_md.writelines(lst_file)
fle_md.close()