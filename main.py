import sys
import os

# se recebeu o nome do ficheiro fca
if len(sys.argv) == 2:
    file = sys.argv[1]
    path = "fca/"

    #criar o caminho para o ficheiro fca
    caminho = os.path.join(path,file)

    try:
        with open (caminho, 'r') as ficheiro:
            conteudo = ficheiro.read()

            # isto e para testar se esta a ler o ficheiro
            print(conteudo)

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
