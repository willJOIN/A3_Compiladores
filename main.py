from interacoes_terminal import get_input_str
from tokenizacao import tokenizar_input

if __name__ == "__main__":
    expressao_matematica = get_input_str()
    tokenizar_input(expressao_matematica)
