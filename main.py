import customtkinter as ctk
import threading
from tkinter import messagebox
from tkinter import filedialog
import config
from config import TITLE_FONT_PARAMS, FONT_PARAMS, BUTTON_FONT_PARAMS
from utils_audio import captura, procesamiento
from codificacion import procesamiento as pr

audio_file = None

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

def cargar_audio():
    global audio_file
    audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])

def limpiar_audio():
    global audio_file
    audio_file = None

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
    else:
        verificacion_msg = "Audio cargado."
        verificacion_fg = config.VERIFY_CORR_COLOR
        button_widget.grid(row=2, column=3, columnspan=2 ,pady=20, padx=30, sticky="we")
        decoding[0].grid(row=5, column=1, pady=20, padx=30)
        decoding[1].grid(row=5, column=2, columnspan=3, pady=20, padx=30, sticky="we")
        encode[0].grid_remove()
        encode[1].grid_remove()
    
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
        root.focus()
    except:
        messagebox.showerror("Error", "El mensaje no fue codificado. Intentelo nuevamente.\nRecuerde que solo se permiten letras y el '-'")
        root.focus()

def decodificar_msg(label_widget):
    def worker():
        data, sr = captura.leer_audio(audio_file)
        notas = procesamiento.audio_to_notes(data, sr)
        resultado = pr.decodificar(notas)
        resultado = wrap_text(resultado)
        label_widget.after(0, lambda: label_widget.configure(text=resultado))

    label_widget.configure(text="... decodificando, por favor espere ...")
    threading.Thread(target=worker).start()

class CustomButton(ctk.CTkButton):
    def __init__(self, master, text, command, ancho, esquina=0):
        super().__init__(
            master,
            text=text,
            command=command,
            font=BUTTON_FONT,
            text_color=config.BUTTON_FG_COLOR,
            fg_color=config.BUTTON_BG_COLOR,
            bg_color=config.BG_COLOR,
            hover_color=config.BUTTON_HOVER_COLOR,
            corner_radius=config.BUTTON_RADIUS,
            width=ancho,
        )

root = ctk.CTk()
root.title("Codificador Musical")
root.geometry("1000x450")
root.config(bg=config.BG_COLOR)
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(5, weight=2)
for col in range(1, 5):  # columns 1 to 4
    root.grid_columnconfigure(col, weight=1)

TITLE_FONT = ctk.CTkFont(**TITLE_FONT_PARAMS) # type: ignore
FONT = ctk.CTkFont(**FONT_PARAMS) # type: ignore
BUTTON_FONT = ctk.CTkFont(**BUTTON_FONT_PARAMS) # type: ignore


titulo = ctk.CTkLabel(root, text="Codificador Musical", 
                      font=TITLE_FONT, 
                      text_color=config.TITLE_COLOR,
                      bg_color=config.BG_COLOR, padx= 10)

icono_archivo = ctk.CTkLabel(root, text="Estado:  ", 
                             font=FONT, bg_color=config.BG2_COLOR)

label_archivo = ctk.CTkLabel(root, font=BUTTON_FONT, bg_color=config.BG2_COLOR)

btn_reproducir = CustomButton(root, text="Reproducir mensaje", command=reproducir_audio, ancho=100)

btn_cargar = CustomButton(root, text="Cargar audio", command=cargar_audio, ancho=200)

btn_limpiar = CustomButton(root, text="Limpiar selección", command=limpiar_audio, ancho=200)

mensaje_entry = ctk.CTkEntry(root, placeholder_text="Ingrese el mensaje a codificar",
                             placeholder_text_color=config.BG_COLOR,
                             font=FONT,
                             text_color=config.FONT_COLOR,
                             bg_color=config.BG_COLOR,
                             fg_color=config.BG_MSG)

btn_codifcar = CustomButton(root, text="Codificar y descargar", command=lambda: codificar_msg(mensaje_entry.get()), ancho=100)

label_decodificar = ctk.CTkLabel(root, text="", font=FONT, bg_color=config.BG_MSG, text_color=config.FONT_COLOR)

btn_decodifcar = CustomButton(root, text="Decodificar", command=lambda: decodificar_msg(label_decodificar), ancho=100)

titulo.grid(row=1, column=1, pady=10, columnspan=4, sticky="we")
icono_archivo.grid(row=2, column=1,pady=20, sticky="e")
label_archivo.grid(row=2, column=2,pady=20, sticky="w")
btn_reproducir.grid(row=2, column=3, columnspan=2 ,pady=20, padx=30, sticky="e")
btn_cargar.grid(row=3, column=1, columnspan=2,pady=20, padx=30,)
btn_limpiar.grid(row=3, column=3,columnspan=2, pady=20, padx=30,)
mensaje_entry.grid(row=4, column=1, columnspan=3, pady=20, padx=30, sticky="we")
btn_codifcar.grid(row=4, column=4, pady=20, padx=30)
btn_decodifcar.grid(row=5, column=1, pady=20, padx=30)
label_decodificar.grid(row=5, column=2, columnspan=3, pady=20, padx=30, sticky="we")

decode = [btn_decodifcar, label_decodificar]
encode = [btn_codifcar, mensaje_entry]

root.after(10, lambda: verificar_audio(label_archivo, btn_reproducir, decode, encode))
root.mainloop()