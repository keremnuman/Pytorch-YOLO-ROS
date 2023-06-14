import numpy as np
import matplotlib.pyplot as plt

# Genlik ve faz değerleri
amplitudes = [3, 2, 4, 1]
frequencies = [0, 0.1, 0.2, 0.25]
phases = [0, 0, -np.pi/2, np.pi]

# Genlik spektrumu
plt.stem(frequencies, amplitudes)
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.title('Genlik Spektrumu')
plt.grid(True)
plt.show()

# Faz spektrumu
plt.stem(frequencies, phases)
plt.xlabel('Frekans (Hz)')
plt.ylabel('Faz (radyan)')
plt.title('Faz Spektrumu')
plt.grid(True)
plt.show()
