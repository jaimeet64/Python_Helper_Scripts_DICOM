# -*- coding: utf-8 -*-

import pywt
import numpy
import struct
import sys
import os
import math
import timeit
import shutil
from optparse import OptionParser

def dec_and_save(path, wty, lvl, out_dir, border, sx, sy):
        """ Take an image and decompose it using a wavelet decomposition
        Parameters
        ----------
        path : str
               The path of the image, including the image name
        wty : str
              The short name of the image, chosen from the ones at http://wavelets.pybytes.com/
        lvl : int
              The level of decomposition to be used. The width of the image divided by the level must yield an integer result
        out_dir : str
                  the output directory where all the component images will be written
        border : str
                 The short name of the border distortion handling technique to be used in the decomposition. Can be per, sym, zpd
        """
	noext = os.path.split(os.path.splitext(path)[0])[1] # Get the name of the input image without the full path or the extension
	data = numpy.fromfile(path,dtype='>i2')[0:1760*1760] # Read the binary data from the image
	try:
		data = data.reshape(sx, sy) # Reshape the data from a 1-D array to a 2-D array (matrix)
		coeffs = pywt.wavedec2(data, wty, border, lvl) # Decompose the image using the provided parameters for level, etc
		for i in xrange(0,len(coeffs)): # coeffs is a multi level nested tuple. Extracting the data
			if i == 0: # The first element of the first level of tuple is the average coefficients
				cA = coeffs[i]
				icA = cA.astype(numpy.int16, copy=False)
				ocA = icA.byteswap()
				ocA.tofile(out_dir+noext+'_'+wty+('_ll'*lvl)+'.img') # Save the coefficients to the planned output file
				print ocA.shape
			else: # The other levels of nested tuples are a tuple containing the detail coefficients for this level, save them to their corresponding files
				(cH, cV, cD) = coeffs[i]
				icH = cH.astype(numpy.int16, copy=False)
				ocH = icH.byteswap()
				ocH.tofile(out_dir+noext+'_'+wty+('_ll'*(lvl-i))+'_lh'+'.img')
				icV = cV.astype(numpy.int16, copy=False)
				ocV = icV.byteswap()
				ocV.tofile(out_dir+noext+'_'+wty+('_ll'*(lvl-i))+'_hl'+'.img')
				icD = cD.astype(numpy.int16, copy=False)
				ocD = icD.byteswap()
				ocD.tofile(out_dir+noext+'_'+wty+('_ll'*(lvl-i))+'_hh'+'.img')
				print ocD.shape
	except ValueError as e:
		print e
	except:
		print("Error when opening the file or decomposing it")
		print sys.exc_info()[0]
def main():
	wt = sys.argv[1]
	level = int(sys.argv[2])
	border = sys.argv[3]
	sx = int(sys.argv[4])
	sy = int(sys.argv[5])
	for x in xrange(6,len(sys.argv)):
		dec_and_save(sys.argv[x], wt, level, './', border, sx, sy)

if __name__ == '__main__':
	main()
