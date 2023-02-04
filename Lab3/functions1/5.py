# Python3 program to print all permutations with
# duplicates allowed


def toString(List):
    return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.


def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            # backtrack


# Driver code
string = input("Enter any string: ")
n = len(string)
a = list(string)

# Function call
permute(a, 0, n)
