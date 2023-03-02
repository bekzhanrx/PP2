fruits = ['apple', 'cherry', 'banana']
with open('a.txt', 'a') as a:
    for i in fruits:
        a.write("\n")
        a.write(i)
text = open('a.txt')
print(text.read())
