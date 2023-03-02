def ispal(s):
    l = 0
    r = len(s) - 1
    while r >= l:
        if s[r] != s[l]:
            return False
        l += 1
        r -= 1
    return True


print(ispal('azat'))
