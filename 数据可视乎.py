# -*- coding:utf-8 -*-
import  seaborn as sns
import pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt

data = pd.DataFrame(np.random.random((10,6)),columns = ["wahaha","CaptainAmercia","BlackWidow","thor","Hulk","hawkeye"])

print(data)

heatmap_plot = sns.heatmap(date,center=0,cmap='gist_ncar')

plt.show()