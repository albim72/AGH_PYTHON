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
