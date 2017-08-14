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

def main():

	parser = OptionParser()
	parser.add_option("-p", "--prefix", dest="prefix", default="../img/pa007_",help="Input prefix", metavar="PREFIX")
	parser.add_option("-w", "--wavelet", dest="wavelet", default="db20",help="Input prefix", metavar="WAVELET")
	parser.add_option("-o", "--output", dest="output", default="../img/rec.img",help="Desired output image", metavar="OUTPUT")
        parser.add_option("-l", "--level", dest="level", default=4,help="Dec level", metavar="LEVEL")
        parser.add_option("-m", "--mode", dest="mode", default="zpd",help="Border mode", metavar="LEVEL")
	(options, args) = parser.parse_args()
	coeffs = []

        options.level  = int(options.level)

        for i in xrange(options.level, 0, -1):
                if i == options.level:
                        datall = numpy.fromfile(options.prefix+("_ll"*i)+".img", dtype='>i2')
                        datall = datall.reshape(-1, int(math.sqrt(datall.size)))
                        coeffs.append(datall)

                datalh = numpy.fromfile(options.prefix+("_ll"*(i-1))+"_lh.img", dtype='>i2')
                datahl = numpy.fromfile(options.prefix+("_ll"*(i-1))+"_hl.img", dtype='>i2')
                datahh = numpy.fromfile(options.prefix+("_ll"*(i-1))+"_hh.img", dtype='>i2')

                datalh = datalh.reshape(-1, int(math.sqrt(datalh.size)))
                datahl = datahl.reshape(-1, int(math.sqrt(datahl.size)))
                datahh = datahh.reshape(-1, int(math.sqrt(datahh.size)))
                details = (datalh, datahl, datahh)
                coeffs.append(details)

        noext = os.path.basename(options.prefix)
        original = pywt.waverec2(coeffs, options.wavelet, options.mode)
        original = original.astype(numpy.int16, copy=False)
        original = original.byteswap()
        original.tofile(options.output)

if __name__ == '__main__':
	main()
