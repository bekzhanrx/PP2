import re
text = input("Enter a string: ")
print(re.findall('[A-Z][a-z]*', text))
