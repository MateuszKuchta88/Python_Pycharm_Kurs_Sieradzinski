# PD4 - Temperature in cities

# Write a program that will execute a while loop that will ask questions
# user with the name of the city and the temperature in degrees Celsius. There will be a program
# stored this information in a dictionary, where the key would be the city name and the value
# temperature. The loop will continue until the user enters "end".
# After completing the loop, the program should display the average temperature for all cities
# and the name of the city with the highest and lowest temperature.

# Import libraries

# Declare dictionary
cities = {}

# Welcome message
print('Welcome in "Temperature in cities" app.')

# While loop for operations
print('If you want to finish introducing new cities and their temperatures write "end" instead of city name.')
while 0 == 0:
    city = str(input("Give me city: "))
    if city == "end":
        break
    temperature = float(input('Give me temperature (in Celsius) from this city: '))
    cities.update({city: temperature})

# Initiate variables
max_temp = -1000
min_temp = 1000
max_temp_city = None
min_temp_city = None
for c, t in cities.items():
    if t > max_temp:
        max_temp_city = c
        max_temp = t
    if t < min_temp:
        min_temp_city = c
        min_temp = t

# print goodbye message
print(f'Average temperature for all cities: {(sum(cities.values())/len(cities.values())):.1f} Celsius')
print(f'City with highest temperature is {max_temp_city}. That temperature is {cities[max_temp_city]} Celsius.')
print(f'City with lowest temperature is {min_temp_city}. That temperature is {cities[min_temp_city]} Celsius.')
