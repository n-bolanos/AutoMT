class Node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol 
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.symbol is not None

class Queue:
    lista: list[Node] = []

    def push(self, node):
        self.lista.append(node)
        i = len(self.lista) - 1

        while i > 0 and self.lista[i].freq < self.lista[i-1].freq:
            self.lista[i], self.lista[i-1] = self.lista[i-1], self.lista[i]
            i -= 1

    def pop_min(self):
        return self.lista.pop(0)  # smallest element
