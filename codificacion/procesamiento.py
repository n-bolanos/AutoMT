from .arbol_huffman import construir_codigo

codif_espanol = construir_codigo()[0]

def codificar(msj: str):
    """
    This function encodes a message returning a list of musical notes
    """
    notes = []
    for letter in msj:
        notes.append(codif_espanol[letter])
    return notes

def decodificar(notas):
    """
    Decodes a list of musical notes back to a string message.
    """
    note_to_letter = {note: letter for letter, note in codif_espanol.items()}
    
    message = ""
    for nota in notas:
        if nota in note_to_letter:
            message += note_to_letter[nota]
        else:
            message += "?"  # unknown note
    return message