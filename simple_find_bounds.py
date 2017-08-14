import sys
import numpy as np

for i in range(1, len(sys.argv)):
    mini = sys.maxint
    maxi = -sys.maxint - 1
    data = np.fromfile(sys.argv[i], dtype=">i2")
    if np.amin(data) < mini:
        mini = np.amin(data)
    if np.amax(data) > maxi:
        maxi = np.amax(data)

    print("%s: %d - %d"%(sys.argv[i],maxi, mini))
