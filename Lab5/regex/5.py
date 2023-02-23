import re

s = input("Enter a string: ")
x = re.search('a.*b$', s)
if x:
    print("Match found!")
else:
    print("None")
