from random import randint
import math

x = randint(1, 100)

print(f'X = {x}.\nPower({x}) = {x*x}.\nceil(sqrt({x})) = {math.ceil(math.sqrt(x))}.\nfloor(sqrt({x})) = '
      f'{math.floor(math.sqrt(x))}.')