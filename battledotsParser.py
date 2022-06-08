# Generated from battledots.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("\27\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\21\n\3\3\3\3\3\5\3\25\n\3\3\3\2\2\4\2\4\2")
        buf.write("\2\2\27\2\b\3\2\2\2\4\24\3\2\2\2\6\t\5\4\3\2\7\t\3\2\2")
        buf.write("\2\b\6\3\2\2\2\b\7\3\2\2\2\t\3\3\2\2\2\n\13\7\3\2\2\13")
        buf.write("\f\7\6\2\2\f\r\7\4\2\2\r\20\7\6\2\2\16\17\7\4\2\2\17\21")
        buf.write("\7\6\2\2\20\16\3\2\2\2\20\21\3\2\2\2\21\25\3\2\2\2\22")
        buf.write("\23\7\5\2\2\23\25\7\7\2\2\24\n\3\2\2\2\24\22\3\2\2\2\25")
        buf.write("\5\3\2\2\2\5\b\20\24")
        return buf.getvalue()


class battledotsParser ( Parser ):

    grammarFileName = "battledots.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'start'", "'vs'", "'broyale'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "PLAYERS", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    PLAYERS=4
    NUMBER=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(battledotsParser.ExprContext,0)


        def getRuleIndex(self):
            return battledotsParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = battledotsParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [battledotsParser.T__0, battledotsParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [battledotsParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return battledotsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DurationfightExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a battledotsParser.ExprContext
            super().__init__(parser)
            self.player_1 = None # Token
            self.player_2 = None # Token
            self.player_3 = None # Token
            self.copyFrom(ctx)

        def PLAYERS(self, i:int=None):
            if i is None:
                return self.getTokens(battledotsParser.PLAYERS)
            else:
                return self.getToken(battledotsParser.PLAYERS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDurationfightExpr" ):
                listener.enterDurationfightExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDurationfightExpr" ):
                listener.exitDurationfightExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDurationfightExpr" ):
                return visitor.visitDurationfightExpr(self)
            else:
                return visitor.visitChildren(self)


    class BrfightExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a battledotsParser.ExprContext
            super().__init__(parser)
            self.duration = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(battledotsParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrfightExpr" ):
                listener.enterBrfightExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrfightExpr" ):
                listener.exitBrfightExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrfightExpr" ):
                return visitor.visitBrfightExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = battledotsParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [battledotsParser.T__0]:
                localctx = battledotsParser.DurationfightExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(battledotsParser.T__0)
                self.state = 9
                localctx.player_1 = self.match(battledotsParser.PLAYERS)
                self.state = 10
                self.match(battledotsParser.T__1)
                self.state = 11
                localctx.player_2 = self.match(battledotsParser.PLAYERS)
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==battledotsParser.T__1:
                    self.state = 12
                    self.match(battledotsParser.T__1)
                    self.state = 13
                    localctx.player_3 = self.match(battledotsParser.PLAYERS)


                pass
            elif token in [battledotsParser.T__2]:
                localctx = battledotsParser.BrfightExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(battledotsParser.T__2)
                self.state = 17
                localctx.duration = self.match(battledotsParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





