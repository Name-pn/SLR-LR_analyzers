import pandas as pd

from libraries import Utils
from libraries.Grammar import Grammar
from libraries.LR.LRUtils import LRUtils
from libraries.SLR.SLRAnalyzer import SLRAnalyzer
from libraries.SetOfItems import SetOfItems
from libraries.Symbol.EndSymbol import EndSymbol
from libraries.Symbol.Epsilon import Epsilon
from libraries.Symbol.NonTerminal import NonTerminal
from libraries.Production import Production
from libraries.ProductionBody import ProductionBody
from libraries.Symbol.Terminal import Terminal
from libraries.Utils import items, write_states, firstDict, followDict

lst = []
lst.append(Production(NonTerminal("S\'"), ProductionBody([NonTerminal("S")])))
# lst.append(Production(NonTerminal("S"), ProductionBody([NonTerminal("S"), Terminal("+"), NonTerminal("S")])))
# lst.append(Production(NonTerminal("S"), ProductionBody([NonTerminal("S"), NonTerminal("S")])))
# lst.append(Production(NonTerminal("S"), ProductionBody([Terminal("("), NonTerminal("S"), Terminal(")")])))
# lst.append(Production(NonTerminal("S"), ProductionBody([NonTerminal("S"), Terminal("*")])))
# lst.append(Production(NonTerminal("S"), ProductionBody([Terminal("a")])))

lst.append(Production(NonTerminal("S"), ProductionBody([NonTerminal("C"), NonTerminal("C")])))
lst.append(Production(NonTerminal("C"), ProductionBody([Terminal("c"), NonTerminal("C")])))
lst.append(Production(NonTerminal("C"), ProductionBody([Terminal("d")])))

gr = Grammar(lst, NonTerminal("S\'"))
utils = LRUtils(gr)
#I = SetOfItems()
#I.append((0, 0, EndSymbol()))
states = utils.items()
utils.write_states(states)
# gr = Grammar(lst, NonTerminal("S\'"))
# print(gr)
# states = items(gr)
# write_states(states, gr)
# d = firstDict(gr)
# print(d)
# d = followDict(gr)
# print(d)
# analyzer = SLRAnalyzer(gr)
# string = [Terminal("("), Terminal("a"), Terminal("+"), Terminal("a"), Terminal("*"), Terminal("a")]
# print(analyzer.parse(string))
# pd.set_option('display.max_columns', 7)
# pd.set_option('display.width', 1000)
# print(analyzer.history.to_string(index=False))