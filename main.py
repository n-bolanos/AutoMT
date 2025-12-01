from utils_audio import captura, analisis_notas, procesamiento
from matplotlib.pyplot import show
from codificacion import procesamiento as pr
import config

while True:
    print("\n\n0 -> Salir\n1 -> Redactar mensaje.\n2 -> Descifrar mensaje\n3 -> Reproducir último mensaje guardado")
    eleccion = int(input("Elija: "))

    if eleccion == 0:
        break
    elif eleccion == 1:
        mensaje = input("Ingrese el mensaje que quiera enviar: ")
        captura.construir_audio(mensaje)
        print("\tMENSAJE CODIFICADO EXITOSAMENTE")

    elif eleccion == 2:
        path = r"output.wav"
        data, sr= captura.leer_audio(path)
        num_muestras = len(data)
        num_simbolos = num_muestras//(sr*config.FRAME_LENGTH)
        print("Cantidad de símbolos esperados: ", num_simbolos)

        notas = procesamiento.audio_to_notes(data, sr)
        print("\tMENSAJE DECODIFCADO: ", pr.decodificar(notas))
        
    elif eleccion == 3:
        path = r"output.wav"
        data, sr= captura.leer_audio(path)
        captura.reproducir_audio(data, sr)
    else:
        print("Opción no válida")
