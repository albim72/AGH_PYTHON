import numpy as np
import pandas as p
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal length','sepal width','petal length','petal width','class']

ds = pd.read_csv(url,names=names)

print(ds.head())

#normalizacja danych
list_sl = []
list_sw = []
list_pl = []
list_pw = []

for sl in ds['sepal length']:
    sl = (sl-min(ds['sepal length']))/(max(ds['sepal length'])-min(ds['sepal length']))
    list_sl.append(sl)

for sw in ds['sepal width']:
    sw = (sw-min(ds['sepal width']))/(max(ds['sepal width'])-min(ds['sepal width']))
    list_sw.append(sw)

for pl in ds['petal length']:
    pl = (pl - min(ds['petal length'])) / (max(ds['petal length']) - min(ds['petal length']))
    list_pl.append(pl)

for pw in ds['petal width']:
    pw = (pw - min(ds['petal width'])) / (max(ds['petal width']) - min(ds['petal width']))
    list_pw.append(pw)

X = np.array(list(zip(list_sl,list_sw,list_pl,list_pw)))

#inicjacja zestawu wartości opsujących sieć

nc = 3 #liczba klas (gatunków irysów)
W = [] #lista wektorów w
M = len(X) #liczba wektorów x
N = len(X[0]) #rozmiar wektorów x


def get_weights():
    y = np.random.random()*(2.0/np.sqrt(M))
    return 0.5-(1/np.sqrt(M))+y

for i in range(nc):
    W.append(list())
    for j in range(N):
        W[i].append(get_weights()*0.5)
