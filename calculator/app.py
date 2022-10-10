# define the functions needed: add, sub, multiply, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit


def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
#add(5, 5)


def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))
# sub(10,5)


def multiply(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))
#multiply(4, 8)


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))
#div(60, 4)


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

choice = input("input your choice: ")

if choice == 'a' or choice == 'A':
    print("Addition")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    add(a, b)
elif choice == 'b' or choice == 'B':
    print("Subtraction")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    sub(a, b)
elif choice == 'c' or choice == 'C':
    print("Multiplication")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    multiply(a, b)
else:
    print("Division")
    a = int(input("input first number:"))
    b = int(input("input second number:"))
    div(a, b)
