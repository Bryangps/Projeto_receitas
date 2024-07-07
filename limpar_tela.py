import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Use a função para limpar a tela
limpar_tela()

