# =============================================================================
# ESTRUTURA DE REPETIÇÃO: while
# =============================================================================
# Linguagem : Python
# Tema      : Laço de repetição while
# Objetivo  : Guia simples, objetivo e fácil de entender sobre o uso do while
# =============================================================================


# -----------------------------------------------------------------------------
# 1. O QUE É?
# -----------------------------------------------------------------------------
#
# O "while" é uma estrutura de repetição que executa um bloco de código
# ENQUANTO uma condição for verdadeira (True).
#
# Diferente do "for" (que percorre uma sequência finita e conhecida),
# o "while" continua repetindo até que a condição se torne falsa (False)
# — ou até que seja interrompido manualmente.
#
# Em resumo: "Enquanto isso for verdade, continue fazendo isso."


# -----------------------------------------------------------------------------
# 2. SINTAXE DE USO
# -----------------------------------------------------------------------------
#
#   while <condição>:
#       <bloco de código a ser repetido>
#
# Exemplo básico:

contador = 0

while contador < 5:
    print(f"Contagem: {contador}")
    contador += 1

# Saída:
# Contagem: 0
# Contagem: 1
# Contagem: 2
# Contagem: 3
# Contagem: 4

# ⚠️  ATENÇÃO: Se a condição nunca se tornar False, o loop será infinito!


# -----------------------------------------------------------------------------
# 3. MELHORES PRÁTICAS
# -----------------------------------------------------------------------------
#
# ✅  Sempre garanta que a condição do while vai se tornar False em algum momento.
# ✅  Use uma variável de controle clara e com nome descritivo.
# ✅  Prefira "break" com moderação — abuse dele pode tornar o código confuso.
# ✅  Inicialize a variável de controle ANTES do loop.
# ✅  Atualize a variável de controle DENTRO do loop.
# ✅  Use comentários se a lógica de parada não for óbvia.
#
# ❌  Evite condições complexas e difíceis de ler no cabeçalho do while.
# ❌  Nunca esqueça de atualizar a variável de controle (causa loop infinito).
# ❌  Não use while quando o número de iterações já é conhecido — prefira for.


# -----------------------------------------------------------------------------
# 4. QUANDO USAR?
# -----------------------------------------------------------------------------
#
# ✔  Quando você NÃO sabe quantas vezes o loop vai repetir.
# ✔  Quando a repetição depende de uma entrada do usuário.
# ✔  Quando você espera por um evento ou condição externa (ex: conexão, resposta).
# ✔  Para criar menus interativos que continuam até o usuário sair.
# ✔  Para processar dados de forma contínua (streams, filas, sensores).

# Exemplo — aguardando entrada válida do usuário:
#
#   senha = ""
#   while senha != "1234":
#       senha = input("Digite a senha: ")
#   print("Acesso liberado!")


# -----------------------------------------------------------------------------
# 5. QUANDO NÃO USAR?
# -----------------------------------------------------------------------------
#
# ✘  Quando o número de iterações é fixo e conhecido → use "for".
# ✘  Quando você está percorrendo uma lista, tupla ou dicionário → use "for".
# ✘  Quando a lógica fica mais clara com "for" → prefira a legibilidade.
#
# Exemplo ruim com while (prefira for neste caso):
#
#   i = 0
#   while i < len(lista):        # ❌ desnecessariamente complexo
#       print(lista[i])
#       i += 1
#
# Exemplo correto com for:
#
#   for item in lista:           # ✅ mais simples e legível
#       print(item)


# -----------------------------------------------------------------------------
# 6. RECURSOS MAIS COMUNS DENTRO DO WHILE
# -----------------------------------------------------------------------------


# 6.1 — break
# Interrompe o loop imediatamente, independente da condição.

numero = 0
while True:                         # loop "infinito" controlado pelo break
    if numero == 3:
        break                       # para quando numero for 3
    print(f"numero = {numero}")
    numero += 1

# Saída: 0, 1, 2


# 6.2 — continue
# Pula para a próxima iteração, ignorando o restante do bloco atual.

i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue                    # ignora números pares
    print(i)

# Saída: 1, 3, 5


# 6.3 — else
# O bloco "else" é executado quando o loop termina normalmente
# (sem ser interrompido por um "break").

tentativas = 0
while tentativas < 3:
    print(f"Tentativa {tentativas + 1}")
    tentativas += 1
else:
    print("Loop encerrado normalmente.")

# Saída: Tentativa 1, Tentativa 2, Tentativa 3, Loop encerrado normalmente.


# 6.4 — while True (loop infinito intencional)
# Muito usado em menus, servidores, jogos e sistemas contínuos.

#   while True:
#       opcao = input("Escolha (0 para sair): ")
#       if opcao == "0":
#           break
#       print(f"Você escolheu: {opcao}")


# 6.5 — Variável de controle com flag (bandeira)
# Uma variável booleana usada para controlar quando o loop deve parar.

rodando = True
ciclos = 0

while rodando:
    ciclos += 1
    if ciclos >= 4:
        rodando = False             # "desliga" a flag para encerrar o loop

print(f"Total de ciclos: {ciclos}")

# Saída: Total de ciclos: 4


# 6.6 — while com múltiplas condições
# Você pode combinar condições usando "and" e "or".

x = 0
y = 10

while x < 5 and y > 5:
    print(f"x={x}, y={y}")
    x += 1
    y -= 1

# Saída: x=0,y=10 / x=1,y=9 / x=2,y=8 / x=3,y=7 / x=4,y=6


# -----------------------------------------------------------------------------
# 7. RESUMO
# -----------------------------------------------------------------------------
#
#  Conceito       | Descrição
#  ---------------|------------------------------------------------------------
#  while          | Repete enquanto a condição for True
#  break          | Interrompe o loop imediatamente
#  continue       | Pula para a próxima iteração
#  else           | Executa ao fim do loop (se não houve break)
#  while True     | Loop infinito — requer break para sair
#  flag booleana  | Variável de controle para encerrar o loop de forma limpa
#
#  REGRA DE OURO:
#  → Use "for"   quando souber quantas vezes vai repetir.
#  → Use "while" quando a repetição depender de uma condição dinâmica.
#
# =============================================================================