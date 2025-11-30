# Huffman tree builder and codes for the provided Spanish-letter frequencies.
# This code prints:
# - the Huffman codes for each symbol (shorter codes for more frequent letters)
# - an ASCII representation of the tree
# The results are shown to the user.

from priority_queue import Node, Queue
from math import log2

def generate_codes(node, codes, prefix=""):
    if node.is_leaf():
        codes[node.symbol] = prefix or "0"
        return
    generate_codes(node.left, codes, prefix + "0")
    generate_codes(node.right, codes, prefix + "1")

def construir_codigo():

    # Input frequencies (percentages given by CVC)
    data = [
        ("E", 13.19),
        ("A", 12.85),
        ("O", 9.47),
        ("S", 7.56),
        ("N", 6.97),
        ("I", 6.7),
        ("R", 6.49),
        ("L", 4.94),
        ("D", 4.9),
        ("U", 4.34),
        ("T", 4.3),
        ("C", 4.14),
        ("M", 2.87),
        ("P", 2.47),
        ("B", 1.47),
        ("G", 1.08),
        ("Q", 1.07),
        ("V", 1.01),
        ("Y", 0.9),
        ("F", 0.67),
        ("H", 0.66),
        ("J", 0.43),
        ("Z", 0.39),
        ("LL",0.35),
        ("CH",0.22),
        ("Ñ",0.19),
        ("X",0.15),
        ("K",0.02),
        ("W",0.01),
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

    # Pretty-print codes sorted by frequency (descending)
    freq_dict = {sym: f for sym, f in data}
    sorted_syms = sorted(freq_dict.keys(), key=lambda s: -freq_dict[s])

    return codes

if __name__ == "__main__":
    codes = construir_codigo()
    print(codes)
    print("Huffman codes (symbol : frequency% -> code)")
    for s in codes:
        print(f"{s:3} -> {codes[s]}")
