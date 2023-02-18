from math import tan, pi
sides = int(input("Enter number of sides: "))
length = int(input("Enter length of a side: "))
area = int(sides * (length**2) / (4 * tan(pi / sides)))
print("The area of the polygon is: ", area)
