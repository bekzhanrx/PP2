import re

s = input("Enter a string: ")
x = re.search('ab{2,3}', s)
if x:
    print("Match found! ")
else:
    print("None")
