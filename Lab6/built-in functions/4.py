from time import sleep
import math


def delay(ms, arg):
    sleep(ms / 1000)
    return math.sqrt(arg)


print("Square root after specific miliseconds:")
print(delay(2000, 25))
