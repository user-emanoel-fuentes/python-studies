# =============================================================================
#                         STRINGS EM PYTHON
# =============================================================================


# =============================================================================
# 1. O QUE É UMA STRING?
# =============================================================================
#
# Uma string é uma sequência de caracteres — letras, números, símbolos ou
# espaços — armazenados em uma variável de texto.
#
# Em Python, strings são IMUTÁVEIS: uma vez criadas, não podem ser alteradas
# diretamente. Qualquer "modificação" gera uma nova string.
#
# Strings podem ser criadas com aspas simples, duplas ou triplas:

nome        = 'Maria'            # aspas simples
cidade      = "São Paulo"        # aspas duplas
paragrafo   = """Este é um
texto com múltiplas linhas."""   # aspas triplas (multilinha)

# Todas as formas acima são válidas. Use a que melhor se adapta ao contexto.


# =============================================================================
# 2. ÍNDICES — ACESSANDO CARACTERES INDIVIDUALMENTE
# =============================================================================
#
# O QUE É:
#   Cada caractere de uma string possui uma posição (índice).
#   A contagem começa em 0 (do início) ou em -1 (do final).
#
# SINTAXE:
#   string[indice]
#
# EXEMPLO:

palavra = "Python"

print(palavra[0])   # 'P'  → primeiro caractere
print(palavra[1])   # 'y'
print(palavra[-1])  # 'n'  → último caractere
print(palavra[-2])  # 'o'  → penúltimo

#   P  y  t  h  o  n
#   0  1  2  3  4  5   → índices positivos
#  -6 -5 -4 -3 -2 -1   → índices negativos
#
# QUANDO USAR:
#   Quando precisar de um caractere específico da string.
#
# QUANDO NÃO USAR:
#   Quando quiser verificar se uma palavra existe dentro de outra —
#   use o operador 'in' para isso.
#
# MELHOR PRÁTICA:
#   Prefira índices negativos para acessar o final da string,
#   pois são mais legíveis que calcular o tamanho manualmente.


# =============================================================================
# 3. TAMANHO — DESCOBRINDO O COMPRIMENTO DA STRING
# =============================================================================
#
# O QUE É:
#   A função len() retorna a quantidade de caracteres de uma string,
#   incluindo espaços e símbolos.
#
# SINTAXE:
#   len(string)
#
# EXEMPLO:

frase = "Olá, mundo!"
tamanho = len(frase)
print(tamanho)  # 11

# QUANDO USAR:
#   Para validar senhas, limitar entradas, percorrer strings com for, etc.
#
# MELHOR PRÁTICA:
#   Armazene o resultado em uma variável se for usar len() mais de uma vez
#   no mesmo bloco — evita recalcular.


# =============================================================================
# 4. OPERADORES COM STRINGS
# =============================================================================
#
# O QUE É:
#   Python permite usar operadores para concatenar (+), repetir (*) e
#   verificar a existência de trechos em strings (in / not in).
#
# SINTAXE E EXEMPLOS:

# --- Concatenação (+) ---
primeiro = "Bom"
segundo  = "dia"
saudacao = primeiro + " " + segundo
print(saudacao)  # "Bom dia"

# --- Repetição (*) ---
linha = "-" * 30
print(linha)  # "------------------------------"

# --- Verificação (in / not in) ---
texto = "Aprender Python é divertido"
print("Python" in texto)       # True
print("Java" not in texto)     # True

# QUANDO USAR:
#   + para montar mensagens dinâmicas.
#   * para criar separadores visuais ou padrões repetidos.
#   in/not in para validar se um trecho existe na string.
#
# QUANDO NÃO USAR:
#   Evite usar + dentro de loops para concatenar muitas strings —
#   prefira join() ou f-strings nesse caso (mais eficiente).
#
# MELHOR PRÁTICA:
#   Use f-strings no lugar de concatenação sempre que possível.
#   Ruim:   "Olá " + nome + ", você tem " + str(idade) + " anos."
#   Bom:    f"Olá {nome}, você tem {idade} anos."


# =============================================================================
# 5. CORTES (SLICING) — EXTRAINDO PARTES DA STRING
# =============================================================================
#
# O QUE É:
#   Slicing permite extrair um trecho (fatia) da string usando índices.
#
# SINTAXE:
#   string[inicio : fim : passo]
#   - inicio: índice onde começa (incluído)
#   - fim:    índice onde termina (NÃO incluído)
#   - passo:  de quantos em quantos caracteres avança (padrão: 1)
#
# EXEMPLOS:

s = "0123456789"

print(s[2:5])    # '234'   → do índice 2 até 4
print(s[:4])     # '0123'  → do início até 3
print(s[6:])     # '6789'  → do índice 6 até o fim
print(s[::2])    # '02468' → de 2 em 2
print(s[::-1])   # '9876543210' → string invertida!

