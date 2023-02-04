def ulist(lt):
    new = []
    for x in lt:
        if x not in new:
            new.append(x)

    print(new)


l = []
n = int(input('Enter length: '))
for x in range(n):
    x = int(input())
    l.append(x)


ulist(l)
