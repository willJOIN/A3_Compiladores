class InteracoesTerminal:
    def __init__(self) -> None:
        pass
    
def get_input_str() -> str:
    input = input("Por favor, insira uma expressão matemática: ") # ex: "3 + 5 - (2 + 4)"
    assert isinstance(input, str), "A variável não é uma string (str)"
    return input
