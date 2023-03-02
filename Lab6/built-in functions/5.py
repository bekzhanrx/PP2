def tupletrue(t):
    for x in t:
        if bool(x) == False:
            return False
    return True


print(tupletrue((1, 2, [1, 2], {}, (3, 4))))
