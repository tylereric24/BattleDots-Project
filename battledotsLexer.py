# Generated from battledots.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("<\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\5\5\"\n\5\3\5\6\5%\n\5\r\5\16\5&\3")
        buf.write("\5\3\5\6\5+\n\5\r\5\16\5,\5\5/\n\5\3\6\6\6\62\n\6\r\6")
        buf.write("\16\6\63\3\7\6\7\67\n\7\r\7\16\78\3\7\3\7\2\2\b\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\3\2\5\5\2\62;C\\c|\3\2\62;\5\2\13")
        buf.write("\f\17\17\"\"\2A\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\25")
        buf.write("\3\2\2\2\7\30\3\2\2\2\t!\3\2\2\2\13\61\3\2\2\2\r\66\3")
        buf.write("\2\2\2\17\20\7u\2\2\20\21\7v\2\2\21\22\7c\2\2\22\23\7")
        buf.write("t\2\2\23\24\7v\2\2\24\4\3\2\2\2\25\26\7x\2\2\26\27\7u")
        buf.write("\2\2\27\6\3\2\2\2\30\31\7d\2\2\31\32\7t\2\2\32\33\7q\2")
        buf.write("\2\33\34\7{\2\2\34\35\7c\2\2\35\36\7n\2\2\36\37\7g\2\2")
        buf.write("\37\b\3\2\2\2 \"\7/\2\2! \3\2\2\2!\"\3\2\2\2\"$\3\2\2")
        buf.write("\2#%\t\2\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2")
        buf.write("\'.\3\2\2\2(*\7\60\2\2)+\t\2\2\2*)\3\2\2\2+,\3\2\2\2,")
        buf.write("*\3\2\2\2,-\3\2\2\2-/\3\2\2\2.(\3\2\2\2./\3\2\2\2/\n\3")
        buf.write("\2\2\2\60\62\t\3\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64\f\3\2\2\2\65\67\t\4\2\2\66\65")
        buf.write("\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29:\3\2\2\2:")
        buf.write(";\b\7\2\2;\16\3\2\2\2\t\2!&,.\638\3\b\2\2")
        return buf.getvalue()


class battledotsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    PLAYERS = 4
    NUMBER = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'start'", "'vs'", "'broyale'" ]

    symbolicNames = [ "<INVALID>",
            "PLAYERS", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "PLAYERS", "NUMBER", "WS" ]

    grammarFileName = "battledots.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


