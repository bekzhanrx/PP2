def spy_game(nums):
    n = len(nums)
    for x in range(n):
        if (nums[x] == 0):
            for y in range(x+1, n):
                if nums[y] == 7:
                    print('False')
                    return 0
                elif nums[y] == 0:
                    for z in range(y+1, n):
                        if nums[z] == 7:
                            print('True')
                            return 0


l = []
n = int(input("Length: "))
for x in range(n):
    x = int(input())
    l.append(x)

if l.index(7) < l.index(0):
    print('False')
else:
    spy_game(l)
