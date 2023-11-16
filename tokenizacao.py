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

    # Lidar com ints
    def t_INTEGER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_error(t):
        print(f"[ERROR]: Caractere ilegal: '{t.value[0]}'")
        t.lexer.skip(1)

    lexer = lex.lex()

    lexer.input(data)

    print("Tokens:")
    
    num_palavras = 0
    num_linhas = 0
    num_caracteres = 0

    while True:
        tok = lexer.token()
        
        if not tok:
            break 
        
        print(tok)
        num_palavras += 1

    num_linhas = data.count('\n') + 1
    num_caracteres = len(data)

    print("\nResultados:")
    print("Número de palavras:", num_palavras)
    print("Número de linhas:", num_linhas)
    print("Número de caracteres:", num_caracteres)

    resultado_calculo = eval(data)
    print("Resultado do cálculo:", resultado_calculo)
