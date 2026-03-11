# =============================================================================
#                        CONDICIONAIS EM PYTHON
# =============================================================================
#
# Autor: Guia de Referência Python
# Tema : Estruturas Condicionais — conceitos, boas práticas e exemplos
#
# =============================================================================


# -----------------------------------------------------------------------------
# 1. O QUE SÃO CONDICIONAIS?
# -----------------------------------------------------------------------------
#
# Condicionais são estruturas de controle de fluxo que permitem ao programa
# tomar decisões com base em expressões booleanas (True ou False).
#
# Em Python, as estruturas condicionais são:
#   - if
#   - if / else
#   - if / elif / else
#   - Operador ternário (expressão condicional inline)
#   - match / case  (disponível a partir do Python 3.10)
#
# A sintaxe básica usa INDENTAÇÃO (4 espaços) para delimitar os blocos —
# não há chaves {} como em outras linguagens.
#
# Sintaxe geral:
#
#   if <condição>:
#       <bloco executado se a condição for True>
#   elif <outra condição>:
#       <bloco executado se a condição acima for True>
#   else:
#       <bloco executado se nenhuma condição anterior for True>


# -----------------------------------------------------------------------------
# 2. EXEMPLOS DE USO
# -----------------------------------------------------------------------------

# --- 2.1 if simples ---
temperatura = 35

if temperatura > 30:
    print("Está calor!")  # Executado pois 35 > 30 é True


# --- 2.2 if / else ---
saldo = -50

if saldo >= 0:
    print("Saldo positivo.")
else:
    print("Saldo negativo!")  # Executado


# --- 2.3 if / elif / else ---
nota = 75

if nota >= 90:
    conceito = "A"
elif nota >= 75:
    conceito = "B"   # Executado
elif nota >= 60:
    conceito = "C"
else:
    conceito = "F"
# Observação: Neste exemplo uma atenção é muito importante, pois a ordem das condições é crucial para o bom funcionamento do código.

print(f"Conceito: {conceito}")  # Conceito: B


# --- 2.4 Operador ternário (expressão condicional) ---
# Forma: <valor_se_true> if <condição> else <valor_se_false>

idade = 20
status = "maior de idade" if idade >= 18 else "menor de idade"
print(status)  # maior de idade


# --- 2.5 Condicionais com operadores lógicos (and, or, not) ---
usuario_logado = True
tem_permissao = False

if usuario_logado and not tem_permissao:
    print("Acesso negado: sem permissão.")  # Executado


# --- 2.6 Verificação de pertencimento com in ---
frutas = ["maçã", "banana", "uva"]

if "banana" in frutas:
    print("Banana está na lista!")  # Executado


# --- 2.7 Verificação de tipo com isinstance ---
valor = 3.14

if isinstance(valor, float):
    print(f"{valor} é um número de ponto flutuante.")  # Executado


# --- 2.8 match / case (Python 3.10+) ---
# Equivalente ao switch/case de outras linguagens, porém muito mais poderoso.

comando = "sair"

match comando:
    case "iniciar":
        print("Iniciando o sistema...")
    case "pausar":
        print("Sistema pausado.")
    case "sair":
        print("Encerrando o sistema.")   # Executado
    case _:
        print("Comando desconhecido.")   # Caso padrão (equivale ao else)


# --- 2.9 Condicional com valor nulo / vazio (Truthy e Falsy) ---
# Em Python, os seguintes valores são considerados False (Falsy):
#   None, 0, 0.0, "", [], {}, set(), ()

nome = ""

if nome:
    print(f"Olá, {nome}!")
else:
    print("Nome não informado.")  # Executado, pois "" é Falsy


# --- 2.10 Condicional em list comprehension ---
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]


# -----------------------------------------------------------------------------
# 3. QUANDO USAR CONDICIONAIS
# -----------------------------------------------------------------------------
#
# ✔ Validar entradas do usuário
#       ex: verificar se um campo está preenchido ou se um valor é válido
#
# ✔ Controlar fluxo de execução do programa
#       ex: decidir qual função chamar com base em um estado
#
# ✔ Tratar casos especiais ou erros de negócio
#       ex: verificar se um usuário tem saldo antes de uma transação
#
# ✔ Aplicar regras de negócio
#       ex: calcular desconto conforme o perfil do cliente
#
# ✔ Guardar código defensivo
#       ex: checar se um objeto não é None antes de acessar seus atributos
#
# ✔ Substituir pequenas funções com operador ternário
#       ex: label = "sim" if ativo else "não"


