import threading
import os
from tkinter import messagebox
from tkinter import filedialog

import config
from utils_audio import captura, procesamiento
from codificacion import procesamiento as pr

audio_file = None
file_name = None

def wrap_text(text, max_chars_per_line=40):
    """
    Rompe el texto en varias líneas con salto de linea.
    Si una palabra es demasiado larga, la divide con un '-'.
    """
    words = text.replace("-", "- ").split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_chars_per_line:
            if current_line:
                current_line +=  word
            else:
                current_line = word
        else:
            while len(word) > max_chars_per_line:
                lines.append(word[:max_chars_per_line] + "-")
                word = word[max_chars_per_line:]
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return "\n".join(lines)

def cargar_audio(label_decode):
    global audio_file, file_name
    audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    file_name = os.path.basename(audio_file)
    label_decode.configure(text="")


def limpiar_audio():
    global audio_file, file_name
    audio_file = None
    file_name = None

def verificar_audio(label_widget, button_widget, decoding, encoding):
    global audio_file
    tmp = [None, ""]
    
    if audio_file in tmp:
        verificacion_msg = "No hay audio seleccionado."
        verificacion_fg = config.VERIFY_INCORR_COLOR
        button_widget.grid_remove()
        decoding[0].grid_remove()
        decoding[1].grid_remove()
        encoding[0].grid(row=4, column=4, pady=20, padx=30)
        encoding[1].grid(row=4, column=1, columnspan=3, pady=20, padx=30, sticky="we")
        encoding[2].grid(row=6, column=1, pady=0, sticky="s")
    else:
        verificacion_msg = f"Audio cargado ({file_name})"
        verificacion_fg = config.VERIFY_CORR_COLOR
        button_widget.grid(row=2, column=3, columnspan=2 ,pady=20, padx=30, sticky="we")
        decoding[0].grid(row=5, column=1, pady=20, padx=30)
        decoding[1].grid(row=5, column=2, columnspan=3, pady=20, padx=30, sticky="we")
        encoding[0].grid_remove()
        encoding[1].grid_remove()
        encoding[2].grid_remove()
    
    label_widget.configure(text=verificacion_msg, text_color=verificacion_fg)

    label_widget.after(200, lambda: verificar_audio(label_widget, button_widget, decoding, encoding))

def reproducir_audio():
    if audio_file:
        data, sr = captura.leer_audio(audio_file)
        captura.reproducir_audio(data, sr)
    else:
        messagebox.showinfo("Mensaje no encontrado", "No hay mensajes cargados")

def codificar_msg(mensaje:str):
    try:
        if not mensaje:
            messagebox.showerror("Error", "No hay mensaje.\nRecuerde que solo se permiten letras y guiones (-)")
            return
        ruta = filedialog.asksaveasfilename(
            defaultextension=".WAV",
            filetypes=[("Audio Files", "*.mp3 *.wav")],
            title="Guardar archivo como"
        )
        mensaje = mensaje.upper().strip()
        captura.construir_audio(mensaje, path=ruta)
        messagebox.showinfo("Codificación completa", "El mensaje fue codificado exitosamente")
    except:
        messagebox.showerror("Error", "El mensaje no fue codificado. Intentelo nuevamente.\nRecuerde que solo se permiten letras y el '-'")

def decodificar_msg(label_widget):
    def worker():
        data, sr = captura.leer_audio(audio_file)
        notas = procesamiento.audio_to_notes(data, sr)
        resultado = pr.decodificar(notas)
        resultado = wrap_text(resultado)
        label_widget.after(0, lambda: label_widget.configure(text=resultado))

    label_widget.configure(text="... decodificando, por favor espere ...")
    threading.Thread(target=worker).start()