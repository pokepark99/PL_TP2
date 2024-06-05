# analisador sintatico

import ply.yacc as yacc
from lexer import Lexico

class Grammar:
    # inicializar o analisador sintatico
    def build(self, ): 
        self.lexer = Lexico
        self.lexer.build() # inicializar o analisador lexico

    # inicia a analise sintatica
    def parse(self, entrada):  
        self.lexer.input(entrada)
        return self.yacc.parse(lexer=self.lexer.lexer)

    # gramatica
    def p_expr(self, p): 
        # isto e um exemplo
        """ E : E '+' T 
            | E E"""