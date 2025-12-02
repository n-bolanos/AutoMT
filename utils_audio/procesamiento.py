from numpy.fft import fft
from numpy import ndarray
import librosa
import numpy as np
import config

from .analisis_notas import f0_to_notes

def get_amplitudes(series:ndarray) -> ndarray:
    """
    This function returns the normalized array of amplitudes of a Fourier Transformed
    """
    return abs(fft(series)[:len(series)//2])/(len(series)//2)

def get_frequencies(window_size:int, samplerate:float) -> ndarray:
    """
    This function returns the array of frequencies according to the current analysis
    """
    return librosa.fft_frequencies(sr=samplerate, n_fft=window_size)

def get_samplerate(T:float, N:float) -> float:
    """
    Input:
        T-> Period
        N -> Number of harmonics
    """
    return 5*(1/T)*N

def dominant_frequencies(data: np.ndarray, sr: int):
    """
    This function returns the most energetic frequency value each 0.5 seconds frame.
    """
    n_samples = int(sr*config.FRAME_LENGTH)
    f0_list = []
    w_size = int(min(4096, n_samples//2))

    for i in range(0, len(data)+1, n_samples):
        segment = data[i:i+n_samples]
        if len(segment) == 0:
            continue

        S = np.abs(librosa.stft(segment, n_fft=w_size, hop_length=int(w_size/2), center=False))

        freqs = get_frequencies(w_size, sr)
        mag = np.mean(S, axis=1)

        idx = np.argmax(mag)
        f0_list.append(freqs[idx])

    return f0_list

def audio_to_notes(data, sr):
    f0 = dominant_frequencies(data, sr)
    notes = f0_to_notes(f0)
    return notes