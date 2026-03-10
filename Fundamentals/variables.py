# =============================================================================
# VARIÁVEIS EM PYTHON
# Fundamentos da Linguagem
# =============================================================================

# -----------------------------------------------------------------------------
# 1. O QUE SÃO VARIÁVEIS NA PROGRAMAÇÃO?
# -----------------------------------------------------------------------------

# Uma variável é um espaço reservado na memória do computador usado para
# armazenar um valor. Pense nela como uma caixa com um rótulo: o rótulo é
# o nome da variável e o conteúdo da caixa é o valor armazenado.

# Esse valor pode ser lido, usado em cálculos, comparado com outros valores
# ou substituído por um novo valor ao longo da execução do programa.

# Em toda linguagem de programação, variáveis são fundamentais porque
# permitem que o programa "lembre" de informações enquanto está rodando.


# -----------------------------------------------------------------------------
# 2. O QUE SÃO VARIÁVEIS EM PYTHON?
# -----------------------------------------------------------------------------

# Em Python, variáveis são rótulos que apontam para objetos na memória.
# Diferente de outras linguagens (como C ou Java), em Python:
#
#   - Você NÃO precisa declarar o tipo da variável antes de usá-la.
#   - O tipo é definido automaticamente pelo valor atribuído.
#   - Uma mesma variável pode armazenar tipos diferentes ao longo do código.
#
# Isso é chamado de tipagem dinâmica.

nome = "Ana"        # string
idade = 25          # inteiro (int)
altura = 1.68       # decimal (float)
ativo = True        # booleano (bool)

# Python identifica o tipo de cada variável automaticamente.
# Para confirmar o tipo de uma variável, use a função type():

print(type(nome))    # <class 'str'>
print(type(idade))   # <class 'int'>
print(type(altura))  # <class 'float'>
print(type(ativo))   # <class 'bool'>

# observação: o recurso type() é útil para depuração, pois ajuda a entender o tipo de dados que uma variável está armazenando.


# -----------------------------------------------------------------------------
# 3. COMO DECLARAR UMA VARIÁVEL
# -----------------------------------------------------------------------------

# A sintaxe é simples:
#
#   nome_da_variavel = valor
#
# O símbolo = é o operador de atribuição. Ele diz:
# "guarde este valor neste nome".

cidade = "São Paulo"
preco = 49.90
quantidade = 3
disponivel = True

# Você também pode atribuir o mesmo valor a várias variáveis de uma vez:

x = y = z = 0

# Ou atribuir múltiplos valores a múltiplas variáveis em uma única linha:

largura, altura_retangulo, profundidade = 10, 5, 3


# -----------------------------------------------------------------------------
# 4. PADRÕES PARA NOMEAR VARIÁVEIS
# -----------------------------------------------------------------------------

# Python segue a convenção PEP 8 (guia oficial de estilo do Python).
# Siga esses padrões para escrever código limpo e legível.

# ✅ snake_case — padrão recomendado para variáveis e funções em Python
#    Palavras separadas por underscore (_), tudo em minúsculo.

nome_completo = "Carlos Silva"
data_de_nascimento = "10/04/1990"
total_de_itens = 42
preco_unitario = 9.99

# ✅ Nomes descritivos — o nome deve deixar claro o que a variável representa.

# Bom:
salario_mensal = 3500.00
quantidade_de_alunos = 30

# Ruim (não deixa claro o que representa):
s = 3500.00
q = 30

# ✅ SCREAMING_SNAKE_CASE — usado para constantes (valores que não mudam).

TAXA_DE_JUROS = 0.05
LIMITE_DE_TENTATIVAS = 3
PI = 3.14159

# ✅ Nomes de classes usam PascalCase, mas isso não se aplica a variáveis.


# -----------------------------------------------------------------------------
# 5. O QUE NÃO FAZER AO DECLARAR VARIÁVEIS
# -----------------------------------------------------------------------------

# ❌ Não use palavras reservadas do Python como nome de variável.
#    Palavras reservadas têm significado especial na linguagem.

# Exemplos de palavras reservadas (não use como nomes):
# if, else, elif, for, while, def, class, return, import,
# True, False, None, and, or, not, in, is, pass, break, continue...

# Errado — causará erro de sintaxe:
# for = 10
# if = "sim"

# ❌ Não comece nomes com números.

