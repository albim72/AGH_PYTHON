import numpy as np

wprowadzenie do pakietu numpy....<br>
<img src="numpy.png" style="width:50%;">
<h4>kilka słów o tablicach pakietu NUMPY....

a = np.array([23,56,7,8,91,27,0,9,-7])
print(a)

mc = np.array([[4,6,1],[67,8,9],[-23,0,7]])
print(mc)


print(mc[0])

z = np.zeros(6)
print(z)

j = np.ones(8)
print(j)

e = np.empty(10)
print(e)

a = np.arange(7)
print(a)

a = np.arange(2,18,2)
print(a)

a = np.linspace(0,10,num=5)
print(a)

a = np.array([7,2,5,16,9,11,-5,0,123,-44,19])
print(np.sort(a))
