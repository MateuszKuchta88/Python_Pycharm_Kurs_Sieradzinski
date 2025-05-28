# This is script to check if number is palindromic one

number = int(input("Enter an integer you want to check if it's palindromic: "))
str_number = str(number)
number_length = len(str_number)
iter = int(number_length/2)
i = 0
while(i < iter):
    if(str_number[i] == str_number[number_length - 1 - i]):
        i += 1
        if(i + 1 == iter and iter % 2 == 0):
            print(f'{number} is palindromic number.')
        elif(i == iter and iter % 2 != 0):
            print(f'{number} is palindromic number.')
    else:
        print(f'{number} is not palindromic number.')
        i = iter