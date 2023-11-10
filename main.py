from interacoes_terminal import get_input_str
from tokenizacao import tokenizar_input

if __name__ == "__main__":
    data = get_input_str()

    count_open = data.count('(')
    count_close = data.count(')')
    
    if count_open != count_close:
        raise Exception('[ERROR] Parênteses incompletos!')        
    
    tokenizar_input(data)
