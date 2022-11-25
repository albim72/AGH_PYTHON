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

a = np.array([2,4,8,9])
b = np.array([1,6,11,34,67])

w = np.concatenate((a,b))
print(w)
print(np.sort(w))

x = np.array([[1,4],[7,8]])
y = np.array([[5,6],[3,9]])


u = np.concatenate((x,y),axis=0)
print(u)

a = np.arange(6)
print(a)

b= a.reshape(2,3)
print(b)

dane = np.arange(1,99,3)
print(dane)

print(dane[2:11])

print(dane[:6])

print(dane[-2])
print(dane[2:15:5])

m = np.array([[67,8,9,12],[2,3,5,8],[11,44,3,6]])
print(m)

print(m[m<9])

pc = (m>=10)
print(m[pc])

parzyste = m[m%2==0]
print(parzyste)

pc = (m >11) | (m==44)
print(pc)

a = np.array([1,2,3,4,8,9,12,16,20,25])
print(a)

aw = a[2:7]
print(aw)
print(type(a))
print(type(aw))

a1 = np.array([[1,1,2],[3,3,2],[4,7,1]])
a2 = np.array([[2,2,5],[7,7,2],[1,89,1]])
a3 = np.array([[5,5,1],[12,17,5],[8,1,1]])

ver = np.vstack((a1,a2,a3))
print(ver)
print("__________________")
hor = np.hstack((a1,a2,a3))
print(hor)
