# =============================================================================
#  🐍  PYTHON NA PRÁTICA
#  Formatação de Strings e Conversão de Tipos
# =============================================================================
#
#  O que você vai aprender neste arquivo:
#    • Como usar .format() para montar textos dinâmicos
#    • Como usar f-strings (a forma moderna e recomendada)
#    • Como converter dados entre tipos (int, float, str, bool)
#    • Quando usar cada recurso — e quando evitá-los
#    • Exemplos práticos e comparações lado a lado
#
# =============================================================================


# =============================================================================
#  PARTE 1 — O MÉTODO .format()
# =============================================================================
#
#  O que é o .format()?
#  ---------------------
#  É um método da classe str que permite inserir valores dentro de uma string
#  usando chaves {} como marcadores de posição.
#
#  Você escreve um texto com "buracos" marcados por {} e depois "preenche"
#  esses buracos com os valores que você quer inserir.
#
#  Sintaxe básica:
#    "texto {} mais texto".format(valor)
#

# --- Exemplo simples ---
nome = "Ana"
mensagem = "Olá, {}!".format(nome)
print(mensagem)  # Saída: Olá, Ana!


# 1.1  Posicionamento por ordem (índice)
# --------------------------------------
# Você pode usar números dentro das chaves para controlar a ordem dos valores.

# Sem índice — preenche em ordem
print("Nome: {}, Idade: {}".format("Carlos", 25))
# Saída: Nome: Carlos, Idade: 25

# Com índice — controla a ordem manualmente
print("{1} tem {0} anos".format(25, "Carlos"))
# Saída: Carlos tem 25 anos

# Reutilizando o mesmo valor
print("{0} + {0} = {1}".format(5, 10))
# Saída: 5 + 5 = 10


# 1.2  Posicionamento por nome (keyword)
# ---------------------------------------
# Você pode nomear cada marcador para deixar o código mais legível.

produto = "Notebook"
preco = 3500.99
estoque = 7

texto = "Produto: {nome} | Preço: R$ {valor:.2f} | Estoque: {qtd}".format(
    nome=produto,
    valor=preco,
    qtd=estoque
)
print(texto)
# Saída: Produto: Notebook | Preço: R$ 3500.99 | Estoque: 7


# 1.3  Formatação de números
# ---------------------------
# O .format() tem uma mini-linguagem para formatar números com precisão.

pi = 3.14159265

# Casas decimais
print("Pi = {:.2f}".format(pi))    # Pi = 3.14
print("Pi = {:.4f}".format(pi))    # Pi = 3.1416

# Largura mínima (padding)
print("{:10}".format("oi"))        # "oi        "  (espaços à direita)
print("{:>10}".format("oi"))       # "        oi"  (alinha à direita)
print("{:^10}".format("oi"))       # "    oi    "  (centraliza)

# Separador de milhar
print("{:,}".format(1_000_000))    # 1,000,000

# Zeros à esquerda
print("{:05d}".format(42))         # 00042


# ✔  Quando usar .format():
#    - Python 2 ou versões antigas (< 3.6)
#    - Templates reutilizáveis armazenados em variáveis
#    - Strings carregadas de banco de dados ou arquivos de configuração
#    - Quando a string é montada fora do código (ex: traduções)
#
# ✘  Quando NÃO preferir .format():
#    - Quando você já usa Python 3.6+ e a string é simples (prefira f-strings)
#    - Quando o código fica confuso com muitos índices numéricos ({0}{1}{2}...)


# =============================================================================
#  PARTE 2 — F-STRINGS (Formatted String Literals)
# =============================================================================
#
#  O que é uma f-string?
#  ----------------------
#  Uma f-string é uma string prefixada com a letra f (ou F) que permite
#  inserir expressões Python diretamente dentro das chaves {}.
#  O Python avalia essas expressões em tempo de execução.
#
#  Diferença fundamental:
#    Com .format() → você passa os valores DEPOIS da string.
#    Com f-strings  → você escreve as expressões DENTRO da string.
#
#  Sintaxe: f"texto {expressão} texto"
#

# --- Exemplo simples ---
nome = "Lucas"
idade = 28
print(f"Olá, {nome}! Você tem {idade} anos.")
# Saída: Olá, Lucas! Você tem 28 anos.

# Comparação com .format() (equivalente, mas mais verboso):
print("Olá, {}! Você tem {} anos.".format(nome, idade))


# 2.1  Expressões dentro da string
# ---------------------------------
# Você pode colocar qualquer expressão Python válida dentro das chaves.

a = 10
b = 3

# Operações matemáticas
print(f"{a} + {b} = {a + b}")               # 10 + 3 = 13
print(f"{a} dividido por {b} = {a/b:.2f}")  # 10 dividido por 3 = 3.33

# Chamadas de métodos
nome = "  ana silva  "
print(f"Nome: {nome.strip().title()}")      # Nome: Ana Silva

# Condição inline (operador ternário)
saldo = -50
print(f"Status: {'positivo' if saldo >= 0 else 'negativo'}")
# Saída: Status: negativo

