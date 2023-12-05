import re
from func import *

def lexer(contents):
    # as linhas do arquivos são dividias por \n
    lines = contents.split('\n')

    nLines = []
    # laço para cada linha do arquivo
    for line in lines:
        # var char recebe todos os caracteres da linha
        chars = list(line)

        temp_str = ""
        # lista par armazenar os tokens
        tokens = []

        # variavel para contar quantidade de aspas
        quote_count = 0
        lparen_count = 0
        rparen_count = 0

        # condição para continuar na linha
        if len(chars) != 0:
            # laço que percorre lista de caracteres
            for i in range(len(chars)):

                # print(chars[i])
                # se o caracter for uma aspas aumentar variavel quote_count
                if chars[i] == '"' or chars[i] == "'":
                    quote_count += 1

                # se quantidade de aspas for par definir que estamos fora de aspas
                if quote_count % 2 == 0:
                    in_quotes = False
                # caso contrario definir que estamos dentro de aspas
                else:
                    in_quotes = True

                # esta sessão de ifs elifs e else decidem a separação dos tokens da linha atual
                if chars[i] == " " and in_quotes == False:
                    tokens.append(temp_str)
                    temp_str = ""

                elif chars[i] == '(' and in_quotes == False:
                    lparen_count += 1
                    tokens.append(temp_str)
                    temp_str = chars[i]
                    tokens.append(temp_str)
                    temp_str = ''

                elif chars[i] == ')' and in_quotes == False:
                    rparen_count += 1
                    tokens.append(temp_str)
                    temp_str = chars[i]
                    tokens.append(temp_str)
                    temp_str = ''

                elif chars[i] in '+-*/=^':
                    if(chars[i] == '^'):
                        chars[i] = '**'
                    tokens.append(temp_str)
                    temp_str = chars[i]
                    tokens.append(temp_str)
                    temp_str = ''

                # adicionar caracter em temp_str
                else:
                    temp_str += chars[i]

            # adicionar ultimo token a lista de tokens
            tokens.append(temp_str)
            tokens = list(filter(('').__ne__, tokens))

            # lista de tokens com tipos
            items = []

            # laço para tipar os tokens
            for token in tokens:
                
                # se token começar e terminar com aspas simples ou composta tipar como STRING
                if token[0] == "'" or token[0] == '"':
                    if token[-1] == '"' or token[-1] == "'":
                        items.append(("string", token))
                    # se token começar com aspas e nao terminar lançar erro
                    else:
                        raise Exception("missing closing quote: \"")
                    
                # verifica se o token é um parentesis esquerdo
                elif re.match(r"\(", token):
                    items.append(("lparen", token))

                elif re.match(r"\)", token):
                    items.append(("rparen", token))    

                # verifica se o token é um parentesis direito
                elif re.match(r"[0-9]+", token):
                    items.append(("number", token))
                
                # verificar se o token é um simbolo através de um regex
                elif re.match(r"[a-zA-Z_]+[.a-zA-Z0-9_]*", token):
                    items.append(("symbol", token))

                # verificar se o token é um operador
                elif token in ['+','-','**','/','=','^']:
                    items.append(("operator", token))
                
            nLines.append(items) 
    return nLines

# All Symbols. Anything not in here  is considered a variable
Symbols = [
    "var",
    "print"
]

Vars = {
    
}

def parse(file):

    contents = open(file, 'r').read()
    lines = lexer(contents)

    for i in range(len(lines)):
        
        # lina recebe a linha i do arquivo
        line = lines[i]

        # instruction line
        inst_line = ""

        # percorre todos os tokens da linha i
        for y in range(len(line)):

            # token atual
            token = line[y]

            # token[0] -> tipo do token
            # token[1] -> valor do token
            if token[0] == 'symbol':
                if token[1] in Symbols:
                    if token[1] == 'var':
                        inst_line += 'Vars["$v"]'
                    elif token[1] == 'print':
                        inst_line += 'print($v)'
                else: # assuming a variable
                    # se o valor do próximo token for um sinal de atribuição
                    if arrVal(line, y+1)[1] == '=':
                        # se o valor do token anterior for o simbolo var
                        if line[y-1][1] == 'var':
                            if token[1] in Vars:
                                raise Exception('Variable already exists')
                                
                            else:
                                if re.match(r'[.a-zA-Z0-9_]+', token[1]):
                                    inst_line = inst_line.replace('$v', token[1])
                                else:
                                    raise Exception('Variable name is no accepted')

                        # caso o valor do token anterior não for o simbolo var
                        else:
                            if token[1] in Vars:
                                inst_line = 'Vars["'+ token[1] + '"]'
                            else:
                                # throw error
                                break
                    else:
                        if token[1] in Vars:
                            inst_line = inst_line.replace('$v', str(Vars[token[1]]))
            elif token[0] == 'operator':
                inst_line += token[1]
            elif token[0] == 'number':
                inst_line += token[1]
            elif token[0] == 'string':
                inst_line += '"' + token[1] + '"'
            elif token[0] == 'lparen':
                inst_line += '"' + token[1] + '"'
            elif token[0] == 'rparen':
                inst_line += '"' + token[1] + '"'
        # verificar se a linha é uma expressão numérica e então utilizar a função exec('print({eval(int_line)})')
        if is_line_expr(line):
            inst_line = inst_line.replace('^','**')
            exec(f'print({eval(inst_line)})')
        else:
            exec(inst_line)
    return lines

def is_line_expr(line):
    for token in line:
        if token[0] == 'symbol':
            return False
    return True 