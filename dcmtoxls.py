# -*- coding: utf-8 -*-
""" dcmtoxls.py
Outputs the information collected from the header of all listed dicom images
to an excel spreadsheet for convinient overview
Usage: python dcmtoxls.py [image1 ... imageN]

Parameters:
	- image1..imageN: a list of the paths to each dicom image to process
"""
from openpyxl import Workbook
import dicom
import sys
import os
import numpy as np
import math
wb = Workbook()
ws = wb.active
ws.append(["File name", "Case number", "Width", "Height", "Pixel Size", "kVp", "Exposure (mAs)", "Exposure time", "Resized pixel size", "Resized Width", "Resized Height"])
c = 1
lowest = 50000
for i in range(1, len(sys.argv)):
    head, tail = os.path.split(sys.argv[i])
    ds = dicom.read_file(sys.argv[i])
    recol = ds.Columns if ds.Columns < 2560 else 2560
    rerows = ds.Rows if ds.Rows < 2560 else 2560
    ws.append([tail, "%03d"%c, ds.Columns, ds.Rows, "%sx%s"%(ds.PixelSpacing[0], ds.PixelSpacing[1]), ds.KVP, ds.Exposure, ds.ExposureTime, "0.8", math.ceil(recol*0.18), math.ceil(rerows*0.18)])
    if ds.Columns < lowest:
        lowest = ds.Columns
    c+=1
    
wb.save("report.xlsx")