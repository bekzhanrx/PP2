import re

string_to_match = input("Enter a string: ")

if re.search('a(b*)', string_to_match):
    print("Match found!")
else:
    print("No match found.")
