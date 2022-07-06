import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('rose.jpeg')

image = img[:, :,:3].mean(axis=2)

f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
ift = np.fft.ifft2(f)

magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(131)
plt.imshow(img, cmap = 'gray')
plt.title('Input Image')
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum')
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.imshow(abs(ift),cmap = 'gray')
plt.title('ifft')
plt.xticks([])
plt.yticks([])
plt.show()
