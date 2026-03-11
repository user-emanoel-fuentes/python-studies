# =============================================================================
#  ESTRUTURA DE REPETIÇÃO: for
# =============================================================================

# -----------------------------------------------------------------------------
#  O QUE É?
# -----------------------------------------------------------------------------
#
#  O "for" é uma estrutura de repetição (laço/loop) usada para percorrer
#  (iterar) sobre os elementos de uma sequência ou coleção de dados.
#
#  A cada ciclo do laço, uma variável recebe automaticamente o próximo
#  elemento da sequência, até que todos os elementos tenham sido visitados.
#
#  Sequências e coleções compatíveis:
#    - Strings        → cada caractere
#    - Listas         → cada item
#    - Tuplas         → cada item
#    - Dicionários    → cada chave (por padrão)
#    - Conjuntos      → cada elemento
#    - range()        → sequência numérica gerada automaticamente
#    - Qualquer objeto iterável


# -----------------------------------------------------------------------------
#  SINTAXE DE USO
# -----------------------------------------------------------------------------
#
#  Forma básica:
#
#    for <variavel> in <sequencia>:
#        <bloco de código>
#
#  Regras obrigatórias:
#    1. Os dois-pontos (:) ao final da linha do "for" são obrigatórios.
#    2. O bloco de código deve estar indentado (4 espaços é o padrão Python).
#
#  Exemplos:

# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
# Saída: maçã / banana / laranja

# Iterando com range() — sequência numérica
for numero in range(5):       # gera: 0, 1, 2, 3, 4
    print(numero)

for numero in range(1, 6):    # gera: 1, 2, 3, 4, 5
    print(numero)

for numero in range(0, 10, 2):  # gera: 0, 2, 4, 6, 8  (passo 2)
    print(numero)

# Iterando sobre uma string
for letra in "Python":
    print(letra)
# Saída: P / y / t / h / o / n

# Iterando sobre um dicionário
pessoa = {"nome": "Ana", "idade": 30, "cidade": "SP"}

for chave in pessoa:               # itera pelas chaves
    print(chave)

for valor in pessoa.values():      # itera pelos valores
    print(valor)

for chave, valor in pessoa.items():  # itera por chave e valor juntos
    print(f"{chave}: {valor}")

# Usando enumerate() — obtém índice e valor ao mesmo tempo
nomes = ["Carlos", "Beatriz", "Diego"]
for indice, nome in enumerate(nomes):
    print(f"{indice} - {nome}")
# Saída: 0 - Carlos / 1 - Beatriz / 2 - Diego

# Usando zip() — itera duas listas em paralelo
nomes   = ["Ana", "Bruno", "Clara"]
notas   = [9.5, 7.0, 8.3]
for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")

# Cláusula else no for — executada quando o loop termina normalmente
for i in range(3):
    print(i)
else:
    print("Loop concluído!")   # sempre executa, a menos que haja "break"


# -----------------------------------------------------------------------------
#  MELHORES PRÁTICAS
# -----------------------------------------------------------------------------
#
#  1. Nomeie bem a variável de iteração
#     Ruim  → for x in lista_de_usuarios:
#     Bom   → for usuario in lista_de_usuarios:
#
#  2. Prefira iterar diretamente sobre a coleção em vez de usar índices
#     Evite → for i in range(len(frutas)): print(frutas[i])
#     Use   → for fruta in frutas: print(fruta)
#
#  3. Use enumerate() quando precisar do índice
#     Evite → i = 0; for item in lista: print(i, item); i += 1
#     Use   → for i, item in enumerate(lista): print(i, item)
#
#  4. Use zip() para percorrer múltiplas listas juntas
#
#  5. Prefira list comprehension para criar listas simples (mais pythônico)
#     Evite →
#       quadrados = []
#       for n in range(5): quadrados.append(n ** 2)
#
#     Use   →
#       quadrados = [n ** 2 for n in range(5)]
#
#  6. Não modifique a coleção enquanto itera sobre ela
#     Isso pode causar comportamentos inesperados ou erros.
#     Se precisar remover itens, itere sobre uma cópia:
#       for item in lista.copy(): ...
#
#  7. Use "break" e "continue" com moderação — em excesso dificultam leitura.


