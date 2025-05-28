#Project 1
#PainterTool


## Importing packages
import math

## Variables definition
widths = []
heights = []
height_m_default = 2
painting_area_m2 = 0
area_per_liter_of_base_paint = 5
area_per_liter_of_paint = 13

## User defines number of walls
nr_of_walls = int(input("How many walls to paint? "))

## Info for user regarding variables definition
print("If you want to take recent value of wall height press 'Enter' button")

## Init iteration for first wall in order to define default height value
width_tmp = float(input(f'Insert wall no 1 width: '))
widths.append(width_tmp)
height_tmp = float(input(f'Insert wall no 1 height: '))
heights.append(height_tmp)
height_m_default = heights[0]

## Loop for User to define walls dimensions
for i in range(2,nr_of_walls + 1):
    width_tmp = float(input(f'Insert wall no {i} width: '))
    widths.append(width_tmp)
    height_tmp = input(f'Insert wall no {i} height: ')

### If condition to check if User would like to use default value for height
    if height_tmp == '':
        heights.append(height_m_default)
    else:
        heights.append(float(height_tmp))
        height_m_default = height_tmp

## Loop for calculating Painting area
for i in range(len(heights)):
    painting_area_m2 += heights[i] * widths[i]

print(widths)
print(heights)
print(f'Area to paint equals {painting_area_m2} m2.')

## User defines number of base paint layers
nr_of_base_paint_layers = int(input("Number of base paint layers: "))

## User defines number of base paint layers
nr_of_paint_layers = int(input("Number of paint layers: "))

## Final purchase value calculation
nr_of_base_paint_liters = math.ceil(nr_of_base_paint_layers * painting_area_m2/float(area_per_liter_of_base_paint))
nr_of_paint_liters = math.ceil(nr_of_paint_layers * painting_area_m2/float(area_per_liter_of_paint))

## Returning results
print(f'You require {nr_of_base_paint_liters} liters of base paint.')
print(f'You require {nr_of_paint_liters} liters of paint.')
