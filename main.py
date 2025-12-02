import customtkinter as ctk
import config
from config import TITLE_FONT_PARAMS, FONT_PARAMS, BUTTON_FONT_PARAMS, INFO_FONT_PARAMS
from front_utils import *

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
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(5, weight=2)
for col in range(1, 5):  # columns 1 to 4
    root.grid_columnconfigure(col, weight=1)

TITLE_FONT = ctk.CTkFont(**TITLE_FONT_PARAMS) # type: ignore
FONT = ctk.CTkFont(**FONT_PARAMS) # type: ignore
BUTTON_FONT = ctk.CTkFont(**BUTTON_FONT_PARAMS) # type: ignore
INFO_FONT = ctk.CTkFont(**INFO_FONT_PARAMS) # type: ignore


titulo = ctk.CTkLabel(root, text="Codificador Musical", 
                      font=TITLE_FONT, 
                      text_color=config.TITLE_COLOR,
                      bg_color=config.BG_COLOR, padx= 10)

icono_archivo = ctk.CTkLabel(root, text="Estado:  ", 
                             font=FONT, bg_color=config.BG2_COLOR)

label_archivo = ctk.CTkLabel(root, font=BUTTON_FONT, bg_color=config.BG2_COLOR)

btn_reproducir = CustomButton(root, text="Reproducir mensaje", command=reproducir_audio, ancho=100)

btn_cargar = CustomButton(root, text="Cargar audio", command=lambda: cargar_audio(label_decodificar), ancho=200)

btn_limpiar = CustomButton(root, text="Limpiar selección", command=limpiar_audio, ancho=200)

mensaje_entry = ctk.CTkEntry(root, placeholder_text="Ingrese el mensaje a codificar",
                             placeholder_text_color=config.BG_COLOR,
                             font=FONT,
                             text_color=config.FONT_COLOR,
                             bg_color=config.BG_COLOR,
                             fg_color=config.BG_MSG)
label_info = ctk.CTkLabel(root, text="IMPORTANTE: Por favor, use guiones (-) en lugar de espacios.", font=INFO_FONT, 
                          fg_color=config.BG_COLOR, text_color=config.FONT_COLOR, padx=10)

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
label_info.grid(row=6, column=3)
btn_codifcar.grid(row=4, column=4, pady=20, padx=30)
btn_decodifcar.grid(row=5, column=1, pady=20, padx=30)
label_decodificar.grid(row=5, column=2, columnspan=3, pady=20, padx=30, sticky="we")

decode = [btn_decodifcar, label_decodificar]
encode = [btn_codifcar, mensaje_entry, label_info]

root.after(10, lambda: verificar_audio(label_archivo, btn_reproducir, decode, encode))
root.mainloop()