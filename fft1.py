from numpy import fft
import numpy as np
import matplotlib.pyplot as plt

fs = 80000
ts = 1/fs

f1 = 4000

N=int((fs/f1))
t = np.linspace(0,(N-1)*ts,N)
fstep = fs/N
f = np.linspace(0,(N-1),N)

Y=1*np.sin(2*np.pi*f1*t)

X=np.fft.fft(Y)

X_mag=np.abs(X)/N
f_plot=f[0:int(N/2+1)]
X_mag_plot=2*X_mag[0:int(N/2+1)]

fig,[ax1,ax2] = plt.subplots(nrows=2,ncols=1)

ax1.plot(t,Y,'.-')
ax2.plot(f_plot,X_mag_plot,'.-')

plt.show()
