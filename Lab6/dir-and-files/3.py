import os
print("Test a path exists or not:")
path = r'c:\\pp2\\Lab5\\row.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
