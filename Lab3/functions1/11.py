def ispalindrome(s):
    x = s
    x = x[::-1]
    if (x == s):
        print("It is a palindrome")
    else:
        print("It is not palindrome")


a = input("Enter any str: ")
ispalindrome(a)
