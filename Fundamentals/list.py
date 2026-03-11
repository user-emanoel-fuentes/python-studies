# =============================================================================
# LISTAS EM PYTHON
# =============================================================================
# Arquivo de referência rápida sobre Listas em Python.
# Estrutura: O que é | Sintaxe | Melhores Práticas | Quando Usar |
#            Quando Não Usar | Recursos Comuns | Resumo
# =============================================================================


# -----------------------------------------------------------------------------
# 1. O QUE É
# -----------------------------------------------------------------------------
# Uma lista é uma estrutura de dados que armazena uma coleção ordenada de
# elementos. Ela é:
#
#   - MUTÁVEL       → seus elementos podem ser alterados após a criação
#   - ORDENADA      → os elementos mantêm a ordem em que foram inseridos
#   - HETEROGÊNEA   → pode conter elementos de tipos diferentes
#   - INDEXADA      → cada elemento é acessado por um índice (começa em 0)
#   - DINÂMICA      → cresce ou diminui conforme elementos são adicionados
#                     ou removidos
#
# Listas são representadas por colchetes [ ] e seus elementos são separados
# por vírgulas.


# -----------------------------------------------------------------------------
# 2. SINTAXE DE USO
# -----------------------------------------------------------------------------

# --- Criando listas ---
lista_vazia     = [] # ou list()
lista_numeros   = [1, 2, 3, 4, 5]
lista_strings   = ["maçã", "banana", "laranja"]
lista_mista     = [42, "texto", 3.14, True, None]
lista_aninhada  = [[1, 2], [3, 4], [5, 6]]   # lista dentro de lista

# --- Acessando elementos (indexação) ---
frutas = ["maçã", "banana", "laranja", "uva"]

primeiro    = frutas[0]     # "maçã"    → índice positivo (do início)
ultimo      = frutas[-1]    # "uva"     → índice negativo (do final)
penultimo   = frutas[-2]    # "laranja"

# --- Fatiamento (slicing): lista[início:fim:passo] ---
# O índice de início é INCLUSIVO; o de fim é EXCLUSIVO.
dois_primeiros  = frutas[0:2]   # ["maçã", "banana"]
do_segundo      = frutas[2:]    # ["laranja", "uva"]
ate_terceiro    = frutas[:3]    # ["maçã", "banana", "laranja"]
invertida       = frutas[::-1]  # ["uva", "laranja", "banana", "maçã"]

# --- Modificando elementos ---
frutas[1] = "manga"             # substitui "banana" por "manga"

# --- Iterando sobre uma lista ---
for fruta in frutas:
    print(fruta)

# Com índice:
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# --- List Comprehension (forma pythônica de criar listas) ---
quadrados       = [x ** 2 for x in range(1, 6)]        # [1, 4, 9, 16, 25]
pares           = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
maiusculas      = [s.upper() for s in lista_strings]


# -----------------------------------------------------------------------------
# 3. RECURSOS MAIS COMUNS
# -----------------------------------------------------------------------------

numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# ADICIONAR elementos
numeros.append(7)           # adiciona ao final              → [..., 7]
numeros.insert(0, 0)        # insere na posição 0            → [0, 3, 1, ...]
numeros.extend([8, 9, 10])  # adiciona múltiplos elementos ao final

# REMOVER elementos
numeros.remove(1)           # remove a PRIMEIRA ocorrência do valor 1
valor = numeros.pop()       # remove e retorna o último elemento
valor = numeros.pop(0)      # remove e retorna o elemento do índice 0
del numeros[2]              # remove o elemento do índice 2
numeros.clear()             # remove TODOS os elementos

# BUSCAR e CONTAR
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
posicao     = numeros.index(4)      # retorna o índice do valor 4  → 2
quantidade  = numeros.count(1)      # conta ocorrências do valor 1 → 2
existe      = 5 in numeros          # verifica se existe           → True

# ORDENAR
numeros.sort()                          # ordena in-place (modifica a lista)
numeros.sort(reverse=True)              # ordena em ordem decrescente
ordenada = sorted(numeros)              # retorna nova lista ordenada (original intacta)
numeros.reverse()                       # inverte a ordem in-place

# INFORMAÇÕES
tamanho     = len(numeros)          # quantidade de elementos
maior       = max(numeros)          # maior valor
menor       = min(numeros)          # menor valor
soma        = sum(numeros)          # soma de todos os valores

# COPIAR (evite usar lista2 = lista1, pois ambas apontarão para o mesmo objeto)
copia_rasa  = numeros.copy()        # cópia rasa (shallow copy)
copia_rasa  = numeros[:]            # equivalente ao .copy()

import copy
copia_profunda = copy.deepcopy(numeros) # use para listas aninhadas

# JUNTAR e REPETIR
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
juntas      = lista_a + lista_b     # [1, 2, 3, 4, 5, 6]
repetida    = lista_a * 3           # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# CONVERTER
lista_de_string     = list("python")        # ['p', 'y', 't', 'h', 'o', 'n']
lista_de_tupla      = list((1, 2, 3))       # [1, 2, 3]
lista_de_range      = list(range(5))        # [0, 1, 2, 3, 4]

