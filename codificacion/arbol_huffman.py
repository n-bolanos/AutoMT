# Huffman tree builder and codes for the provided Spanish-letter frequencies.
# Now includes a symbol for word separation ("-") mapped to a note.
from .priority_queue import Node, Queue

def generate_codes(node, codes, prefix=""):
    if node.is_leaf():
        codes[node.symbol] = prefix or "0"
        return
    generate_codes(node.left, codes, prefix + "0")
    generate_codes(node.right, codes, prefix + "1")

def mapear_codigo_nota(codes):
    note_sequence = [
    "C4","D4","E4","F4","G4","A4","B4",
    "C5","D5","E5","F5","G5","A5","B5",
    "C6","D6","E6","F6","G6","A6","B6",
    "C7","D7","E7","F7","G7","A7","B7",
    "C8","D8"]

    # Map each symbol to a note
    letters = list(codes.keys())
    letter_to_note = {}
    for i, letter in enumerate(letters):
        letter_to_note[letter] = note_sequence[i % len(note_sequence)]

    return letter_to_note

def construir_codigo():

    # Input frequencies (percentages given by CVC)
    data = [
        ("E", 13.19), ("A", 12.85), ("O", 9.47), ("S", 7.56),
        ("N", 6.97), ("I", 6.7), ("R", 5.49), ("L", 4.94),
        ("D", 4.9), ("U", 4.34), ("T", 4.3), ("C", 4.14),
        ("M", 2.87), ("P", 2.47), ("B", 1.47), ("G", 1.08),
        ("Q", 1.07), ("V", 1.01), ("Y", 0.9), ("F", 0.67),
        ("H", 0.66), ("J", 0.43), ("Z", 0.39), ("LL",0.35),
        ("CH",0.22), ("Ñ",0.19), ("X",0.15), ("K",0.02),
        ("W",0.01),
        ("-", 1.0)
    ]

    queue = Queue()
    for symbol, f in data:
        queue.push(Node(f, symbol=symbol))

    while len(queue.lista) > 1:
        n1 = queue.pop_min()
        n2 = queue.pop_min()
        merged = Node(n1.freq + n2.freq, left=n1, right=n2)
        queue.push(merged)

    root = queue.lista[0]

    codes = {}
    generate_codes(root, codes)

    # Map Huffman symbols to musical notes
    notas = mapear_codigo_nota(codes)

    return notas, codes

if __name__ == "__main__":
    notas, codes = construir_codigo()
    print("Symbol -> Note")
    for s in sorted(codes.keys()):
        print(f"{s:3}: {codes[s]} -> {notas[s]}")
