
import numpy as np
import sys
import pandas as pd
list_max=[]
for i in range(1,len(sys.argv)):
	data = np.fromfile(sys.argv[i], ">i2")
	list_max.append(np.max(data))

	
df = pd.DataFrame(list_max)
df.to_excel('output_max.xlsx', header=False, index=False)