# Errado:
# 1produto = "caneta"

# Correto:
produto_1 = "caneta"

# ❌ Não use espaços no nome da variável.

# Errado:
# meu produto = "caderno"

# Correto:
meu_produto = "caderno"

# ❌ Não use caracteres especiais (exceto underscore _).

# Errado:
# preço = 10.0      (acento — evite em nomes de variáveis)
# total$ = 50       (símbolo especial)
# dado-extra = 7    (hífen não é permitido)

# Correto:
preco = 10.0
total = 50
dado_extra = 7

# ❌ Não use nomes genéricos demais que não dizem nada sobre o conteúdo.

# Ruim:
a = "João"
b = 28
c = True

# Bom:
nome_usuario = "João"
idade_usuario = 28
usuario_ativo = True

# ❌ Não reutilize uma variável para guardar coisas completamente diferentes
#    no mesmo bloco de código. Isso confunde quem lê o código.

# Ruim:
valor = 100
# ... muitas linhas depois ...
valor = "mensagem de erro"  # agora é string? Confuso.


# -----------------------------------------------------------------------------
# 6. QUANDO USAR VARIÁVEIS
# -----------------------------------------------------------------------------

# ✅ Use variáveis quando precisar guardar um valor para usar mais de uma vez.

raio = 7
area = 3.14159 * raio ** 2
circunferencia = 2 * 3.14159 * raio

print(f"Área: {area:.2f}")
print(f"Circunferência: {circunferencia:.2f}")

# ✅ Use variáveis para tornar o código mais legível.

# Sem variável — difícil de entender:
print(3600 * 24 * 7)

# Com variável — imediatamente claro:
segundos_por_hora = 3600
horas_por_dia = 24
dias_por_semana = 7
segundos_por_semana = segundos_por_hora * horas_por_dia * dias_por_semana
print(segundos_por_semana)

# ✅ Use variáveis para armazenar entradas do usuário.

# nome = input("Qual é o seu nome? ")
# print(f"Olá, {nome}!")

# ✅ Use constantes (MAIÚSCULAS) para valores fixos que se repetem no código.

DESCONTO = 0.10
preco_original = 200.00
preco_final = preco_original * (1 - DESCONTO)
print(f"Preço final: R$ {preco_final:.2f}")

# ✅ Use variáveis intermediárias para quebrar cálculos complexos em etapas.

salario_bruto = 5000.00
inss = salario_bruto * 0.11
irrf = salario_bruto * 0.075
salario_liquido = salario_bruto - inss - irrf
print(f"Salário líquido: R$ {salario_liquido:.2f}")


# -----------------------------------------------------------------------------
# 7. QUANDO NÃO USAR (OU EVITAR) VARIÁVEIS
# -----------------------------------------------------------------------------

# ❌ Evite criar variáveis desnecessárias para valores usados uma única vez
#    em contextos simples e óbvios.

# Desnecessário:
resultado_da_soma = 2 + 2
print(resultado_da_soma)

# Mais direto:
print(2 + 2)

# ❌ Evite variáveis que vivem pouco e tornam o código mais longo sem ganho.

# Desnecessário:
mensagem_de_boas_vindas = "Bem-vindo!"
print(mensagem_de_boas_vindas)

# Mais direto:
print("Bem-vindo!")

# ❌ Não crie variáveis que nunca são usadas. Isso polui o código
#    e pode indicar lógica incompleta ou esquecida.

# Ruim — 'aux' foi criada mas nunca usada:
total_pedido = 150.00
aux = total_pedido * 0.05  # nunca usada


# -----------------------------------------------------------------------------
# 8. RESUMO RÁPIDO
# -----------------------------------------------------------------------------

# | Conceito               | Resumo                                          |
# |------------------------|-------------------------------------------------|
# | O que é               | Espaço na memória com um nome para guardar valor |
# | Tipagem               | Dinâmica — o tipo é definido pelo valor          |
# | Sintaxe               | nome = valor                                    |
# | Padrão de nome        | snake_case (ex: nome_completo)                  |
# | Constantes            | SCREAMING_SNAKE_CASE (ex: TAXA_JUROS)           |
# | Não usar              | Palavras reservadas, acentos, espaços, números  |
# | Quando usar           | Reutilização, legibilidade, entradas, cálculos  |
# | Quando evitar         | Valores únicos simples, variáveis nunca usadas  |