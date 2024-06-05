# analisador lexico

import ply.lex as plex

class lexer:


    tokens=[
    'NUMBER'
    ]
    
    reserved={
    'ESCREVER': 'ESC',
    'ENTRADA':'INPUT',
    'SAIDA':'OUTPUT',
    'SE':'SE',
    'FUNCAO':'FUNC',
    'ALEATORIO':'ALT',
    }


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

