# =============================================================================
# TUPLAS EM PYTHON
# =============================================================================
# Descrição  : Guia simples, objetivo e completo sobre Tuplas em Python
# Linguagem  : Python 3.x
# =============================================================================


# -----------------------------------------------------------------------------
# 1. O QUE É
# -----------------------------------------------------------------------------
#
# Tupla é uma estrutura de dados nativa do Python usada para armazenar uma
# coleção ordenada de elementos. Ela é muito parecida com uma lista, porém com
# uma diferença fundamental: é IMUTÁVEL, ou seja, após criada, seus elementos
# não podem ser alterados, adicionados ou removidos.
#
# Características principais:
#   - Ordenada        → os elementos mantêm a ordem de inserção
#   - Imutável        → não permite alteração após a criação
#   - Permite duplicatas → pode conter valores repetidos
#   - Indexada        → acesso por índice (começa em 0)
#   - Heterogênea     → pode misturar tipos diferentes (int, str, bool, etc.)


# -----------------------------------------------------------------------------
# 2. SINTAXE DE USO
# -----------------------------------------------------------------------------

# Criando tuplas
tupla_vazia = ()
tupla_simples = (1, 2, 3)
tupla_sem_parenteses = 1, 2, 3          # Parênteses são opcionais
tupla_mista = (1, "texto", True, 3.14)
tupla_unitaria = (42,)                  # IMPORTANTE: vírgula obrigatória para 1 elemento

# Acessando elementos por índice
frutas = ("maçã", "banana", "laranja", "uva")

primeiro = frutas[0]        # "maçã"
ultimo = frutas[-1]         # "uva"  (índice negativo = começa do fim)

# Fatiamento (slicing)
alguns = frutas[1:3]        # ("banana", "laranja")
invertida = frutas[::-1]    # ("uva", "laranja", "banana", "maçã")

# Desempacotamento (unpacking)
a, b, c, d = frutas
print(a)  # "maçã"
print(d)  # "uva"

# Desempacotamento parcial com *
primeiro, *resto = frutas
print(primeiro)  # "maçã"
print(resto)     # ["banana", "laranja", "uva"]

# Iterando sobre uma tupla
for fruta in frutas:
    print(fruta)

# Verificando existência de elemento
print("banana" in frutas)   # True
print("melão" in frutas)    # False

# Concatenando tuplas
numeros = (1, 2, 3) + (4, 5, 6)    # (1, 2, 3, 4, 5, 6)

# Repetindo tupla
repetida = (0,) * 4                  # (0, 0, 0, 0)

# Convertendo entre lista e tupla
lista = [1, 2, 3]
tupla_da_lista = tuple(lista)        # (1, 2, 3)
lista_da_tupla = list(tupla_simples) # [1, 2, 3]


# -----------------------------------------------------------------------------
# 3. RECURSOS MAIS COMUNS
# -----------------------------------------------------------------------------

coordenadas = (10, 85, 42, 10, 33)

# .count(valor) → conta quantas vezes um valor aparece
print(coordenadas.count(10))    # 2

# .index(valor) → retorna o índice da primeira ocorrência
print(coordenadas.index(85))    # 1

# len() → retorna o número de elementos
print(len(coordenadas))         # 5

# min() / max() → menor e maior valor (elementos devem ser comparáveis)
print(min(coordenadas))         # 10
print(max(coordenadas))         # 85

# sum() → soma dos elementos numéricos
print(sum(coordenadas))         # 180

# sorted() → retorna uma LISTA ordenada (não modifica a tupla original)
print(sorted(coordenadas))      # [10, 10, 33, 42, 85]

# enumerate() → retorna índice + valor durante iteração
for indice, valor in enumerate(coordenadas):
    print(f"[{indice}] → {valor}")

# zip() → combina duas tuplas elemento a elemento
nomes = ("Ana", "Bruno", "Carlos")
idades = (28, 34, 22)
pessoas = tuple(zip(nomes, idades))
print(pessoas)  # (("Ana", 28), ("Bruno", 34), ("Carlos", 22))

