import soundfile as sf
import sounddevice as sd


# Puede funcionar si tienes las bibliotecas correctas
data, samplerate = sf.read('audio/Acorde DoMiSol.wav')
print(data, samplerate)
sd.play(data, samplerate)
sd.wait()
