import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url,names=['sepal length','sepal width','petal length','petal width','target'])
df.head()

from sklearn.preprocessing import StandardScaler
features = ['sepal length','sepal width','petal length','petal width']
x = df.loc[:,features].values
y = df.loc[:,['target']].values
x = StandardScaler().fit_transform(x)
