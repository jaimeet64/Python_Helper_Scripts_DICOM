import sys
import os
import numpy as np
import dicom
numitems = len(sys.argv) -1
padding = numitems / 2
width = 2560
height = 2560
for i in range(1, padding+1):
  path_dicom = sys.argv[i]
  path_soft = sys.argv[i+padding]
  path_soft_dicom = os.path.splitext(path_dicom)[0] + "_soft.dcm"

  print path_dicom
  print path_soft
  print path_soft_dicom
  ds = dicom.read_file(path_dicom)
  img = np.fromfile(path_soft, dtype=">i2").astype(float).reshape(width, height)
  data = ds.pixel_array
  print np.amin(img)
  print np.amax(img)
  img = img.astype("i2")
  ds.BitsStored = 16
  ds.HighBit = 16
  ds.PixelRepresentation = 0x0001
  data[0:width, 0:height] = img
  ds.PixelData = data.tostring()
  ds.save_as(path_soft_dicom)
