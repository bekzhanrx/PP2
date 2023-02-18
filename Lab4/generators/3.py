def div(n):
    for i in range(n):
        if (i % 3 == 0) and (i % 4 == 0):
            yield i


x = int(input("Enter any integer: "))
for i in div(x):
    print(i)
