from lexer import lexer

teste = lexer()
teste.build()
teste.input("") # por aqui algum input

while True:
    tok = teste.token()
    if not tok:
        break 
    print(tok)