import numpy as np
import matplotlib.pyplot as plt

a = [[255,255,255],[255,255,255]]
b = np.fft.fft2(a)

plt.imshow(abs(b))
plt.show()
