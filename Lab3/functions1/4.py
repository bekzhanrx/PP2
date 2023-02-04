import math


def filter_prime(a):
    primelist = []
    m = 1
    for x in a:
        if (x == 1):
            continue
        for y in range(2, x):
            if x % y == 0:
                m = 0
                break
        if m == 1:
            primelist.append(x)
        else:
            m = 1
    for t in primelist:
        print(t)


l = []
n = int(input("Enter the size of list: "))
for z in range(n):
    z = int(input())
    l.append(z)

print("---------------------------")
filter_prime(l)
