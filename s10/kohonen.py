import numpy as np
import pandas as p
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal length','sepal width','petal length','petal width','class']

ds = pd.read_csv(url,names=names)
