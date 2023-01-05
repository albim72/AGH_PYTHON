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

#obliczenie odległości euklidesowej pomiędzy wektorami x i w
def distance(w,x):
    r=0
    for i in range(len(w)):
        r = r + (w[i] - x[i])**2
    r = np.sqrt(r)
    return r

#funkcja znajdowania wektorów x najbliższym wektorom w:

def findclosest(W,x):
    wm = W[0]
    r = distance(wm,x)

    i=0
    i_n = i
    for w in W:
        if distance(w,x) < r:
            r = distance(w,x)
            wm = w
            i_n = i
        i = i + 1

    return (wm,i_n)

print(W)

la = 0.3 #współczynnik lamdba
dla = 0.05 #delta lambda

while la >=0:
    for k in range(10):
        for x in X:
            wm = findclosest(W,x)[0]
            for i in range(len(wm)):
                wm[i] = wm[i] + la*(x[i]-wm[i])

    la = la -dla

Data = list()

for i in range(len(W)):
    Data.append(list())

dfList = ds['class']

DS = list()
i=0
for x in X:
    i_n = findclosest(W,x)[1]
    Data[i_n].append(x)
    DS.append([i_n,dfList[i]])
    i = i+1

print(DS)
