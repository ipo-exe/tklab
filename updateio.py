import pandas as pd
import inp
import os

#to get the current working directory
directory = os.getcwd()
print(directory)
df = pd.read_csv('iofiles.csv', sep=';')
print(df.to_string())
print(df.columns)

s_samples_url = 'https://github.com/ipo-exe/tklab/blob/main/samples'

lst_file = list()

for i in range(len(df)):
    s_filename = df['Name'].values[i]
    s_extension = df['Extension'].values[i]
    s_source = df['Source'].values[i]
    s_format = df['Format'].values[i]
    s_descrp = df['Description'].values[i]

    s_title = '## `{}.{}`'.format(s_filename, s_extension)
    lst_file.append('\n{}'.format(s_title))
    lst_file.append('\n')
    lst_file.append(' - **Source**: {};\n'.format(s_source))
    lst_file.append(' - **Format**: {};\n'.format(s_format))
    lst_file.append(' - **Description**: {};\n'.format(s_descrp))
    lst_file.append(' - **Requirements**: {};\n'.format(s_descrp))
    s_lcl_line = df['Requirements'].values[i]
    lst_file.append(' - **File sample**: [{}.{}]({}/{}.{});\n'.format(s_filename, s_extension,
                                                                    s_samples_url, s_filename, s_extension))
    lst_file.append(' - **Formating example**:\n'.format(s_descrp))
    if s_format == 'Time Series' or s_format == 'Data Table':
        s_path = './samples/{}.{}'.format(s_filename, s_extension)
        try:
            df_sample = pd.read_csv(s_path, sep=';', dtype=str)
            print(df_sample.columns)
            # rename columns fields
            lst_aux = list()
            for i in range(len(df_sample.columns)):
                if i < len(df_sample.columns) - 1:
                    lst_aux.append(df_sample.columns[i] + ';')
                else:
                    lst_aux.append(df_sample.columns[i])
            df_sample.columns = lst_aux
            # rename column values
            for i in range(len(df_sample.columns)):
                s_col = df_sample.columns[i]
                if i < len(df_sample.columns) - 1:
                    df_sample[s_col] = df_sample[s_col] + ';'

            if s_format == 'Time Series':
                s_example = df_sample.head(7).to_string(index=False)
            else:
                s_example = df_sample.to_string(index=False)
                print(s_example.split('\n'))
            print(s_example)
            lst_file.append('```\n{}\n```'.format(s_example))
        except FileNotFoundError:
            print('file not found')


fle_md = open('iofiles.md', 'w')
fle_md.writelines(lst_file)
fle_md.close()