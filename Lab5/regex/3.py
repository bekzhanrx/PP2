import re

s = input("Enter a string: ")
x = re.findall("[a-z]+_[a-z]+", s)
print(x)