# DESEMPACOTAR (unpacking)
a, b, c = [10, 20, 30]             # a=10, b=20, c=30
primeiro, *resto = [1, 2, 3, 4]   # primeiro=1, resto=[2, 3, 4]
*inicio, ultimo  = [1, 2, 3, 4]   # inicio=[1, 2, 3], ultimo=4

# ZIP — combina duas listas em pares
nomes   = ["Ana", "Bruno", "Carol"]
idades  = [28, 35, 22]
pares   = list(zip(nomes, idades))  # [("Ana", 28), ("Bruno", 35), ("Carol", 22)]

# MAP e FILTER
dobros      = list(map(lambda x: x * 2, [1, 2, 3]))        # [2, 4, 6]
maiores     = list(filter(lambda x: x > 3, [1, 2, 3, 4]))  # [4]

# ANY e ALL
algum_par   = any(x % 2 == 0 for x in [1, 3, 4])   # True
todos_pares = all(x % 2 == 0 for x in [2, 4, 6])   # True


# -----------------------------------------------------------------------------
# 4. MELHORES PRÁTICAS
# -----------------------------------------------------------------------------
#
#  ✔  Prefira List Comprehension ao invés de loops para criar listas simples.
#     Ruim:
#         quadrados = []
#         for x in range(10):
#             quadrados.append(x**2)
#     Bom:
#         quadrados = [x**2 for x in range(10)]
#
#  ✔  Use .copy() ou [:] ao copiar listas para evitar efeitos colaterais.
#     Ruim:   lista_b = lista_a          (ambas apontam para o mesmo objeto)
#     Bom:    lista_b = lista_a.copy()
#
#  ✔  Evite modificar uma lista enquanto itera sobre ela.
#     Ruim:
#         for item in lista:
#             if item < 0:
#                 lista.remove(item)   # comportamento imprevisível!
#     Bom:
#         lista = [item for item in lista if item >= 0]
#
#  ✔  Prefira 'in' para verificar existência em vez de usar .index() com try/except.
#     Bom:    if valor in lista:
#
#  ✔  Use nomes de variáveis no plural para deixar claro que é uma coleção.
#     Ruim:   numero = [1, 2, 3]
#     Bom:    numeros = [1, 2, 3]
#
#  ✔  Para grandes volumes de dados numéricos, considere usar o módulo array
#     ou a biblioteca NumPy, que são mais eficientes em memória e velocidade.


# -----------------------------------------------------------------------------
# 5. QUANDO USAR LISTAS
# -----------------------------------------------------------------------------
#
#  ✔  Quando a ordem dos elementos importa.
#  ✔  Quando você precisa adicionar, remover ou modificar elementos.
#  ✔  Quando os elementos podem se repetir (duplicatas são permitidas).
#  ✔  Para coleções pequenas a médias de dados heterogêneos.
#  ✔  Quando precisar iterar, filtrar ou transformar uma coleção de dados.
#  ✔  Para empilhar ou enfileirar dados de forma simples (com append/pop).
#
#  Exemplos práticos:
#       - Lista de tarefas (to-do list)
#       - Histórico de ações do usuário
#       - Resultado de uma consulta ao banco de dados
#       - Coleção de nomes, notas, preços etc.


# -----------------------------------------------------------------------------
# 6. QUANDO NÃO USAR LISTAS
# -----------------------------------------------------------------------------
#
#  ✘  Quando os dados NÃO devem ser alterados → use TUPLE ( )
#     Ex: coordenadas geográficas, configurações fixas, chaves compostas.
#
#  ✘  Quando precisar de busca rápida por chave → use DICT { }
#     Buscar em listas é O(n); dicionários fazem isso em O(1).
#     Ex: {"nome": "Ana", "idade": 28}
#
#  ✘  Quando precisar garantir elementos únicos → use SET { }
#     Ex: conjunto de tags, IDs únicos.
#
#  ✘  Para dados numéricos em grande volume com operações matemáticas
#     → use array (módulo array) ou numpy.array
#     Listas são mais lentas e consomem mais memória nesses casos.
#
#  ✘  Quando a ordem de inserção e remoção no início for frequente
#     → use collections.deque (mais eficiente que lista para esse caso).


# -----------------------------------------------------------------------------
# 7. RESUMO
# -----------------------------------------------------------------------------
#
#  Listas são uma das estruturas mais versáteis e usadas em Python.
#  São ideais para coleções mutáveis e ordenadas de elementos.
#
#  Pontos-chave para lembrar:
#
#   │ Característica     │ Lista [ ]      │
#   ├────────────────────┼────────────────┤
#   │ Mutável            │ ✔ Sim          │
#   │ Ordenada           │ ✔ Sim          │
#   │ Duplicatas         │ ✔ Permite      │
#   │ Tipos mistos       │ ✔ Permite      │
#   │ Indexação          │ ✔ Sim (base 0) │
#   │ Performance busca  │ O(n) — linear  │
#
#  Métodos essenciais:
#   append()  insert()  extend()  remove()  pop()
#   sort()    reverse() index()   count()   copy()
#   clear()   len()     in        sorted()
#
#  Sintaxes mais importantes:
#   lista[i]         → acesso por índice
#   lista[a:b]       → fatiamento
#   lista[::-1]      → inversão por fatiamento
#   [expr for x in iterável if condição]  → list comprehension
#
# =============================================================================