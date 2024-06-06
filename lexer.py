# analisador lexico

import ply.lex as plex

class lexer:
    tokens=[            #tokens que o lexer deve reconhecer
        'number', #numerointeiro
        'numberF', #numero decimal
        'true',
        'false',
        'variavel' #identificador variavel/funcao
        'string', #string entre ""
        'commentOne', #comentarios de uma linha
        'commentMult', #comenatrios de varias linhas
        'and',  # '/\'
        'or',  # '\/'
        'interpolation',
        'not', #operador lógico não 'neg'

    ]
    
    reserved={          #dicionário de palavras "reservadas" /palavras-chave
        'ESCREVER': 'ESC',
        'ENTRADA':'ENT',
        'SE':'SE',
        'FUNCAO':'FUNC',
        'ALEATORIO':'ALT',
        'FIM':'END',
        'map': 'MAP',  
        'fold': 'FOLD'  
    }

    tokens =tokens +list(reserved.values()) #lista final de tokens que o lexer vai reconhecer

    literals = ['+','-','*','/','(',')',';',':','=','#','!','<','>', '[',']']
    t_ignore = " \n"
    
    t_interpolation = r'\# [{][a-zA-Z_][a-zA-Z_0-9]*[}]' #expressoes regulares
    t_and = r'/\\'
    t_or = r'\\/'
    t_not = r'neg'

#init

# inicializar o analisador lexico
def build(self, **kwargs): 
    self.lexer = plex.lex(module=self, **kwargs)

# define o texto de entrada
def input(self, string): 
    self.lexer.input(string)

# determina o prox. token
def token(self):  
    token = self.lexer.token()
    return token if token is None else token.type


def t_number(self, t):
    r'[0-9]+' #numero com um ou mais digitos
    t.value = int(t.value)
    return t

def t_numberF(self,t):
    r"[0-9]+\.[0.9]+"
    t.value =float (t.value)

def t_commentOne(self, t):
    r'--.*' #comentário de uma linha
    return t

def t_commentMult(self, t):
    r'{-(.|\n)*-}' #numero com um ou mais digitos
    return t

def t_variavel(self, t):
    r'([a-z]|\_)([a-z]|[0-9]|[\_])*([\?|\!])?' #identificador de variavel
    return t

def t_STRING(self, t):
        r'"([^"\\]|\\.)*"'  # ([^"\\]|\\.) -> Grupo de caracteres que corresponde a qualquer caractere que não seja uma aspas duplas (") ou uma barra invertida (\)
        t.value = t.value[1:-1]  # O 1 e -1 servem para remover as aspas
        return t

def t_error(self, t):
        print(f"token inesperado'{t.value[0]}'")
        exit(1)

def t_newline(self, t):
        r'\n+'
        self.lexer.lineno += len(t.value)        