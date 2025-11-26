import soundfile as sf
import sounddevice as sd
import numpy as np

def leer_audio(path):
    """
    Esta función lee un audio que esté en el path indicado.
    Retorna una tupla (data, frecuencia_muestreo)
    """
    data, sr = sf.read(path)
    
    if data.ndim == 2:   # stereo → mono
        data = np.mean(data, axis=1)

    return (data, sr)



def capturar_audio():
    """
    Esta función detecta el audio en vivo.
    """
    pass

def reproducir_audio(data, sr):
    sd.play(data, sr)
    sd.wait()
    return