# =============================================================================
# TEMA: SET (Conjunto) em Python
# =============================================================================
# Arquivo de referência técnica — estudo e consulta rápida
# Cobertura: definição, sintaxe, boas práticas, casos de uso e resumo
# =============================================================================


# -----------------------------------------------------------------------------
# 1. O QUE É UM SET?
# -----------------------------------------------------------------------------
#
# Um SET (conjunto) é uma estrutura de dados nativa do Python que armazena
# uma coleção de elementos:
#
#   ✔ DESORDENADA     — os itens não possuem posição/índice definido
#   ✔ SEM DUPLICATAS  — cada valor aparece no máximo uma única vez
#   ✔ MUTÁVEL         — é possível adicionar e remover elementos após a criação
#   ✔ ITERÁVEL        — pode ser percorrido com loops
#
# Internamente, o set usa uma tabela hash (como dict), o que garante:
#   • Verificação de pertencimento em O(1) — extremamente rápido
#   • Operações matemáticas de conjunto (união, interseção, diferença etc.)
#
# IMPORTANTE: os elementos de um set precisam ser HASHABLE (imutáveis),
# ou seja: strings, números, tuplas são aceitos. Listas e dicts NÃO podem
# ser elementos de um set.
#
# Tipo Python: <class 'set'>
# Tipo imutável equivalente: frozenset


# -----------------------------------------------------------------------------
# 2. SINTAXE DE USO
# -----------------------------------------------------------------------------

# --- 2.1 CRIAÇÃO ---

# Com chaves (literal)
frutas = {"maçã", "banana", "laranja"}

# Com o construtor set()
numeros = set([1, 2, 3, 4, 5])

# A partir de uma string (cada caractere vira um elemento)
letras = set("python")  # {'p', 'y', 't', 'h', 'o', 'n'}

# Set vazio — ATENÇÃO: {} cria um dict, não um set!
vazio_correto   = set()       # ✔ set vazio
vazio_errado    = {}          # ✗ isso é um dicionário vazio

# frozenset — versão imutável do set
imutavel = frozenset([1, 2, 3])


# --- 2.2 ADIÇÃO E REMOÇÃO DE ELEMENTOS ---

cores = {"vermelho", "azul"}

cores.add("verde")            # adiciona um elemento
cores.update(["amarelo", "roxo"])  # adiciona múltiplos elementos

cores.remove("azul")          # remove; lança KeyError se não existir
cores.discard("preto")        # remove; NÃO lança erro se não existir
elemento = cores.pop()        # remove e retorna um elemento arbitrário
cores.clear()                 # remove todos os elementos


# --- 2.3 VERIFICAÇÃO DE PERTENCIMENTO ---

animais = {"gato", "cachorro", "peixe"}

print("gato" in animais)      # True  — O(1), muito eficiente
print("cobra" not in animais) # True


# --- 2.4 ITERAÇÃO ---

for animal in animais:
    print(animal)             # ordem não garantida


# --- 2.5 TAMANHO ---

print(len(animais))           # número de elementos


# -----------------------------------------------------------------------------
# 3. OPERAÇÕES MATEMÁTICAS DE CONJUNTO
# -----------------------------------------------------------------------------
#
# Esta é uma das maiores forças do set — operações de teoria dos conjuntos
# prontas para uso, disponíveis como métodos OU operadores simbólicos.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# UNIÃO — todos os elementos de A e B (sem repetição)
uniao_op     = A | B                  # {1, 2, 3, 4, 5, 6}
uniao_metodo = A.union(B)             # equivalente

# INTERSEÇÃO — apenas os elementos comuns
inter_op     = A & B                  # {3, 4}
inter_metodo = A.intersection(B)      # equivalente

# DIFERENÇA — elementos em A que NÃO estão em B
dif_op       = A - B                  # {1, 2}
dif_metodo   = A.difference(B)        # equivalente

# DIFERENÇA SIMÉTRICA — elementos que estão em A ou B, mas NÃO em ambos
sim_op       = A ^ B                  # {1, 2, 5, 6}
sim_metodo   = A.symmetric_difference(B)  # equivalente

# SUBCONJUNTO — todos os elementos de X estão em Y?
X = {3, 4}
print(X.issubset(A))          # True  (X ⊆ A)
print(X <= A)                 # True  — operador equivalente

# SUPERCONJUNTO — A contém todos os elementos de X?
print(A.issuperset(X))        # True  (A ⊇ X)
print(A >= X)                 # True  — operador equivalente

# CONJUNTOS DISJUNTOS — não têm nenhum elemento em comum?
C = {10, 20}
print(A.isdisjoint(C))        # True


# --- Versões in-place (modificam o set original) ---

A |= {7, 8}           # união in-place         (update)
A &= {1, 2, 7}        # interseção in-place     (intersection_update)
A -= {2}              # diferença in-place      (difference_update)
A ^= {1, 9}           # dif. simétrica in-place (symmetric_difference_update)


