grammar battledots;

start: expr | <EOF>;

expr    : 'start' player_1=PLAYERS 'vs' player_2=PLAYERS ('vs' player_3=PLAYERS)? #durationfightExpr
        | 'broyale' duration=NUMBER  #brfightExpr
        ;

PLAYERS : ('-')? ('0' .. '9' | 'a'..'z' | 'A'..'Z') + ('.' ('0' .. '9' | 'a'..'z' | 'A'..'Z') +)? ; 
NUMBER : [0-9]+;
WS : [ \r\n\t]+ -> skip;
