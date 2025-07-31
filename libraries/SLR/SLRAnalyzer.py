import pandas as pd

from libraries.Symbol.EndSymbol import EndSymbol
from libraries.Grammar import Grammar
from libraries.Command import CommandType
from libraries.SLR.SLRTable import SLRTable
from libraries.Symbol.Symbol import Symbol

class SLRAnalyzer():
    def __init__(self, gr: Grammar):
        self.table = SLRTable(gr)
        self.stack = [0]
        self.gr = gr
        self.historyColumns = ["Номер", "Стек", "Символы", "Вход", "Действие"]
        self.history = pd.DataFrame(columns=self.historyColumns)

    def reduce(self, state, symbol):
        prodIndex = self.table.loc[state, symbol].value
        A = self.gr[prodIndex].head
        n = len(self.gr[prodIndex].body)
        for i in range(n):
            self.stack.pop()
            self.symbols.pop()
        self.symbols.append(A)
        state = self.stack[-1]
        self.stack.append(self.table.loc[state, A].value)

    def history_add(self, string, index, type: CommandType):
        state = self.stack[-1]
        if index < len(string):
            symbol = string[index]
        else:
            symbol = EndSymbol()
        prodIndex = self.table.loc[state, symbol].value
        symbols_with_end = self.symbols# + [EndSymbol()]
        d = {"Номер": self.number, "Стек": str(self.stack), "Символы": str(symbols_with_end), "Вход": str(string[index:]+[EndSymbol()]), "Действие": "---"}
        self.number += 1
        if type == CommandType.SHIFT:
            d["Действие"] = f"Перенос {string[index]}"
        elif type == CommandType.REDUCE:
            d["Действие"] = f"Свертка {str(self.gr[prodIndex])}"
        elif type == CommandType.ACCEPT:
            d["Действие"] = "Принятие"
        elif type == CommandType.ERROR:
            d["Действие"] = "Ошибка"
        else:
            d["Действие"] = "Undef"
        self.history = pd.concat([self.history, pd.DataFrame(data=d, index=[0])], ignore_index=True)

    def parse(self, string: list[Symbol]):
        index = 0
        self.number = 0
        self.symbols = []
        while True:
            state = self.stack[-1]
            if index < len(string):
                symbol = string[index]
            else:
                symbol = EndSymbol()
            if self.table.loc[state, symbol].type == CommandType.SHIFT:
                self.history_add(string, index, CommandType.SHIFT)
                self.symbols.append(string[index])
                self.stack.append(self.table.loc[state, symbol].value)
                index += 1
            elif self.table.loc[state, symbol].type == CommandType.REDUCE:
                self.history_add(string, index, CommandType.REDUCE)
                self.reduce(state, symbol)
            elif self.table.loc[state, symbol].type == CommandType.ACCEPT:
                self.history_add(string, index, CommandType.ACCEPT)
                break
            else:
                self.history_add(string, index, CommandType.ERROR)
                return False
                #raise Exception(f"Ошибка синтаксического анализа в символе {index}")
        return True

