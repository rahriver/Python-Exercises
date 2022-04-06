class Stringer:
    
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("String: ")

    def printString(self):
        print(self.string.upper())

str1 = Stringer()
str1.getString()
str1.printString()
