# analisador sintatico

import ply.yacc as yacc
from lexer import lexer

class Grammar:
    # regras de precedencia 
    # o que vem a esquerda tem precedencia do que vem a direita
    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
    )
    
    # inicializar o analisador sintatico
    def build(self, ): 
        self.lexer = lexer
        self.lexer.build() # inicializar o analisador lexer

    # inicia a analise sintatica
    def parse(self, entrada):  
        self.lexer.input(entrada)
        return self.yacc.parse(lexer=self.lexer.lexer)

    # gramatica
    def p_expr(self, p): 
        # isto e um exemplo
        """ E : E '+' T 
            | E E"""