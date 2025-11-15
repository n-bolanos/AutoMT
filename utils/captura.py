import soundfile as sf
import sounddevice as sd

def leer_audio(path):
    """
    Esta función lee un audio que esté en el path indicado.
    Retorna una tupla (data, frecuencia_muestreo)
    """
    return sf.read(path)

def capturar_audio():
    """
    Esta función detecta el audio en vivo.
    """
    pass

def reproducir_audio(data, sr):
    sd.play(data, sr)
    sd.wait()
    return