# Com texto real:
linguagem = "JavaScript"
print(linguagem[0:4])   # 'Java'
print(linguagem[4:])    # 'Script'

# QUANDO USAR:
#   Para extrair partes de textos, inverter strings, pegar prefixos/sufixos.
#
# QUANDO NÃO USAR:
#   Quando a posição do trecho for variável/desconhecida —
#   use find() ou métodos de busca nesse caso.
#
# MELHOR PRÁTICA:
#   Omita o 0 no início (s[:5] é mais limpo que s[0:5]).
#   Use s[::-1] para inverter strings (pythônico e eficiente).


# =============================================================================
# 6. FORMATAÇÃO DE STRINGS
# =============================================================================
#
# O QUE É:
#   Formas de inserir valores de variáveis dentro de strings.
#   Existem 3 abordagens principais em Python.
#
# --- ABORDAGEM 1: f-string (recomendada, Python 3.6+) ---
#
# SINTAXE:
#   f"texto {variavel} texto"
#
# EXEMPLO:

nome  = "Carlos"
idade = 28
print(f"Olá, {nome}! Você tem {idade} anos.")
# "Olá, Carlos! Você tem 28 anos."

# Também aceita expressões diretamente:
print(f"Daqui a 5 anos você terá {idade + 5} anos.")

# --- ABORDAGEM 2: .format() ---
#
# SINTAXE:
#   "texto {} texto".format(valor)
#
# EXEMPLO:

print("Olá, {}! Você tem {} anos.".format(nome, idade))

# --- ABORDAGEM 3: % (antiga, evitar em código novo) ---

print("Olá, %s! Você tem %d anos." % (nome, idade))

# QUANDO USAR:
#   f-strings → sempre que possível (mais legível e rápido).
#   .format() → quando precisar de compatibilidade com Python 2 ou
#               templates reutilizáveis.
#   %         → apenas em código legado — evite em projetos novos.
#
# MELHOR PRÁTICA:
#   Padronize o uso de f-strings no projeto inteiro.
#   Para números, use formatação de precisão quando necessário:
#   f"{preco:.2f}"  → exibe 2 casas decimais


# =============================================================================
# 7. PRINCIPAIS MÉTODOS DE STRINGS
# =============================================================================
#
# O QUE É:
#   Métodos são funções embutidas das strings que realizam operações comuns.
#   São chamados com a notação: string.metodo()
#
# SINTAXE GERAL:
#   resultado = string.metodo(argumentos)
#
# ─────────────────────────────────────────────────────
# GRUPO 1: TRANSFORMAÇÃO DE CAIXA (MAIÚSCULO/MINÚSCULO)
# ─────────────────────────────────────────────────────

texto = "python é incrível"

print(texto.upper())       # "PYTHON É INCRÍVEL"
print(texto.lower())       # "python é incrível"
print(texto.capitalize())  # "Python é incrível" → só 1ª letra maiúscula
print(texto.title())       # "Python É Incrível"  → 1ª letra de cada palavra

# QUANDO USAR:
#   Comparações sem diferenciar maiúsculas/minúsculas:
#   entrada.lower() == "sim"

# ─────────────────────────────────────────────────────
# GRUPO 2: REMOÇÃO DE ESPAÇOS E CARACTERES
# ─────────────────────────────────────────────────────

entrada = "   olá mundo   "

print(entrada.strip())     # "olá mundo"  → remove dos dois lados
print(entrada.lstrip())    # "olá mundo   " → remove só da esquerda
print(entrada.rstrip())    # "   olá mundo"  → remove só da direita

# QUANDO USAR:
#   Sempre ao receber dados do usuário (inputs, arquivos, APIs).
#   Espaços extras são uma fonte comum de bugs silenciosos.

# ─────────────────────────────────────────────────────
# GRUPO 3: BUSCA E VERIFICAÇÃO
# ─────────────────────────────────────────────────────

frase = "O rato roeu a roupa"

# .find()  → retorna o índice da primeira ocorrência (-1 se não encontrar)
print(frase.find("roeu"))    # 7
print(frase.find("gato"))    # -1

# .count() → conta quantas vezes aparece
print(frase.count("ro"))     # 3

# .startswith() / .endswith() → verifica início e fim
print(frase.startswith("O rato"))  # True
print(frase.endswith("roupa"))     # True

# .isdigit()  → True se todos os caracteres são dígitos
print("123".isdigit())    # True
print("12a".isdigit())    # False

# .isalpha()  → True se todos os caracteres são letras
print("abc".isalpha())    # True
print("ab1".isalpha())    # False

# QUANDO USAR:
#   find()       → quando precisar da posição do trecho encontrado.
#   in           → quando só precisar saber se existe (mais simples).
#   startswith() → validar extensões de arquivo, prefixos de URL, etc.
#   isdigit()    → validar se uma entrada é numérica antes de converter.

