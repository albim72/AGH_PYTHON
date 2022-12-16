import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url,names=['sepal length','sepal width','petal length','petal width','target'])
df.head()
