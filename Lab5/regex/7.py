def camel(d):
    x = d.split('_')
    for i in range(len(x)):
        x[i] = x[i].capitalize()
    return "".join(x)


s = input("Enter a string: ")
print(camel(s))
