# This is script to process given 4 points on plane

import math

x1 = float(input('Input x coordinate of 1st point: '))
x2 = float(input('Input x coordinate of 2nd point: '))
y1 = float(input('Input y coordinate of 1st point: '))
y2 = float(input('Input y coordinate of 2nd point: '))

x_length = max(x1, x2) - min(x1, x2)
y_length = max(y1, y2) - min(y1, y2)
radius = math.sqrt(pow(x_length, 2) + pow(y_length, 2)) / 2
area = math.pi * pow(radius, 2)
area_rectangle = x_length * y_length
circuit_rectangle = 2 * x_length + 2 * y_length

x_mid_point = max(x1, x2) - x_length / 2
y_mid_point = max(y1, y2) - y_length / 2

print(f'Coordinates of middle point: (x,y) = ({x_mid_point}, {y_mid_point}).')
print(f'Radius of this circle equals {radius:.2f}.')
print(f'Area of this circle equals {area:.2f}.')
print(f'Area of this rectangle equals {area_rectangle:.2f}.')
print(f'Circuit of this rectangle equals {circuit_rectangle:.2f}.')