# Funções
numeros = [3, 1, 4, 1, 5]
print(f"Maior número: {max(numeros)}")      # Maior número: 5


# 2.2  Formatação de números (igual ao .format())
# ------------------------------------------------

preco = 1299.9
percentual = 0.175
codigo = 42

print(f"Preço: R$ {preco:.2f}")             # Preço: R$ 1299.90
print(f"Desconto: {percentual:.1%}")        # Desconto: 17.5%
print(f"Vendas: {1_500_000:,}")             # Vendas: 1,500,000
print(f"Código: {codigo:05d}")              # Código: 00042
print(f"Valor: {0.00042:.2e}")              # Valor: 4.20e-04


# 2.3  Debug com f-strings (Python 3.8+)
# ----------------------------------------
# O sinal = depois da variável mostra o nome E o valor — ótimo para debugging!

x = 42
lista = [1, 2, 3]

print(f"{x=}")          # x=42
print(f"{lista=}")      # lista=[1, 2, 3]
print(f"{x * 2=}")      # x * 2=84


# 2.4  F-strings multilinha
# --------------------------

nome = "Maria"
produto_comprado = "Smartphone"
preco_final = 2499.90

recibo = (
    f"===== RECIBO =====\n"
    f"Cliente: {nome}\n"
    f"Produto: {produto_comprado}\n"
    f"Total:   R$ {preco_final:.2f}\n"
    f"=================="
)
print(recibo)


# ✔  Quando usar f-strings:
#    - Sempre que possível no Python 3.6+
#    - Strings simples com variáveis locais
#    - Quando precisar de expressões e cálculos inline
#    - Para debugging rápido com {variavel=}
#
# ✘  Quando NÃO usar f-strings:
#    - Em templates armazenados em banco de dados
#      (a string seria avaliada agora, não depois)
#    - Com entrada direta de usuários desconhecidos (risco de injeção)
#    - Em Python < 3.6 (não existe nessa versão)


# =============================================================================
#  PARTE 3 — CONVERSÃO DE TIPOS DE DADOS (Type Casting)
# =============================================================================
#
#  Por que converter tipos?
#  -------------------------
#  Em Python, cada dado tem um tipo: inteiro, decimal, texto, booleano, etc.
#  Às vezes é preciso converter um tipo em outro.
#
#  Situações comuns:
#    • O usuário digita algo com input() — que SEMPRE retorna str
#    • Você precisa fazer cálculos com um número que está como string
#    • Precisa mostrar um número como parte de um texto
#
#  Problema clássico:
#
#    numero = input("Digite um número: ")  # usuário digita "5"
#    print(numero + 3)   # TypeError! não dá para somar str + int
#
#    Solução:
#    numero = int(input("Digite um número: "))
#    print(numero + 3)   # Agora funciona! Saída: 8


# 3.1  int() — Converter para inteiro
# ------------------------------------

# De string para int
print(int("42"))            # 42
print(int("100"))           # 100

# De float para int — TRUNCA (não arredonda!)
print(int(3.9))             # 3  ← cuidado! não vira 4
print(int(3.1))             # 3
print(int(-2.8))            # -2

# De bool para int
print(int(True))            # 1
print(int(False))           # 0

# Bases numéricas
print(int("FF", 16))        # 255  (hexadecimal)
print(int("1010", 2))       # 10   (binário)

# ⚠️  Cuidados com int():
#   int("3.5")  → ValueError!  Use int(float("3.5")) → 3
#   int("abc")  → ValueError!
#   int(None)   → TypeError!


# 3.2  float() — Converter para decimal
# ----------------------------------------

# De string para float
print(float("3.14"))        # 3.14
print(float("100"))         # 100.0

# De int para float
print(float(5))             # 5.0

# De bool para float
print(float(True))          # 1.0
print(float(False))         # 0.0

# ⚠️  Cuidado: usa ponto, não vírgula!
#   float("3,14")  → ValueError — use "3.14"


# 3.3  str() — Converter para texto
# -----------------------------------

# Praticamente qualquer coisa vira string
print(str(42))              # "42"
print(str(3.14))            # "3.14"
print(str(True))            # "True"
print(str(None))            # "None"
print(str([1, 2, 3]))       # "[1, 2, 3]"

# Uso prático: concatenar número em texto
idade = 25
mensagem = "Idade: " + str(idade)
print(mensagem)             # Idade: 25

# Com f-string você não precisa converter:
mensagem = f"Idade: {idade}"  # mais elegante, mesmo resultado


# 3.4  bool() — Converter para booleano
# ----------------------------------------
# bool() segue a regra "truthy/falsy":
# todo valor em Python pode ser interpretado como True ou False.

# Valores que viram False (falsy):
print(bool(0))              # False
print(bool(0.0))            # False
print(bool(""))             # False — string vazia
print(bool([]))             # False — lista vazia
print(bool(None))           # False

# Valores que viram True (truthy):
print(bool(1))              # True
print(bool(-99))            # True — qualquer número ≠ 0
print(bool("oi"))           # True — string não vazia
print(bool([0]))            # True — lista com qualquer conteúdo


