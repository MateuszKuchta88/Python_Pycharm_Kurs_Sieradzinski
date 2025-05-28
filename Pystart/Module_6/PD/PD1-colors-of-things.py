# PD6 1 - Print color of things

# TASK DESCRIPTION
# Prepare a function that will receive arguments in the form:
# group_them(wall=”red”, tomato=”red”, light=”yellow”, lemon=”yellow”, grass=”green”)
# In response, the function should display (in separate lines)
# Wall is red \n Tomato is red \n Light is yellow etc.
# Remember about testing!

# Import libraries


# Declare function
def group_them(**kwargs) -> str:
    output = ''
    for kwarg, value in kwargs.items():
        value = 'colorless' if value == '' else value
        output += kwarg.capitalize() + ' is ' + value.lower() + ' \n '
    return output.rstrip()


# Prepare tests
def test_group_them():
    assert group_them(wall="red", tomato="red", light="yellow", lemon="yellow", grass="green") == "Wall is red \n Tomato is red \n Light is yellow \n Lemon is yellow \n Grass is green"
    assert group_them() == ""
    assert group_them(light="yeLLow", lemon="yellow") == "Light is yellow \n Lemon is yellow"
    assert group_them(CAR="white", lemon="") == "Car is white \n Lemon is colorless"


# Print output message
# print(group_them(light="yeLLow"))
