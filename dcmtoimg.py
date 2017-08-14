# -*- coding: utf-8 -*-
""" dcmtoimg.py
Takes a list of images in dicom format and saves them as raw signed 
16 bit big endian integer files. Files may be cropped if the original
dimensions exceed width or height.
Non compliant images (eg. too small) will be saved under another name
eg. pa001_test.img
Usage: python dcmtoimg.py width height [image1 ... imageN]

Parameters:
	- width: the width at wich the output will be cropped
	- height: the height at wich the output will be cropped
	- image1..imageN: a list of the paths to each dicom image to process
"""
import sys
import os
import numpy as np
import dicom
from scipy.ndimage.interpolation import zoom
c = 1 
d = 1
w = int(sys.argv[1])
h = int(sys.argv[2])
for i in range(3, len(sys.argv)):
    base = os.path.splitext(sys.argv[i])[0]
    head, tail = os.path.split(sys.argv[i])
    ds = dicom.read_file(sys.argv[i])
    data = ds.pixel_array
    print data.shape
    croped = data[0:w,0:h]
    print croped.shape
    zoomed = zoom(croped, 0.18, order=1, prefilter=False)
    print zoomed.shape
    maxi = np.amax(zoomed)
    mini = np.amin(zoomed)
    zoomed = -zoomed + np.abs(maxi) + np.abs(mini)
    if zoomed.shape[0] == zoomed.shape[1]:
        out = "%spa%03d.img"%(head, c)
        c +=1
    else:
        out = "%spa_test%03d.img"%(head, d)
        d += 1
    zoomed.astype("i2").byteswap().tofile(out)
    print out