# -----------------------------------------------------------------------------
# 4. SET COMPREHENSION (Compreensão de Conjunto)
# -----------------------------------------------------------------------------
#
# Assim como list comprehension, sets suportam sua própria sintaxe compacta.

quadrados = {x**2 for x in range(10)}             # {0, 1, 4, 9, 16, 25, ...}
pares     = {x for x in range(20) if x % 2 == 0}  # {0, 2, 4, 6, ...}


# -----------------------------------------------------------------------------
# 5. MÉTODOS DISPONÍVEIS — REFERÊNCIA RÁPIDA
# -----------------------------------------------------------------------------
#
# Método                         Descrição
# ─────────────────────────────────────────────────────────────────────────────
# add(elem)                    → adiciona um elemento
# update(*iteráveis)           → adiciona múltiplos elementos
# remove(elem)                 → remove; lança KeyError se ausente
# discard(elem)                → remove; silencioso se ausente
# pop()                        → remove/retorna elemento arbitrário
# clear()                      → esvazia o set
# copy()                       → retorna cópia rasa do set
# union(*outros)               → retorna a união (sem alterar o original)
# intersection(*outros)        → retorna a interseção
# difference(*outros)          → retorna a diferença
# symmetric_difference(outro)  → retorna a diferença simétrica
# issubset(outro)              → True se self ⊆ outro
# issuperset(outro)            → True se self ⊇ outro
# isdisjoint(outro)            → True se não há elementos comuns
# intersection_update(*outros) → interseção in-place
# difference_update(*outros)   → diferença in-place
# symmetric_difference_update  → dif. simétrica in-place
# ─────────────────────────────────────────────────────────────────────────────


# -----------------------------------------------------------------------------
# 6. MELHORES PRÁTICAS
# -----------------------------------------------------------------------------

# ✔ USE set() para eliminar duplicatas de uma lista de forma idiomática
nomes_com_repeticao = ["Ana", "Bruno", "Ana", "Carlos", "Bruno"]
nomes_unicos = list(set(nomes_com_repeticao))

# ✔ PREFIRA 'in' em sets em vez de listas para buscas frequentes
# Ruim para muitas buscas:
lista_ids = [101, 202, 303, 404]
if 202 in lista_ids:   # O(n) — percorre a lista inteira
    pass

# Bom:
set_ids = {101, 202, 303, 404}
if 202 in set_ids:     # O(1) — busca por hash
    pass

# ✔ USE frozenset quando precisar de um conjunto imutável
# (por exemplo, como chave de dicionário ou elemento de outro set)
config_permitida = frozenset(["admin", "editor"])
permissoes = {
    frozenset(["admin", "editor"]): "acesso total",
    frozenset(["viewer"]): "somente leitura",
}

# ✔ USE operadores simbólicos (|, &, -, ^) para código mais legível
# ✔ USE métodos quando precisar encadear ou passar múltiplos argumentos
resultado = A.union(B, C)   # múltiplos conjuntos de uma vez

# ✔ PREFIRA discard() a remove() quando a ausência do elemento é normal
# (evita tratar exceções desnecessariamente)

# ✔ NOMEIE sets com substantivos no plural para clareza
usuarios_ativos = {"alice", "bob", "carol"}


# -----------------------------------------------------------------------------
# 7. QUANDO USAR SET
# -----------------------------------------------------------------------------
#
# ✔ Quando precisar garantir unicidade de elementos (sem duplicatas)
#
# ✔ Quando realizar buscas de pertencimento com alta frequência
#   → 'x in set' é O(1) vs O(n) em listas
#
# ✔ Quando precisar de operações de teoria dos conjuntos:
#   → "quais clientes compraram A e B?" → interseção
#   → "quais itens estão em A mas não em B?" → diferença
#   → "todos os itens de A e B juntos?" → união
#
# ✔ Quando a ordem dos elementos NÃO importa
#
# ✔ Para eliminar duplicatas rapidamente de qualquer iterável
#
# ✔ Quando os elementos são hashable (strings, números, tuplas)
#
# Exemplos práticos de cenários reais:
#   • Verificar se um usuário tem determinada permissão
#   • Encontrar palavras comuns entre dois documentos
#   • Filtrar IDs únicos de um log de eventos
#   • Calcular diferenças entre versões de dados
#   • Validar se todos os campos obrigatórios foram preenchidos


# -----------------------------------------------------------------------------
# 8. QUANDO NÃO USAR SET
# -----------------------------------------------------------------------------
#
# ✗ Quando a ORDEM dos elementos importa
#   → Use list ou collections.OrderedDict
#
# ✗ Quando precisar de ÍNDICES ou fatias (slicing)
#   → sets não suportam set[0] ou set[1:3]
#
# ✗ Quando os elementos precisam ser MUTÁVEIS (listas, dicts)
#   → elementos precisam ser hashable; use listas de listas se necessário
#
# ✗ Quando precisar de elementos DUPLICADOS intencionalmente
#   → Use list ou collections.Counter
#
# ✗ Quando precisar de ACESSO FREQUENTE por índice ou posição
#   → list é mais adequado
#
# ✗ Quando o conjunto é MUITO PEQUENO e a operação ocorre poucas vezes
#   → O overhead de criar um set pode não compensar
#
# ✗ Quando precisar preservar a ordem de inserção com unicidade
#   → Considere dict.fromkeys() ou collections.OrderedDict como alternativa


