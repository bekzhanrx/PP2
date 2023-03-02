import os
print('Exist:', os.access('c:\\pp2\\Lab5\\row.txt', os.F_OK))
print('Readable:', os.access(
    'c:\\Users\\Public\\c:\\pp2\\Lab5\\row.txt', os.R_OK))
print('Writable:', os.access(
    'c:\\Users\\Public\\c:\\pp2\\Lab5\\row.txt', os.W_OK))
print('Executable:', os.access(
    'c:\\Users\\Public\\c:\\pp2\\Lab5\\row.txt', os.X_OK))
