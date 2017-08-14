import SimpleITK as sitk
import os
import sys
import numpy as np
from skimage.restoration import denoise_bilateral
color=float(sys.argv[1])
spatial=float(sys.argv[2])
w = int(sys.argv[3])
h = int(sys.argv[4])
for i in range(5,len(sys.argv)):
    data = np.fromfile(sys.argv[i], dtype=">i2").reshape(w,h).astype("f4")
    mini = np.amin(data)
    data += np.abs(mini)
    img = sitk.GetImageFromArray(data)
    filtered = sitk.Bilateral(img, color, spatial)
    filtereda = sitk.GetArrayFromImage(filtered).astype("i2").byteswap()
    #filtered = denoise_bilateral(data, sigma_color=color, sigma_spatial=spatial,multichannel=False).astype("i2").byteswap()
    filtereda.tofile("%s_blc%.2fs%1.0f.img"%(os.path.splitext(sys.argv[i])[0], color, spatial))
    print("%s_blc%.2fs%1.0f.img"%(os.path.splitext(sys.argv[i])[0], color, spatial))