# ─────────────────────────────────────────────────────
# GRUPO 4: SUBSTITUIÇÃO
# ─────────────────────────────────────────────────────

original = "Eu gosto de café"

# .replace(antigo, novo) → substitui todas as ocorrências
novo = original.replace("café", "chá")
print(novo)  # "Eu gosto de chá"

# Limitando substituições:
frase2 = "aaa bbb aaa ccc aaa"
print(frase2.replace("aaa", "XXX", 2))  # "XXX bbb XXX ccc aaa"

# QUANDO USAR:
#   Limpeza de dados, substituição de templates, sanitização de texto.
#
# QUANDO NÃO USAR:
#   Substituições complexas com padrões variáveis —
#   use o módulo 're' (expressões regulares) nesse caso.

# ─────────────────────────────────────────────────────
# GRUPO 5: DIVISÃO E JUNÇÃO
# ─────────────────────────────────────────────────────

# .split() → divide a string em uma lista
csv_linha = "nome,email,telefone"
campos = csv_linha.split(",")
print(campos)  # ['nome', 'email', 'telefone']

# Sem argumento: divide por espaços
frase3 = "Python é muito poderoso"
palavras = frase3.split()
print(palavras)  # ['Python', 'é', 'muito', 'poderoso']

# .join() → junta uma lista em uma string (inverso do split)
lista = ["2024", "01", "15"]
data  = "-".join(lista)
print(data)  # "2024-01-15"

# QUANDO USAR:
#   split() → processar CSVs, separar palavras, dividir por delimitador.
#   join()  → montar strings a partir de listas (muito mais eficiente que +).
#
# MELHOR PRÁTICA:
#   Para juntar muitos elementos, SEMPRE use join() em vez de concatenar
#   com + dentro de um loop. É significativamente mais rápido.


# =============================================================================
# 8. CARACTERES ESPECIAIS (ESCAPE)
# =============================================================================
#
# O QUE É:
#   Sequências que representam caracteres que não podem ser digitados
#   diretamente em uma string.
#
# PRINCIPAIS:
#   \n  → nova linha
#   \t  → tabulação (tab)
#   \\  → barra invertida literal
#   \"  → aspas duplas dentro de string com aspas duplas
#   \'  → aspas simples dentro de string com aspas simples
#
# EXEMPLOS:

print("Linha 1\nLinha 2\nLinha 3")
print("Nome:\tCarlos")
print("Caminho: C:\\Users\\carlos")
print("Ele disse: \"Olá!\"")

# STRING RAW (r"") — ignora todos os escapes:
caminho = r"C:\Users\carlos\documentos"
print(caminho)  # C:\Users\carlos\documentos  (sem interpretar \U, \c, \d)

# QUANDO USAR r"":
#   Caminhos de arquivos no Windows, expressões regulares.


# =============================================================================
# 9. RESUMO GERAL
# =============================================================================
#
# ┌──────────────────────┬──────────────────────────────────────────────────┐
# │ CONCEITO             │ USO PRINCIPAL                                    │
# ├──────────────────────┼──────────────────────────────────────────────────┤
# │ Criação              │ '', "", """ """ para texto simples ou multilinha  │
# │ Índices              │ s[0], s[-1] para acessar caracteres              │
# │ Tamanho              │ len(s) para saber o comprimento                  │
# │ Operadores           │ + concatena, * repete, in verifica existência    │
# │ Slicing              │ s[2:5], s[::-1] para extrair trechos             │
# │ f-strings            │ f"{var}" para formatar texto com variáveis       │
# │ .upper()/.lower()    │ normalizar caixa para comparações                │
# │ .strip()             │ limpar espaços de entradas do usuário            │
# │ .replace()           │ substituir trechos de texto                      │
# │ .split()/.join()     │ dividir texto em lista e unir lista em texto     │
# │ .find()/.count()     │ localizar e contar trechos                       │
# │ .startswith/endswith │ verificar prefixos e sufixos                     │
# │ .isdigit()/.isalpha()│ validar tipo do conteúdo                         │
# │ Escape (\n, \t...)   │ caracteres especiais e formatação interna        │
# │ r"string"            │ strings brutas (caminhos, regex)                 │
# └──────────────────────┴──────────────────────────────────────────────────┘
#
# REGRAS DE OURO:
#   1. Use f-strings para formatar — são as mais legíveis e rápidas.
#   2. Sempre use .strip() ao processar entradas externas.
#   3. Use .lower() ou .upper() para comparar textos sem erro de caixa.
#   4. Prefira .join() a concatenar strings em loops.
#   5. Lembre-se: strings são imutáveis — métodos sempre retornam novas strings.
#
# =============================================================================