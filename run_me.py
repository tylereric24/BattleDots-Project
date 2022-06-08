from antlr4 import *
from battledotsLexer import battledotsLexer
from battledotsParser import battledotsParser
from battledotsVisitor import battledotsVisitor
import time
import os

def main():
	lexer = battledotsLexer( FileStream('testerfile'))
	token_stream = CommonTokenStream(lexer)
	parser = battledotsParser( token_stream )
	visitor = battledotsVisitor()

	while True:
		tree = parser.start()
		if tree.expr() == None:
			#this is end of file
			break
		print( tree.toStringTree(recog=parser))
		visitor.visit(tree)

	time.sleep(10)


if __name__ == '__main__':
	main()

