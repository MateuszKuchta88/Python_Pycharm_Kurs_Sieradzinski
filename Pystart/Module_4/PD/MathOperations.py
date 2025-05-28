# PD4 - Mathematical operations

# Write a program that will perform various mathematical operations
# depending on the user's choice. The user should be able to choose
# between addition, subtraction, multiplication and division.

# Take numbers for operations from user
num1 = int(input("Give me 1st number: "))
num2 = int(input("Give me 2nd number: "))

# List possible operations
print("add-addition; sub-subtraction; mul-multiplication; div-division")

# Take operation from user
operation = str(input("Give me operation you want to perform: "))

# Match case which perform math operations
match operation:
    case "add":
        result = num1 + num2
    case "sub":
        result = num1 - num2
    case "mul":
        result = num1 * num2
    case "div":
        result = num1 / num2
    case _:
        print("I think operation is not correct.")
        quit()

print(f'Result of such operation is: {result}')
