import pandas as pd
#importing the os module
import os

#to get the current working directory
directory = os.getcwd()
print(directory)
df = pd.read_csv('iofiles.csv', sep=';')
print(df.to_string())
print(df.columns)



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
    lst_file.append(' - **Example**: {};\n'.format(s_descrp))


print(lst_file)
fle_md = open('iofiles.md', 'w')
fle_md.writelines(lst_file)
fle_md.close()