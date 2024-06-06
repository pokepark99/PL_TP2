# analisador sintatico

import ply.yacc as pyacc
from lexer import lexer

class Grammar:
    # regras de precedencia 
    # o que vem a esquerda tem precedencia do que vem a direita
    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('left', '<','>')
    )
    
    def __init__(self):
        self.lexer=None
        self.yacc=None
        self.tokens=None

   
    # inicializar o analisador sintatico
    def build(self, **kwargs): 
        self.lexer = lexer()
        self.lexer.build(**kwargs) # inicializar o analisador lexer
        self.tokens = self.lexer.tokens
        self.yacc = yacc.yacc(module=self, **kwargs)

    # inicia a analise sintatica
    def parse(self, entrada):  
        self.lexer.input(entrada)
        return self.yacc.parse(lexer=self.lexer.lexer)

    # gramatica
    def p_expr(self, p): 
        # isto e um exemplo
        """ E : E '+' T 
            | E E"""