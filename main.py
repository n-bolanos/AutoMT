from utils import captura, graficas, procesamiento
from matplotlib.pyplot import show

#path = input("Path del audio a analizar: ")
path = r"audio\Grave.wav"
data, sr= captura.leer_audio(path)
print(len(data), sr , data.shape)

frecuencias = procesamiento.get_frequencies(len(data), sr)
amplitudes = procesamiento.get_amplitudes(data)

graficas.graf_vs_time(data, 0, len(data)-1)
#graficas.graf_transformada(amplitudes, frecuencias)
#graficas.espectrograma(data, sr)

print(procesamiento.audio_to_notes(data, sr))


show()

