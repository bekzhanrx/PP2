def uplow(s):
    u = 0
    l = 0
    for i in range(len(s)):
        if s[i].isupper():
            u += 1
        elif s[i].islower():
            l += 1
    print("Number of upper case letters: ", u)
    print("Number of lower case letters: ", l)


uplow("It Was A Good Day")
