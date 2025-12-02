import soundfile as sf
import sounddevice as sd
import numpy as np
import codificacion.procesamiento as pr
from utils_audio import analisis_notas as an
import config

def leer_audio(path, invertir=False):
    """
    Esta función lee un audio que esté en el path indicado.
    Retorna una tupla (data, frecuencia_muestreo)
    """
    data, sr = sf.read(path)

    if invertir:
        data = data[::-1]

    
    if data.ndim == 2:   # stereo → mono
        data = np.mean(data, axis=1)

    return (data, sr)



def construir_audio(mensaje, sr=48000, path="output.wav"):
    """
    Esta función toma un mensaje, lo codifica y construye un .wav
    """
    notas = pr.codificar(mensaje)

    audio = np.concatenate([an.notes_to_wave(n, duration=config.FRAME_LENGTH, sr=sr) for n in notas])
    sf.write(path, audio, sr)

def reproducir_audio(data, sr):
    sd.play(data, sr)
    sd.wait()
    return