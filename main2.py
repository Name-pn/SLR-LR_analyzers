from libraries.Grammar import Grammar
from libraries.LR.LRAnalyzer import LRAnalyzer
from libraries.LR.LRUtils import LRUtils
from libraries.Symbol.NonTerminal import NonTerminal
from libraries.Production import Production
from libraries.ProductionBody import ProductionBody
from libraries.Symbol.Terminal import Terminal
from libraries.Utils import firstDict, followDict

lst = []
lst.append(Production(NonTerminal("S\'"), ProductionBody([NonTerminal("S")])))
lst.append(Production(NonTerminal("S"), ProductionBody([NonTerminal("A"), Terminal("++")])))
lst.append(Production(NonTerminal("S"), ProductionBody([Terminal("++"), NonTerminal("A")])))
lst.append(Production(NonTerminal("S"), ProductionBody([NonTerminal("B")])))
lst.append(Production(NonTerminal("A"), ProductionBody([Terminal("c")])))
lst.append(Production(NonTerminal("B"), ProductionBody([Terminal("c")])))

gr = Grammar(lst, NonTerminal("S\'"))
utils = LRUtils(gr)
states = utils.items()
print(utils.write_states(states))
d = firstDict(gr)
print(d)
d = followDict(gr)
print(d)
analyzer = LRAnalyzer(gr)
string = [Terminal("c"), Terminal("++")]
print(analyzer.parse(string))