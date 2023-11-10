from ply import lex

class Tokenizacao:
    def __init__(self) -> None:
        pass
    
def tokenizar_input(str: data) -> :
  # Definição dos tokens
    tokens = (
        'INTEGER',
        'PLUS',
        'MINUS',
        'LPAREN',
        'RPAREN',
    )

    # Regras de expressão regular para os tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    # Regra para ignorar espaços em branco
    t_ignore = ' \t'

    # Função para lidar com números inteiros
    def t_INTEGER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Tratamento de erros
    def t_error(t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    # Verificação de erros para parênteses desbalanceados
    def t_LPAREN_error(t):
        r'\('
        print("Error: Unbalanced parentheses. Missing closing parenthesis.")

    def t_RPAREN_error(t):
        r'\)'
        print("Error: Unbalanced parentheses. Unexpected closing parenthesis.")

    lexer = lex.lex()

    lexer.input(data)

    print("Tokens:")
    
    while True:
        tok = lexer.token()
        
        if not tok:
            break  # No more input
        
        print(tok)
