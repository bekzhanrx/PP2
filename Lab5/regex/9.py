import re

s = input("Enter a string: ")
x = re.findall('[A-Z][a-z]*', s)
print(' '.join(x))
