from ply import lex

class Tokenizacao:
    def __init__(self) -> None:
        pass
    
def tokenizar_input(data: str) -> None:
    tokens = (
        'INTEGER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
    )

    # Regras regex de tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    # Regra para ignorar espaços em branco
    t_ignore = ' \t'

    # Função para lidar com números inteiros
    def t_INTEGER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Função para lidar com erros léxicos
    def t_error(t):
        print(f"[ERROR]: Caractere ilegal: '{t.value[0]}'")
        t.lexer.skip(1)

    lexer = lex.lex()

    lexer.input(data)

    print("Tokens:")
    
    while True:
        tok = lexer.token()
        
        if not tok:
            break 
        
        print(tok)

    resultado = eval(data)
    print("Resultado:", resultado)
    