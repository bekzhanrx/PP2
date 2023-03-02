def file_length(fname):
    with open(fname, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print("Number of lines in the file: ", file_length('a.txt'))
