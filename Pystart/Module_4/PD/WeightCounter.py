# PD4 - Weight counter

# Write a program that will convert different units of mass to
# based on user selection. The user should be able to convert
# between kilograms, pounds and ounces.
# The conversion rate is 1 kilogram = 35.274 ounces and 1 kilogram = 2.20462 pounds

# Take numbers for operations from user
value = float(input("Give me value of mass you want to convert: "))

# List possible units of mass
print("kg - kilograms; ou - ounces; po - pounds")

# Take operation from user
operation = str(input("Give me unit of mass you gave me value in: "))

# Match case which perform math operations
match operation:
    case "kg":
        kilograms = value
        ounces = value * 35.274
        pounds = value * 2.20462
    case "ou":
        kilograms = value / 35.274
        ounces = value
        pounds = value * 2.20462 / 35.274
    case "po":
        kilograms = value / 2.20462
        ounces = value * 35.274 / 2.20462
        pounds = value
    case _:
        print("I think we don't have such unit of mass available..")
        quit()

# noinspection PyUnboundLocalVariable
# print results of conversion
print(f'Result of such conversion is: {kilograms:.3f} kilograms, {ounces:.3f} ounces and {pounds:.3f} pounds.')