# 3.5  list(), tuple(), set() — Converter coleções
# --------------------------------------------------

# String para lista de caracteres
print(list("Python"))           # ['P', 'y', 't', 'h', 'o', 'n']

# Lista para tupla (imutável)
lista = [1, 2, 3]
tupla = tuple(lista)            # (1, 2, 3)

# Lista para set (remove duplicatas)
numeros_repetidos = [1, 2, 2, 3, 3, 3]
unicos = set(numeros_repetidos) # {1, 2, 3}

# Prático: remover duplicatas e ordenar
sem_duplicatas = sorted(set(numeros_repetidos))  # [1, 2, 3]


# 3.6  Conversão segura com tratamento de erros
# -----------------------------------------------
# A conversão pode falhar se o dado não for compatível.
# Use try/except para tratar isso de forma segura.

def para_inteiro(valor):
    """Converte para int com segurança."""
    try:
        return int(valor)
    except ValueError:
        print(f'Erro: "{valor}" não pode ser convertido para inteiro.')
        return None
    except TypeError:
        print(f"Erro: tipo inválido ({type(valor).__name__}).")
        return None

print(para_inteiro("42"))       # 42
print(para_inteiro("abc"))      # Erro: "abc" não pode ser convertido...
print(para_inteiro(None))       # Erro: tipo inválido...


# Verificar antes de converter
valor = "123"

if valor.isdigit():
    numero = int(valor)
    print(f"{valor} é um número: {numero}")
else:
    print(f"{valor} não é um número inteiro válido")

# Para floats, use uma função auxiliar:
def eh_numero(texto):
    try:
        float(texto)
        return True
    except ValueError:
        return False

print(eh_numero("3.14"))        # True
print(eh_numero("abc"))         # False


# =============================================================================
#  PARTE 4 — EXEMPLOS COMPLETOS
# =============================================================================

# 4.1  Sistema de cadastro de alunos
# ------------------------------------
# Exemplo que usa os três recursos juntos.

def cadastrar_aluno():
    """Cadastra um aluno e exibe um boletim formatado."""

    # Leitura com conversão de tipo
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    # Cálculos
    media = (nota1 + nota2 + nota3) / 3
    aprovado = media >= 6.0

    # Exibição com f-string
    print(f"""
    ╔══════════════════════════╗
    ║      BOLETIM ESCOLAR     ║
    ╚══════════════════════════╝
    Aluno:  {nome.upper()}
    Nota 1: {nota1:.1f}
    Nota 2: {nota2:.1f}
    Nota 3: {nota3:.1f}
    Média:  {media:.2f}
    Status: {"✅ APROVADO" if aprovado else "❌ REPROVADO"}
    """)

# Descomente para executar:
# cadastrar_aluno()


# 4.2  Relatório financeiro com template reutilizável
# -----------------------------------------------------
# Exemplo de uso do .format() com template — ideal para strings dinâmicas.

template_relatorio = """
RELATÓRIO FINANCEIRO — {mes}/{ano}
{"=" * 40}
Receita bruta:   R$ {receita:>12,.2f}
Despesas:        R$ {despesas:>12,.2f}
Lucro líquido:   R$ {lucro:>12,.2f}
Margem:          {margem:>11.1%}
{"=" * 40}
"""

dados = {
    "mes": "Março",
    "ano": 2024,
    "receita": 125_000.50,
    "despesas": 87_340.20,
}
dados["lucro"] = dados["receita"] - dados["despesas"]
dados["margem"] = dados["lucro"] / dados["receita"]

print(template_relatorio.format(**dados))


# =============================================================================
#  RESUMO — QUANDO USAR CADA RECURSO
# =============================================================================
#
#  Recurso   │ Use quando...                        │ Evite quando...
#  ──────────┼──────────────────────────────────────┼─────────────────────────
#  .format() │ Templates reutilizáveis, configs,    │ Strings simples no
#             │ strings carregadas de fora do código │ código (use f-string)
#  ──────────┼──────────────────────────────────────┼─────────────────────────
#  f-string  │ Strings com variáveis locais,        │ Templates em banco de
#             │ expressões inline, debug com =       │ dados, entradas externas
#  ──────────┼──────────────────────────────────────┼─────────────────────────
#  int()     │ Converter input() numérico,          │ Strings com ponto
#             │ calcular com strings de números      │ decimal (use float())
#  ──────────┼──────────────────────────────────────┼─────────────────────────
#  float()   │ Cálculos com decimais,               │ Strings com vírgula
#             │ converter input() de decimais        │ (troque por ponto antes)
#  ──────────┼──────────────────────────────────────┼─────────────────────────
#  str()     │ Concatenar números em textos         │ Dentro de f-strings
#             │ sem usar f-string                    │ (desnecessário)
#  ──────────┼──────────────────────────────────────┼─────────────────────────
#  bool()    │ Verificar "vazio vs preenchido",     │ Comparações explícitas
#             │ valores 0 vs não-zero                │ onde True/False é óbvio
#
# =============================================================================
#  Bons estudos! 🐍
# =============================================================================