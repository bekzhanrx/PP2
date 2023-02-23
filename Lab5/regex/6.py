import re

s = input("Enter a string: ")
x = re.sub("[ ,.]", ':', s)
print(x)
