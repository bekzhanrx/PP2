import random
name = input("Hello! What is your name?: ")
print('Well ', name, ' I am thinking of a number between 1 and 20.')
y = random.randint(1, 20)
count = 0
for i in range(20):
    x = int(input("Take a guess: "))
    count += 1
    if (x == y):
        print("Good job,", name, " You guessed my number in ", count, " guesses")
        break
    elif (x > y):
        print("Your guess is too high")
    else:
        print("Your guess is too low")
