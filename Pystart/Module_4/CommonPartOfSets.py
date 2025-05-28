# Find common part of sets

# Prepare a set of numbers divisible by 3 and a set of divisible numbers
# by 5, find the common part of both sets.

# Import libraries
from random import randint

# Declare empty set
divisible_by_3 = set()
divisible_by_5 = set()

# Declare while loops to randomly pick proper numbers for both sets
while len(divisible_by_3) < 12:
    random_number = randint(10, 99)
    if random_number % 3 == 0:
        divisible_by_3.add(random_number)
print(f'Random set of numbers divisible by 3: {sorted(divisible_by_3)}.')

while len(divisible_by_5) < 12:
    random_number = randint(10, 99)
    if random_number % 5 == 0:
        divisible_by_5.add(random_number)
print(f'Random set of numbers divisible by 5: {sorted(divisible_by_5)}.')

# Find common part of both sets
common_part = divisible_by_3 & divisible_by_5
print(f'Common part of both random sets is: {sorted(common_part)}.')
