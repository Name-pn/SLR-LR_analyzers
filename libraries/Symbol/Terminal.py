from libraries.Symbol.Symbol import Symbol
from libraries.Symbol.SymbolType import SymbolType

class Terminal(Symbol):
    def __init__(self, value):
        super().__init__(value, SymbolType.TERMINAL)


    def __str__(self):
        return str(self.value)