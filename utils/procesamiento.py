from numpy.fft import fft, fftfreq
from numpy import ndarray

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