def histogram(lt):
    res = ''
    for i in lt:
        for j in range(i):
            res += '*'
        print(res)
        res = ''


l = []
n = int(input("Enter length: "))
for x in range(n):
    x = int(input())
    l.append(x)

histogram(l)
