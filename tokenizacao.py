from ply import lex

class Tokenizacao:
    def __init__(self) -> None:
        pass
    
def tokenizar_input(data: str) -> None:
    tokens = (
        'INTEGER',
        'PLUS',
        'MINUS',
        'LPAREN',
        'RPAREN',
    )

    # Regras regex de tokens especificos
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

    def t_error(t):
        print(f"[ERROR]: Caractere ilegal: '{t.value[0]}'")
        t.lexer.skip(1)

    def t_LPAREN_error(t):
        r'\('
        print("[ERROR]: Falta parenteses de fechamento.")

    def t_RPAREN_error(t):
        r'\)'
        print("[ERROR]: Paranteses de fechamento sem um de abertura antes.")

    lexer = lex.lex()

    lexer.input(data)

    print("Tokens:")
    
    while True:
        tok = lexer.token()
        
        if not tok:
            break 
        
        print(tok)