# -----------------------------------------------------------------------------
# 4. QUANDO NÃO USAR CONDICIONAIS
# -----------------------------------------------------------------------------
#
# ✘ Quando um dicionário de despacho (dispatch dict) é mais limpo
#       Evite longas cadeias de if/elif para mapear ações a funções.
#
#   RUIM:
#       if operacao == "soma":
#           resultado = a + b
#       elif operacao == "subtracao":
#           resultado = a - b
#       elif operacao == "multiplicacao":
#           resultado = a * b
#
#   BOM:
#       operacoes = {
#           "soma":          lambda a, b: a + b,
#           "subtracao":     lambda a, b: a - b,
#           "multiplicacao": lambda a, b: a * b,
#       }
#       resultado = operacoes[operacao](a, b)
#
# ✘ Quando polimorfismo resolve melhor (OOP)
#       Em vez de if isinstance(animal, Cachorro): latir()
#       prefira definir o método falar() em cada subclasse.
#
# ✘ Quando já existe uma função/método nativo
#       Evite: resultado = True if x > 0 else False
#       Use:   resultado = x > 0   (expressão já retorna bool)
#
# ✘ Para tratar exceções previsíveis
#       Prefira try/except em vez de if para lidar com erros de I/O,
#       conversões de tipo e acessos a recursos externos.
#
# ✘ Condicionais desnecessários com retorno booleano
#       RUIM:
#           def eh_par(n):
#               if n % 2 == 0:
#                   return True
#               else:
#                   return False
#       BOM:
#           def eh_par(n):
#               return n % 2 == 0


# -----------------------------------------------------------------------------
# 5. MELHORES PRÁTICAS
# -----------------------------------------------------------------------------
#
# 1. PREFIRA RETORNO ANTECIPADO (early return / guard clause)
#    Reduza o aninhamento retornando cedo em funções.
#
#    RUIM (aninhamento profundo):
#        def processar(usuario):
#            if usuario:
#                if usuario.ativo:
#                    if usuario.saldo > 0:
#                        realizar_operacao(usuario)
#
#    BOM (guard clauses):
#        def processar(usuario):
#            if not usuario:
#                return
#            if not usuario.ativo:
#                return
#            if usuario.saldo <= 0:
#                return
#            realizar_operacao(usuario)
#
#
# 2. EVITE NEGAÇÕES DUPLAS
#    RUIM: if not not ativo
#    BOM : if ativo
#
#
# 3. SIMPLIFIQUE COMPARAÇÕES COM BOOLEANOS
#    RUIM: if ativo == True
#    BOM : if ativo
#
#    RUIM: if ativo == False
#    BOM : if not ativo
#
#
# 4. USE "is" PARA COMPARAR COM None
#    RUIM: if valor == None
#    BOM : if valor is None
#    BOM : if valor is not None
#
#
# 5. MANTENHA CONDIÇÕES LEGÍVEIS
#    Se uma condição for complexa, extraia-a para uma variável com nome claro.
#
#    RUIM:
#        if user.age >= 18 and user.country == "BR" and not user.banned:
#
#    BOM:
#        eh_adulto         = user.age >= 18
#        eh_brasileiro     = user.country == "BR"
#        nao_esta_banido   = not user.banned
#        if eh_adulto and eh_brasileiro and nao_esta_banido:
#
#
# 6. NÃO ABUSE DO OPERADOR TERNÁRIO
#    Use apenas para expressões simples e de fácil leitura.
#    Para lógica complexa, prefira o if/else tradicional.
#
#
# 7. PREFIRA match/case PARA MÚLTIPLOS VALORES DISCRETOS (Python 3.10+)
#    É mais legível que longas cadeias de elif ao comparar um único valor.


# -----------------------------------------------------------------------------
# 6. RESUMO
# -----------------------------------------------------------------------------
#
#  Estrutura          | Uso principal
# --------------------|----------------------------------------------------
#  if                 | Executar bloco apenas se condição for verdadeira
#  if / else          | Escolher entre dois caminhos
#  if / elif / else   | Escolher entre múltiplos caminhos
#  Ternário           | Atribuição/expressão inline simples
#  match / case       | Comparação contra múltiplos valores discretos (3.10+)
#
#  Operadores úteis   | Descrição
# --------------------|----------------------------------------------------
#  and                | Ambas as condições devem ser True
#  or                 | Pelo menos uma condição deve ser True
#  not                | Inverte o valor booleano
#  in / not in        | Pertencimento em coleções
#  is / is not        | Identidade de objetos (ideal para None)
#  isinstance()       | Verifica o tipo de um objeto
#
#  Valores Falsy      | None, 0, 0.0, "", [], {}, set(), ()
#  Valores Truthy     | Qualquer valor que não seja Falsy
#
# Condicionais são fundamentais em qualquer programa Python. Dominar seu uso
# correto torna o código mais legível, eficiente e fácil de manter.
#
# =============================================================================