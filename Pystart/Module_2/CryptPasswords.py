password = str(input('Give me your password: '))

new_pass = password.replace('a', '@').replace('s','$')

print(new_pass)