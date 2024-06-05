# analisador lexico

import ply.lex as plex

class Lexico: 
    tokens = ()
    literals = []
    t_ignore = " "

# inicializar o analisador lexico
def build(self, ): 
    ...

# define o texto de entrada
def input(self, string): 
    ...

# determina o prox. token
def token(self):  
    ...