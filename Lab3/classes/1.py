class Myclass:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter any str: ")

    def printString(self):
        print(self.str.upper())


x = Myclass()
x.getString()
x.printString()
