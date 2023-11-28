#### Problem: Analyzing Signal Frequencies using the Discrete Fourier Transform
# Write a Python program to perform a Discrete Fourier Transform (DFT) on a
# simple signal and plot its frequency spectrum. #The signal can be a 
# combination of sine waves. Identify and correct any errors in the implementation.

import numpy as np
import matplotlib.pyplot as plt

def dft(signal):
    N = len(signal)
    frequencies = np.zeros(N//2 + 1, complex)

    for k in range(N//2 + 1):
        for n in range(N//2 + 1):
            frequencies[k] += signal[n] * np.exp(-1j * np.pi * k * n / N)  

    return frequencies

# Generating a signal
t = np.linspace(0, 1, 400)
signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 80 * t)

# DFT
frequencies = dft(signal)

# Plotting the spectrum
plt.plot(np.abs(frequencies))
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()
