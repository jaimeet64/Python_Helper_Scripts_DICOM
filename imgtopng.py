import os
import sys
import numpy as np
import scipy.misc
w = int(sys.argv[1])
for i in range(2,len(sys.argv)):
    data = np.fromfile(sys.argv[i], dtype=">i2").reshape(w,w)
    #data[data < 0] = 0
    scipy.misc.imsave(os.path.splitext(sys.argv[i])[0]+".png", data)
    #filtered.tofile(os.path.splitext(sys.argv[i])[0]+"_bl0.8.img")
