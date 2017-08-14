
import numpy as np
import sys
import pandas as pd
list_min=[]
for i in range(1,len(sys.argv)):
	data = np.fromfile(sys.argv[i], ">i2")
	list_min.append(np.min(data))

	
df = pd.DataFrame(list_min)
df.to_excel('output_min.xlsx', header=False, index=False)






