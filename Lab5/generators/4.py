def squares(a, b):
    for i in range(a, b+1):
        yield i*i


a = int(input("Enter start point: "))
b = int(input("Enter end point: "))
for z in squares(a, b):
    print(z)
