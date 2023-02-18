def downer(n):
    while n >= 0:
        yield n
        n -= 1


x = int(input("Enter any integer: "))
for i in downer(x):
    print(i)
