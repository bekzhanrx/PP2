def has_33(nums):
    for x in range(len(nums)):
        if nums[x] == 3:
            if (nums[x+1] == 3) and (len(nums) > x + 1):
                print('True')
                return 0
            else:
                print('False')
                return 0


l = []
n = int(input("Enter length: "))
for x in range(n):
    x = int(input())
    l.append(x)

has_33(l)
