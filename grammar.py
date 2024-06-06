# analisador sintatico

import ply.yacc as yacc
from lexer import Lexer

class Grammar:
    # regras de precedencia 
    # o que vem a esquerda tem precedencia do que vem a direita
    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        #('left', '<','>')
    )
    
    def __init__(self):
        self.lexer=None
        self.yacc=None
        self.tokens=None

    # inicializar o analisador sintatico
    def build(self, **kwargs): 
        self.lexer = Lexer()
        self.lexer.build(**kwargs) # inicializar o analisador lexer
        self.tokens = self.lexer.tokens
        self.yacc = yacc.yacc(module=self, **kwargs)

    # inicia a analise sintatica
    def parse(self, entrada):  
        self.lexer.input(entrada)
        return self.yacc.parse(lexer=self.lexer.lexer)

    #regras gramaticais
    def p_program(self,p):
        """programa : instrucoes"""
        p[0] = p[1]

    def p_instrucoes(self,p):
        """instrucoes : instrucao ';'     
                      | instrucoes instrucao ';'"""   #uma unica instrucao  | #varias instrucoes
        if len(p)==3:   #se o tamanho do p for 3->instrucoes: instrucao ; 
            p[0]= [p[1]]    #inicializa a lista com uma unica instrucao
        else:           #se for o outro caso 
            p[0]=[p[1]]     #usa a lista de instrucoes que existe
            p[0].append(p[2])       #adiciona uma nova instrucao

    def p_instrucao(self,p):
        """instrucao : escrita
                     | atribuicao
                     | definicaoF
                     | chamarF
                     | condicional """
        
        p[0]=p[1]
    
    def p_escrita(self,p):
        """escrita : ESC '(' expressao ')' """
        p[0]=('escrita',p[3])   #a expressao escrita

    def p_atribuicao(self,p):       
        """atribuicao : variavel '=' expressao"""
        p[0] = ('atribuicao', p[1], p[3])       #variavel e expressao

    def p_definicaoF(self,p):
        """definicaoF : FUNC variavel '(' parametros ')' ',' ':' expressao ';'
                      | FUNC variavel '(' parametros ')' ':' instrucoes FIM"""
        if len(p)==10:
            p[0]= ('definicaoFunc', p[2],p[4],p[8])
        else:
            p[0]= ('definicaoFuncMult', p[2],p[4],p[7])
        
    def p_chamarF(self,p):
        """chamarF : variavel '(' parametros  ')' """         #args
        p[0]= ('chamar',p[1],p[3])

    def p_condicional(self,p):
        """conditional : SE expressao ':' instrucoes FIM"""
        p[0] = ('if', p[2],p[4])

    def p_expressao(self,p):
        """expressao : termo
                     | expressao '+' termo
                     | expressao '-' termo
                     | interpolacao"""
        if len(p)== 2:
            p[0]=p[1]
        elif p[2]=='+':
            p[0]=('+', p[1], p[3])
        elif p[2]=='-':
            p[0]=('-',p[1],p[3])
      
    def p_interpolacao (self,p):
        """interpolacao : expressao '#' '{' variavel '}' """
        p[0]= ('interpolar', p[1], p[4])

    def p_termo (self,p):
        """termo : fator
                 | termo '*' fator        
                 | termo '/'  fator """
        if len(p)==2:
            p[0]=p[1]
        elif p[2]=='*':
            p[0]=('*', p[1],p[3])
        elif p[2]=='/':
            p[0]=('/', p[1], p[2])
    
    def p_fator(self,p):
        """fator : number
                 | numberF
                 | variavel
                 | '(' expressao ')'
                 | string  
                 | aleatorio
                 | lista
                 | entrada
                 | chamarF"""
        
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_concatenacao(self,p):
        """expressao : expressao '<' '>' expressao"""
        p[0]=('concatenacao',p[1],p[4])

    def p_aleatorio(self,p):
        """aleatorio : ALT '(' number ')'
            """
        p[0]=('aleatorio', p[3])

    def p_lista(self,p): 
        """lista : '[' elementos ']' 
                 | '[' ']' """                        
        if len(p)==4:
            p[0]=p[2]           #define a lista com os "elementos"
        else:
            p[0] = []       #inicializa lista vazia

    def p_entrada(self,p):
        """entrada : ENT '(' ')' """
        p[0] = ('entrada',)

    def p_elementos(self,p):
        """ elementos : expressao
                      | elementos ',' expressao  """
        if len(p)==2:
            p[0]=[p[1]]     #unico elemento na lista
        else:
            p[0] = p[1].append(p[3])   #adiciona a nov aexpressao p3 À lista existente p1

    def p_parametros(self,p):
        """parametros : variavel
                      | parametros ',' variavel """
        if len(p)==2:
            p[0]=[p[1]]
        else:
            p[0]= p[1].append(p[3])

    def p_argumentos(self,p):
        """argumentos : expressao
                      | argumentos ',' expressao"""
        if len(p)==2:
            p[0]=[p[1]]
        else:
            p[0]= p[1].append(p[3])

    def p_error(self,p):
        
        if p:
            print(f"Erro de sintaxe: 'token {p.value} na posicao{p.lexpos}'")
        else:
            print("Erro de sintaxe: fim inesperado do arquivo")