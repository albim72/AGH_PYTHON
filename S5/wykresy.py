import matplotlib.pyplot as plt
import numpy as np

#przygotowanie danych
t = np.arange(0.0,2.0,0.01)
s = 1+np.sin(2*np.pi*t)

#tworzenie wykresu
fig,ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel='czas [s]', ylabel='napięcie prądu (mV)',title='wykres napięcia prądu w czasie t')
ax.grid()
fig.savefig("fala.png")
plt.show()



#multiple subplots
x1 = np.linspace(0.0,5.0)
y1 = np.cos(2*np.pi*x1)*np.exp(x1)

x2 = np.linspace(0.0,2.0)
y2 = np.cos(2*np.pi*x2)

fig,(ax1,ax2) = plt.subplots(2,1)
fig.suptitle('połączenie dwóch wykresów')

ax1.plot(x1,y1,'ro-')
ax.set_ylabel('wartość A')

ax2.plot(x2,y2,'.-')
ax.set_xlabel('czas [s]')
ax.set_ylabel('wartość B')
plt.show()

#multiple subplots
x1 = np.linspace(0.0,5.0)
y1 = np.cos(2*np.pi*x1)*np.exp(x1)

x2 = np.linspace(0.0,2.0)
y2 = np.cos(2*np.pi*x2)

fig,(ax1,ax2) = plt.subplots(2,1)
fig.suptitle('połączenie dwóch wykresów')

ax1.plot(x1,y1,'o-')
ax1.set_xlim(5,0)
ax.set_ylabel('wartość A')

ax2.plot(x2,y2,'.-')
ax.set_xlabel('czas [s]')
ax2.set_xlim(0.0,1.2)
ax2.set_ylim(0.0,1.1)
ax.set_ylabel('wartość B')
plt.show()
