from utils.procesamiento import get_amplitudes, get_frequencies
import matplotlib.pyplot as plt
import numpy as np

def graf_transformada(amplitudes, frequencies):
    plt.stem(frequencies, amplitudes)
    plt.title("Análisis frecuencial")
    plt.xlabel("Frecuencias [Hz]")
    plt.ylabel("Amplitud")
    plt.show()

def graf_vs_time(amplitudes, min, max):
    plt.plot(amplitudes[min:max])
    plt.show()

def espectrograma(data, samplerate):
    window_size = 1024
    hop_size = 512

    spectrogram = []
    for start in range(0, len(data) - window_size, hop_size):
        segment = data[start:start+window_size] * np.hanning(window_size)
        amplitudes = get_amplitudes(segment)[:window_size//2]
        spectrogram.append(amplitudes)

    spectrogram = np.array(spectrogram).T
    frequencies = get_frequencies(window_size, samplerate)[:window_size//2]
    times = np.arange(spectrogram.shape[1]) * hop_size / samplerate

    # Plot
    plt.figure(figsize=(10, 5))
    plt.pcolormesh(times, frequencies, 20 * np.log10(spectrogram + 1e-10), cmap='inferno')
    plt.title("Espectrograma (FFT por ventanas)")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Frecuencia [Hz]")
    plt.colorbar(label="Magnitude [dB]")
    plt.show()