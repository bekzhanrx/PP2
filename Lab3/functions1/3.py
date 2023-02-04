def solve(numheads, numlegs):
    for x in range(numheads):
        for y in range(numheads):
            if (x + y == numheads) and (2*x + 4*y == 94):
                print("Number of chickens: ", x)
                print("Number of rabbits: ", y)
                return 0


a = 35
b = 94
solve(a, b)
