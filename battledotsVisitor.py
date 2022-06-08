# Generated from battledots.g4 by ANTLR 4.9
from antlr4 import *
import os
import shutil
import time
import multiprocessing
from os import mkdir
import subprocess

if __name__ is not None and "." in __name__:
    from .battledotsParser import battledotsParser
else:
    from battledotsParser import battledotsParser

# This class defines a complete generic visitor for a parse tree produced by battledotsParser.

class battledotsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by battledotsParser#start.
    def visitStart(self, ctx:battledotsParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by battledotsParser#durationfightExpr.
    def visitDurationfightExpr(self, ctx:battledotsParser.DurationfightExprContext):
        player_1 = str(ctx.PLAYERS(0))
        player_2 = str(ctx.PLAYERS(1))
        player_3 = str(ctx.PLAYERS(2))
        
        
       
        isExist = os.path.exists('players') 

        if os.path.exists('players'):
           shutil.rmtree('players')
    
        if not isExist:
         os.mkdir('players')        
       

       
 
        if player_1 == '001':
         shutil.copytree('playerlibrary/001', 'players/001') 
        elif player_1 == '002':
         shutil.copytree('playerlibrary/002', 'players/002')
        elif player_1 == '003':
         shutil.copytree('playerlibrary/003', 'players/003')

        if player_2 == '001':
         shutil.copytree('playerlibrary/001', 'players/001')
        elif player_2 == '002':
         shutil.copytree('playerlibrary/002', 'players/002')
        elif player_2 == '003':
         shutil.copytree('playerlibrary/003', 'players/003')

        if player_3 == '001':
         shutil.copytree('playerlibrary/001', 'players/001')
        elif player_3 == '002':
         shutil.copytree('playerlibrary/002', 'players/002')
        elif player_3 == '003':
         shutil.copytree('playerlibrary/003', 'players/003')


        
        
        
        
        return self.visitChildren(ctx)




    # Visit a parse tree produced by battledotsParser#brfightExpr.
    def visitBrfightExpr(self, ctx:battledotsParser.BrfightExprContext):
        timeoutDur = (ctx.duration)

        if (timeoutDur == 0):
          os.system('python 3', 'battledots.py')
        else:
          process = subprocess.Popen(['python3', 'battledots.py'])
          try:
              process.wait(timeout=timeoutDur)
          except subprocess.TimeoutExpired:
              print(f'Timeout for ({timeoutDur}s) expired')
              process.terminate()


        return self.visitChildren(ctx)



del battledotsParser
