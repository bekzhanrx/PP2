def snake(s):
    a = []
    for i in range(len(s)):
        if s[i].isupper():
            if i == 0:
                a.append(s[i].lower())
            else:
                a.append('_')
                a.append(s[i].lower())
        else:
            a.append(s[i])
    return ''.join(a)


x = input("Enter a string: ")
print(snake(x))
