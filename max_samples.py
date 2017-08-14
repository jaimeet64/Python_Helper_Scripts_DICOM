import numpy as np
import sys

for i in range(1,len(sys.argv)):
	data = np.fromfile(sys.argv[i], ">i2")
	print(sys.argv[i]+": "+str(np.count_nonzero(data)))
