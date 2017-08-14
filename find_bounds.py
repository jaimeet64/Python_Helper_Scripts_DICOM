# -*- coding: utf-8 -*-
""" find_bounds.py
Finds the minimum and maximum value of the specified images in the specified
masked areas.
Usage: python find_bounds.py [[image1 mask1] ... [imageN maskN]]

Parameters:
	- image1..imageN: a list of the paths to each image to process
    - mask1..maskN: a list of the corresponding masking images where 1 is
    masked and 0 is not masked
"""
import sys
import numpy as np

mini = sys.maxsize
maxi = -sys.maxsize - 1

for i in range(1, len(sys.argv), 2):
    data = np.fromfile(sys.argv[i], dtype=">i2")
    mask = np.fromfile(sys.argv[i+1], dtype=">i2")
    data = data*mask
    X = np.ma.masked_equal(data,0)
    if np.amin(data) < mini:
        mini = np.amin(data)
    if np.amax(data) > maxi:
        maxi = np.amax(data)

print("%d - %d"%(maxi, mini))
