# PD5 6 - Length based on XY points

# TASK DESCRIPTION
# Prepare a function that will receive two points in the form of tuples (x, y). The result
# should be the length of the segment created by combining these two
# points.

# Import libraries
from math import pow, sqrt

# Testing data
g_point1 = (1, 0)
g_point2 = (3, 2)

# Declare variables


# Declare function
def xy_points_length(p1: tuple, p2: tuple) -> float:
    """
    Function takes two points with XY coordinates and returns length of line joining those points
    :param p1: XY coordinates of first point
    :param p2: XY coordinates of second point
    :return: Length of line joining two given points
    """
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


# Process

# Print output message
print(f'Answer is {xy_points_length(g_point1, g_point2):.3f}')
