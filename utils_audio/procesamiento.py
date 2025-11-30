from numpy.fft import fft, fftfreq
from numpy import ndarray
import librosa
import numpy as np

from .analisis_notas import f0_to_notes, group_notes

def get_amplitudes(series:ndarray) -> ndarray:
    """
    This function returns the normalized array of amplitudes of a Fourier Transformed
    """
    return abs(fft(series)[:len(series)//2])/(len(series)//2)

def get_frequencies(size:int, samplerate:float) -> ndarray:
    """
    This function returns the array of frequencies according to the current analysis
    """
    return fftfreq(size, 1/samplerate)[:size//2]

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
    frame_length = sr//2
    hop_length = sr//4
    fmin = 27
    fmax = 4400

    data = librosa.util.normalize(data.astype(float))

    f0 = librosa.yin(
        data,
        fmin=fmin,
        fmax=fmax,
        sr=sr,
        frame_length=frame_length,
        hop_length=hop_length
    )

     # Voicing threshold: energy-based mask
    rms = librosa.feature.rms(y=data, frame_length=frame_length,
                              hop_length=hop_length, center=True)[0]
    thresh = np.percentile(rms, 80)
    voiced = rms > thresh               # boolean mask

    f0_voiced = f0.copy()
    f0_voiced[~voiced] = np.nan

    times = librosa.frames_to_time(
        np.arange(len(f0)),
        sr=sr,
        hop_length=hop_length,
    )

    return f0_voiced, times

def audio_to_notes(data, sr):
    f0, times = dominant_frequencies(data, sr)
    notes = f0_to_notes(f0, times)
    segments = group_notes(notes)
    return segments