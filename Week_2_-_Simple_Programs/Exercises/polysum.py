# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 06:23:45 2020

@author: Zamberlam
"""

# A regular polygon has n number of sides. Each side has length s.

#     The area of a regular polygon is: 0.25∗n∗s**2/tan(π/n)
#     The perimeter of a polygon is: length of the boundary of the polygon

# Write a function called polysum that takes 2 arguments, n and s. This 
# function should sum the area and square of the perimeter of the regular 
# polygon. The function returns the sum, rounded to 4 decimal places.

def polysum(n, s):
    '''    
    Parameters
    ----------
    n : int
        number of sides of a regular polygon.
    s : int
        length of side.

    Returns
    -------
    sum of area and square of the perimeter of a regular polygon, 
    rounded to 4 decimal places.
    '''
    
    def polygonAreaPerimeter(n, s):
        '''
        Parameters
        ----------
        n : int
            number of sides of a regular polygon.
        s : int
            length of side.

        Returns
        -------
        area : int or float
            area of a regular polygon.
        perimeter : int or float
            perimeter of a regular polygon.
        '''
        from math import tan, pi
    
        area = (0.25*n*s**2) / (tan(pi/n))
        perimeter = s * n
        return area, perimeter
    
    area, perimeter = polygonAreaPerimeter(n, s)
    
    return round(area + perimeter ** 2, 4)

print(polysum(26, 4))