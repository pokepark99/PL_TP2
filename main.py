"""
	Processamento de Linguagens (ESI) 
	Trabalho Prático 2
    Alunos: 
        Daniela Pereira n25988
        Sofia Carvalho n25991
        Diogo Fernandes n26008
	
	invocar como: python main.py <ficheiro.fca>	
"""

import sys
import os
from grammar import Grammar

# se recebeu o nome do ficheiro fca
if len(sys.argv) == 2:
    file = sys.argv[1]
    path = "fca/"

    #criar o caminho para o ficheiro fca
    caminho = os.path.join(path,file)

    try:
        with open (caminho, 'r') as ficheiro:
            conteudo = ficheiro.read()
            # isto era para testar se estava a ler o ficheiro
            #print(conteudo)
        ag = Grammar()
        ag.build()
        # a analise sintatica recebe o conteudo do ficheiro afc
        res = ag.parse(conteudo)
        print(f"Resultado: {res}")

    # no caso do ficheiro nao ser encontrado
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{file}' não foi encontrado.")
    # no caso de outros erros
    except Exception as e:
        print(f"Um erro ocurreu: {e}")

# caso houve argumentos a mais
elif len(sys.argv) > 2:
    print("Uso: python main.py <ficheiro>")

#para remover isto depois -- por o utilizador a conseguir inserir instrucoes
else:
    print("Uso: python main.py <ficheiro>")
