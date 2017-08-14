import sys
import argparse
import numpy as np
from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_mse as compare_mse


parser = argparse.ArgumentParser(description='Calculate the SSIM value between two images in the masked area')
parser.add_argument("gold_standard", help="The gold standard image you want to compare against")
parser.add_argument("compare", help="The image you want to compare to the gold standard image")
parser.add_argument("mask", help="A mask image with pixel value > 0 in the areas where SSIM should be calculated")
parser.add_argument("-x", "--width", type=int, help="Specify the width of the images", default=440)
parser.add_argument("-y", "--height", type=int, help="Specify the height of the images", default=440)
parser.add_argument("-s", "--size", type=int, help="Specify the SSIM kernel size", default=7)
parser.add_argument("-t", "--type", help="Specify the type of data. EG >i2 for big endian 16bit int", default=">i2")
#parser.add_argument("-r", "--range", type=int, help="Specify the dynamic range of the images (specify -1 to use the images' complete dynamic range)", default=-1)
args = parser.parse_args()

data = np.fromfile(args.gold_standard, args.type).reshape(args.width,args.height).astype("f4")
datab = np.fromfile(args.compare, args.type).reshape(args.width,args.height).astype("f4")
datam = np.fromfile(args.mask, args.type).reshape(args.width,args.height).astype("f4")

cont = np.hstack((data, datab))
max = np.percentile(cont, 95)
min = np.percentile(cont, 5)
# maxa = np.percentile(data, 95)
# maxb = np.percentile(datab, 95)
# mina = np.percentile(data, 5)
# minb = np.percentile(datab, 5)

# data = (data - mina) / maxa
# datab = (datab - minb) / maxb
data = (data-min)/max
datab = (datab-min)/max
#maxi = data.max() > datab.max() ? data.max() : datab.max()
# if args.range == -1:
#     if data.max() > datab.max():
#         maxi = data.max()
#     else:
#         maxi = datab.max()

#     if data.min() < datab.min():
#         mini = data.min()
#     else:
#         mini = datab.min()
#mini = data.min() < datab.min() ? data.min() : datab.min()
# data = data + np.abs(np.amin(data))
# datab = datab + np.abs(np.amin(datab))
ssim_noise, mapss = ssim(data, datab, win_size=args.size, full=True)
# mse = compare_mse(data, datab)
# msf = mapss
# print msf.shape
# #msf = msf.astype("i2")
# msf = msf.byteswap()
# msf.tofile("map.dump")
mapss *= datam
masked = np.ma.masked_where(mapss == 0, mapss)
print np.mean(masked)
# print mse