# -----------------------------------------------------------------------------
#  QUANDO USAR
# -----------------------------------------------------------------------------
#
#  ✔ Quando você sabe quantas vezes (ou quais elementos) quer percorrer.
#  ✔ Quando precisa processar cada item de uma lista, tupla, string etc.
#  ✔ Quando quer acumular resultados (somas, contagens, novas listas).
#  ✔ Quando quer aplicar uma operação a todos os elementos de uma coleção.
#  ✔ Quando a quantidade de iterações é determinada pela sequência (não por
#    uma condição que pode nunca ser satisfeita).
#
#  Exemplos de cenários ideais:
#    - Percorrer registros de um banco de dados
#    - Processar linhas de um arquivo
#    - Calcular a soma ou média de uma lista de números
#    - Gerar uma nova lista com valores transformados


# -----------------------------------------------------------------------------
#  QUANDO NÃO USAR
# -----------------------------------------------------------------------------
#
#  ✘ Quando a repetição depende de uma condição que pode ser falsa desde
#    o início ou cujo fim é imprevisível → prefira o "while".
#
#  ✘ Quando você não tem uma sequência definida para iterar.
#    Exemplo: "repita até o usuário digitar 'sair'" → use while.
#
#  ✘ Quando a lógica de parada é complexa e muda a cada ciclo → while é
#    mais expressivo nesses casos.
#
#  ✘ Para loops infinitos → use while True.


# -----------------------------------------------------------------------------
#  RECURSOS MAIS COMUNS USADOS COM O "for"
# -----------------------------------------------------------------------------

# 1. range(inicio, fim, passo) — gera sequência numérica
for i in range(1, 11):          # 1 até 10
    print(i)

# 2. enumerate(sequencia) — retorna (índice, valor)
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

# 3. zip(seq1, seq2) — itera em paralelo
for a, b in zip([1, 2, 3], ["x", "y", "z"]):
    print(a, b)

# 4. break — interrompe o loop imediatamente
for n in range(10):
    if n == 5:
        break
    print(n)                    # imprime 0 a 4

# 5. continue — pula para a próxima iteração
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)                    # imprime apenas ímpares

# 6. List Comprehension — cria lista a partir de um for em uma linha
quadrados   = [x ** 2 for x in range(6)]          # [0, 1, 4, 9, 16, 25]
pares       = [x for x in range(20) if x % 2 == 0]

# 7. Dict Comprehension — cria dicionário com for em uma linha
quadrados_dict = {x: x ** 2 for x in range(5)}    # {0:0, 1:1, 2:4, ...}

# 8. sum() / max() / min() com for implícito (generator expression)
total = sum(x ** 2 for x in range(10))

# 9. sorted() e reversed() — iterar em ordem diferente
for item in sorted(["banana", "maçã", "abacaxi"]):
    print(item)

for item in reversed([1, 2, 3, 4, 5]):
    print(item)

# 10. Nested for (for aninhado) — loop dentro de loop
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()


# -----------------------------------------------------------------------------
#  RESUMO
# -----------------------------------------------------------------------------
#
#  O "for" é a estrutura de repetição mais usada em Python quando se tem
#  uma sequência definida para percorrer.
#
#  Pontos-chave para lembrar:
#
#  ┌─────────────────────────────────────────────────────────────────────┐
#  │  • Itera automaticamente sobre qualquer objeto iterável             │
#  │  • range() é o parceiro ideal para repetições numéricas             │
#  │  • enumerate() quando precisar do índice                            │
#  │  • zip() para percorrer múltiplas sequências em paralelo            │
#  │  • break interrompe, continue pula, else executa ao fim             │
#  │  • List/Dict comprehension = for compacto para criar coleções       │
#  │  • Não modifique a coleção durante a iteração                       │
#  │  • Use while quando a condição de parada for dinâmica/imprevisível  │
#  └─────────────────────────────────────────────────────────────────────┘
#
# =============================================================================