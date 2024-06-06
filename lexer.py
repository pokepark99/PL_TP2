# analisador lexico

import ply.lex as plex

class lexer:
    tokens=[
        'number',
        'commentOne',
        'commentMult',
        'variavel',
        'and',  # '/\'
        'or'  # '\/'
    ]
    
    reserved={
        'ESCREVER': 'ESC',
        'ENTRADA':'INPUT',
        'SAIDA':'OUTPUT',
        'SE':'SE',
        'FUNCAO':'FUNC',
        'ALEATORIO':'ALT',
        'FIM':'END',
        'map': 'MAP',  
        'fold': 'FOLD'  
    }


literals = ['+','-','*','/','(',')',';',':','=','#','!','<','>']

t_ignore = " "

# inicializar o analisador lexico
def build(self, **kwargs): 
    self.lexer = plex.lex(module=self, **kwargs)

# define o texto de entrada
def input(self, string): 
    self.lexer.input(string)

# determina o prox. token
def token(self):  
    token = self.lexer.token()
    return token

t_and = r'/\\'
t_or = r'\\/'

def t_number(self, t):
    r'[0-9]+' #numero com um ou mais digitos
    return t

def t_commentOne(self, t):
    r'--.*' #comentario de uma linha
    return t

def t_commentMult(self, t):
    r'{-(.|\n)*-}' #numero com um ou mais digitos
    return t

def t_variavel(self, t):
    r'([a-z]|\_)([a-z]|[0-9]|[\_])*([\?|\!])?' #identificador de variavel
    return t