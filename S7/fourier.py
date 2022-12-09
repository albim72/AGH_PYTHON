import numpy as np
import matplotlib.pyplot as plt

samplingFrequency = 100
samplingInterval = 1/samplingFrequency

beginTime = 0
endTime = 10

#częstotliwości dwóch sygnałów: 4Hz, 7Hz
singnal1Frequency = 4
singnal2Frequency = 7

time = np.arange(beginTime,endTime,samplingInterval)

ampitude1 = np.sin(2*np.pi*singnal1Frequency*time)
ampitude2 = np.sin(2*np.pi*singnal2Frequency*time)

figure,axis = plt.subplots(4,1)
plt.subplots_adjust(hspace=1)

#reprezentacja 1 funkcji
axis[0].set_title("funkcja falowa o częstotliwości 4Hz")
axis[0].plot(time,ampitude1)
axis[0].set_xlabel('Czas')
axis[0].set_ylabel('Amplituda')

#reprezentacja 2 funkcji
axis[1].set_title("funkcja falowa o częstotliwości 7Hz")
axis[1].plot(time,ampitude2)
axis[1].set_xlabel('Czas')
axis[1].set_ylabel('Amplituda')

#złożenie funckji
amplitude = ampitude1 + ampitude2

#złożenie funkcji
axis[2].set_title("złożenie obu funkcji")
axis[2].plot(time,amplitude)
axis[2].set_xlabel('Czas')
axis[2].set_ylabel('Amplituda')

#transformacja Fuouriera
toCount = len(amplitude)
fourierTransform = np.fft.fft(amplitude)/toCount
fourierTransform = fourierTransform[range (int(len(amplitude)/2))]
values = np.arange(int(toCount/2))
timePeriod = toCount/samplingFrequency
frequencies = values/timePeriod

#reprezentacja funkcji amplitude (fft)
axis[3].set_title("Transformata Fouriera rozkładająca komponenty funckji aplitude")
axis[3].plot(frequencies,abs(fourierTransform))
axis[3].set_xlabel('częstotliwość')
axis[3].set_ylabel('Amplituda')

plt.show()

