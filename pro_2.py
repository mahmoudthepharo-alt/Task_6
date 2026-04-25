class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
i=int(input(" 1 for addition\n 2 for subtraction\n 3 for multiplication\n choose an operation: "))
if i == 1: 
    print("The sum is: ", Calculator().add(a, b))
elif i == 2:
    print("The difference is: ", Calculator().subtract(a, b))
elif i == 3:
    print("The product is: ", Calculator().multiply(a, b))