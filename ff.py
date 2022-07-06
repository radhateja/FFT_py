import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft,ifft

sr = 8000
ts = 1.0/sr
t = np.arange(0,10,ts)

freq = 40
x = 1*np.sin(2*np.pi*freq*t)

X = fft(x)
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T

#given input signal
plt.subplot(121)
plt.plot(t,x,'r')
plt.xlabel('time(sec)')
plt.ylabel('Amplitude')

#plt.figure(figsize = (12,6))
#fft output
plt.subplot(122)
plt.stem(freq,np.abs(X),'b',markerfmt=" ",basefmt="-b")

#plt.plot(T,X,'r')
plt.xlabel('freq(hz)')
plt.ylabel('fft amplitude(X(freq))')
plt.xlim(0,10)
plt.tight_layout()
plt.show()