# -----------------------------------------------------------------------------
# 9. COMPARAÇÃO COM OUTRAS ESTRUTURAS
# -----------------------------------------------------------------------------
#
# Estrutura   │ Ordenada │ Duplicatas │ Mutável │ Acesso por índice │ Busca
# ────────────┼──────────┼────────────┼─────────┼───────────────────┼──────
# list        │    ✔     │     ✔      │    ✔    │         ✔         │ O(n)
# tuple       │    ✔     │     ✔      │    ✗    │         ✔         │ O(n)
# set         │    ✗     │     ✗      │    ✔    │         ✗         │ O(1)
# frozenset   │    ✗     │     ✗      │    ✗    │         ✗         │ O(1)
# dict        │    ✔*    │  chaves ✗  │    ✔    │    por chave      │ O(1)
#
# * dicts mantêm ordem de inserção a partir do Python 3.7


# -----------------------------------------------------------------------------
# 10. EXEMPLOS PRÁTICOS COMPLETOS
# -----------------------------------------------------------------------------

# Exemplo 1: Encontrar emails duplicados em uma lista
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
emails_unicos = list(set(emails))
print(f"Únicos: {emails_unicos}")

# Exemplo 2: Usuários que assistiram ambos os vídeos
video1_viewers = {"alice", "bob", "carol", "dave"}
video2_viewers = {"bob", "carol", "eve", "frank"}
ambos = video1_viewers & video2_viewers
print(f"Assistiram ambos: {ambos}")   # {'bob', 'carol'}

# Exemplo 3: Verificar se todas as permissões necessárias estão presentes
necessarias  = {"read", "write", "execute"}
do_usuario   = {"read", "write", "execute", "delete"}
tem_acesso   = necessarias.issubset(do_usuario)
print(f"Acesso liberado: {tem_acesso}")   # True

# Exemplo 4: Remover stop words de um texto
stop_words = {"de", "a", "o", "e", "em", "que", "do", "da"}
palavras   = "o gato e o cachorro vivem em harmonia".split()
filtradas  = [p for p in palavras if p not in stop_words]
print(filtradas)   # ['gato', 'cachorro', 'vivem', 'harmonia']

# Exemplo 5: Itens adicionados e removidos entre duas versões
versao_antiga = {"login", "logout", "perfil", "dashboard"}
versao_nova   = {"login", "logout", "perfil", "relatorios", "config"}
adicionados   = versao_nova - versao_antiga    # {'relatorios', 'config'}
removidos     = versao_antiga - versao_nova    # {'dashboard'}


# -----------------------------------------------------------------------------
# 11. ARMADILHAS COMUNS
# -----------------------------------------------------------------------------

# ✗ ERRO: tentar criar set vazio com {}
errado = {}           # cria dict!
correto = set()       # ✔

# ✗ ERRO: adicionar elemento mutável
# meu_set = {[1, 2, 3]}  → TypeError: unhashable type: 'list'

# ✗ ERRO: acessar por índice
# meu_set = {10, 20, 30}
# meu_set[0]  → TypeError: 'set' object is not subscriptable

# ✗ ERRO: depender da ordem de iteração
# A ordem de um set pode variar entre execuções — não confie nela!

# ✗ ERRO: usar remove() quando o elemento pode não existir
s = {1, 2, 3}
# s.remove(99)   → KeyError!
s.discard(99)    # ✔ seguro


# -----------------------------------------------------------------------------
# 12. RESUMO
# -----------------------------------------------------------------------------
#
# SET é uma das estruturas mais eficientes e elegantes do Python quando o
# contexto exige:
#
#   1. UNICIDADE       → duplicatas são eliminadas automaticamente
#   2. PERFORMANCE     → buscas em O(1) graças à tabela hash interna
#   3. ÁLGEBRA         → operações de conjunto prontas (|, &, -, ^)
#
# Pontos-chave para memorizar:
#
#   • Criação literal:    {1, 2, 3}   |   set vazio: set()
#   • Elementos devem ser hashable (imutáveis)
#   • Sem índices, sem fatias, sem ordem garantida
#   • Use frozenset quando precisar de um set imutável/hashable
#   • Prefira 'discard' a 'remove' para remoções seguras
#   • Set comprehension: {expr for item in iterável if condição}
#
# Regra de ouro:
#   → Se você precisa de UNICIDADE ou PERTENCIMENTO RÁPIDO → use SET
#   → Se você precisa de ORDEM ou ÍNDICE                   → use LIST
#
# =============================================================================