# Tupla como chave de dicionário (listas não podem ser chaves!)
localizacoes = {
    (0, 0): "origem",
    (1, 5): "ponto A",
    (3, 2): "ponto B",
}


# -----------------------------------------------------------------------------
# 4. MELHORES PRÁTICAS
# -----------------------------------------------------------------------------
#
# ✔ Use tuplas para dados que NÃO devem ser alterados (coordenadas, configs,
#   datas, constantes).
#
# ✔ Prefira tuplas a listas quando quiser sinalizar para outros
#   desenvolvedores que aquela coleção é "somente leitura".
#
# ✔ Nomeie bem suas variáveis para deixar claro o que cada posição representa,
#   ou use namedtuple para clareza extra.
#
# ✔ Use desempacotamento ao invés de acessar por índice quando possível:
#       x, y = ponto              → mais legível
#       x = ponto[0]             → menos legível
#
# ✔ Lembre-se da vírgula ao criar tuplas de um único elemento:
#       correto   → (42,)
#       errado    → (42)    ← isso é apenas um inteiro entre parênteses!
#
# ✔ Use namedtuple para tuplas com muitos campos e semântica importante:

from collections import namedtuple

Ponto = namedtuple("Ponto", ["x", "y"])
p = Ponto(x=3, y=7)
print(p.x)  # 3  → muito mais legível que p[0]


# -----------------------------------------------------------------------------
# 5. QUANDO USAR
# -----------------------------------------------------------------------------
#
# ✅ Dados constantes e imutáveis
#       DIAS_SEMANA = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom")
#
# ✅ Retorno de múltiplos valores em funções

def calcular(a, b):
    return a + b, a - b, a * b   # retorna uma tupla automaticamente

soma, diferenca, produto = calcular(10, 3)

# ✅ Chave de dicionário (listas não são hashable)
#       mapa[(linha, coluna)] = valor
#
# ✅ Dados estruturados e pequenos (coordenadas, RGB, pares chave-valor)
#       ponto = (x, y)
#       cor = (255, 128, 0)
#
# ✅ Quando performance importa: tuplas são ligeiramente mais rápidas
#   que listas para iteração e acesso, e usam menos memória.


# -----------------------------------------------------------------------------
# 6. QUANDO NÃO USAR
# -----------------------------------------------------------------------------
#
# ❌ Quando você precisar adicionar, remover ou alterar elementos
#       → Use list em vez disso
#
# ❌ Coleções grandes e dinâmicas que mudam com frequência
#       → Use list ou outras estruturas mutáveis
#
# ❌ Quando precisar de métodos como .append(), .remove(), .sort(), etc.
#       → Esses métodos não existem em tuplas
#
# ❌ Quando a semântica for de "coleção de itens similares e variáveis"
#       → Por convenção, listas são mais adequadas para isso


# -----------------------------------------------------------------------------
# 7. RESUMO
# -----------------------------------------------------------------------------
#
#  Tupla é...         Uma sequência ORDENADA e IMUTÁVEL de elementos.
#
#  Sintaxe            (a, b, c) ou a, b, c
#
#  Imutável?          Sim. Não dá para alterar após criada.
#
#  Permite repetidos? Sim.
#
#  Indexada?          Sim. Começa no índice 0.
#
#  Métodos            Apenas .count() e .index()
#
#  Use quando...      Os dados não devem mudar, precisa retornar múltiplos
#                     valores, usar como chave de dicionário, ou quer
#                     sinalizar imutabilidade ao time.
#
#  Não use quando...  Precisa modificar a coleção dinamicamente.
#
#  Dica de ouro       Uma tupla com 1 elemento PRECISA de vírgula: (42,)
#                     Sem a vírgula, Python interpreta como expressão, não tupla.
#
# =============================================================================