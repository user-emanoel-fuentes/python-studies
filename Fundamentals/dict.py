# =============================================================================
# DICIONÁRIOS EM PYTHON
# =============================================================================
# Arquivo de referência técnica — Rico em detalhes, claro e objetivo.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. O QUE É
# -----------------------------------------------------------------------------
#
# Um dicionário (dict) é uma estrutura de dados nativa do Python que armazena
# pares de CHAVE → VALOR. É uma coleção:
#
#   - MUTÁVEL       → pode ser alterado após a criação
#   - DESORDENADA*  → não garante ordem de inserção até Python 3.6;
#                     a partir do Python 3.7+ a ordem de inserção É garantida
#   - SEM DUPLICATA DE CHAVES → cada chave é única dentro do dicionário
#   - HETEROGÊNEA   → chaves e valores podem ser de tipos diferentes
#
# Internamente, dicionários são implementados como tabelas hash (hash tables),
# o que garante acesso, inserção e remoção com complexidade média O(1).
#
# Chaves válidas: qualquer objeto IMUTÁVEL (str, int, float, tuple, bool).
# Chaves inválidas: listas, dicionários, sets (são mutáveis → não são hasháveis).
#
# Valores: qualquer objeto Python — não há restrição de tipo.


# -----------------------------------------------------------------------------
# 2. SINTAXE DE USO
# -----------------------------------------------------------------------------

# --- 2.1 Criação ---

# Forma literal (mais comum e legível)
pessoa = {
    "nome": "Ana",
    "idade": 30,
    "ativa": True
}

# Construtor dict() com argumentos nomeados
config = dict(host="localhost", porta=5432, debug=False)

# Construtor dict() com lista de tuplas
coordenadas = dict([("x", 10), ("y", 20), ("z", 0)])

# Dicionário vazio
vazio_literal     = {}
vazio_construtor  = dict()

# Dict comprehension (forma compacta e poderosa)
quadrados = {n: n**2 for n in range(1, 6)}
# Resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dict comprehension com filtro
pares = {n: n**2 for n in range(1, 11) if n % 2 == 0}
# Resultado: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Criar dicionário com valor padrão para múltiplas chaves
chaves = ["a", "b", "c"]
padrao = dict.fromkeys(chaves, 0)
# Resultado: {'a': 0, 'b': 0, 'c': 0}


# --- 2.2 Acesso a valores ---

nome = pessoa["nome"]             # Acesso direto → KeyError se não existir
idade = pessoa.get("idade")       # Acesso seguro → retorna None se não existir
cidade = pessoa.get("cidade", "Não informada")  # Valor padrão se ausente


# --- 2.3 Inserção e atualização ---

pessoa["email"] = "ana@email.com"          # Insere nova chave
pessoa["idade"] = 31                       # Atualiza valor existente
pessoa.update({"telefone": "99999-0000"})  # Atualiza/insere múltiplas chaves
pessoa.update(pais="Brasil", estado="SP")  # Também aceita kwargs


# --- 2.4 Remoção ---

del pessoa["email"]                    # Remove a chave → KeyError se não existir
valor = pessoa.pop("telefone")         # Remove e retorna o valor
valor_seguro = pessoa.pop("fax", None) # Remove com fallback → evita KeyError
ultimo = pessoa.popitem()              # Remove e retorna o último par (chave, valor)
pessoa.clear()                         # Remove todos os itens (dicionário vazio)


# --- 2.5 Verificação de existência ---

dados = {"x": 10, "y": 20}

"x" in dados          # True  — verifica se a chave existe
"z" not in dados      # True  — verifica se a chave NÃO existe
10 in dados.values()  # True  — verifica se o valor existe


# --- 2.6 Iteração ---

estoque = {"maçã": 50, "banana": 30, "uva": 80}

for chave in estoque:                      # Itera apenas pelas chaves
    print(chave)

for valor in estoque.values():             # Itera apenas pelos valores
    print(valor)

for chave, valor in estoque.items():       # Itera por pares (chave, valor)
    print(f"{chave}: {valor}")


# --- 2.7 Cópia ---

original = {"a": 1, "b": [1, 2, 3]}

copia_rasa    = original.copy()        # Cópia rasa (shallow copy)
copia_rasa2   = dict(original)         # Equivalente ao .copy()

import copy
copia_profunda = copy.deepcopy(original)  # Cópia profunda (deep copy)
# Use deepcopy quando os valores forem objetos mutáveis (listas, dicts aninhados)


# --- 2.8 Merge de dicionários ---

base    = {"a": 1, "b": 2}
extra   = {"b": 99, "c": 3}

# Python 3.9+ → operador | (merge sem modificar os originais)
merged = base | extra
# Resultado: {'a': 1, 'b': 99, 'c': 3}  ← 'b' do extra prevalece

# Python 3.9+ → operador |= (merge in-place)
base |= extra

# Python 3.5+ → desempacotamento com **
merged_antigo = {**base, **extra}

# Usando update() (modifica o dicionário chamador)
base.update(extra)


# --- 2.9 Dicionários aninhados ---

usuarios = {
    "user_01": {"nome": "Carlos", "perfil": "admin"},
    "user_02": {"nome": "Beatriz", "perfil": "viewer"},
}

nome_carlos = usuarios["user_01"]["nome"]                   # "Carlos"
perfil_safe = usuarios.get("user_03", {}).get("perfil")     # None (sem KeyError)


# -----------------------------------------------------------------------------
# 3. RECURSOS MAIS COMUNS
# -----------------------------------------------------------------------------

# --- 3.1 setdefault() ---
# Retorna o valor da chave. Se não existir, insere com o valor padrão.

contador = {}
palavras = ["oi", "tchau", "oi", "oi", "tchau"]

for palavra in palavras:
    contador.setdefault(palavra, 0)
    contador[palavra] += 1
# Resultado: {'oi': 3, 'tchau': 2}


# --- 3.2 collections.defaultdict ---
# Semelhante ao dict, mas cria automaticamente um valor padrão para chaves novas.

from collections import defaultdict

agrupado = defaultdict(list)
pares_dados = [("fruta", "maçã"), ("vegetal", "cenoura"), ("fruta", "banana")]

for categoria, item in pares_dados:
    agrupado[categoria].append(item)
# Resultado: {'fruta': ['maçã', 'banana'], 'vegetal': ['cenoura']}


# --- 3.3 collections.Counter ---
# Subclasse de dict especializada em contagem de elementos.

from collections import Counter

texto = "abracadabra"
contagem = Counter(texto)
# Resultado: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

mais_comuns = contagem.most_common(3)
# Resultado: [('a', 5), ('b', 2), ('r', 2)]


# --- 3.4 collections.OrderedDict ---
# Antes do Python 3.7, garantia ordem de inserção.
# Hoje ainda é útil quando a ordem tem significado semântico explícito
# ou ao usar .move_to_end() para reordenar.

from collections import OrderedDict

od = OrderedDict([("primeiro", 1), ("segundo", 2), ("terceiro", 3)])
od.move_to_end("primeiro")        # Move para o final
od.move_to_end("terceiro", False) # Move para o início


# --- 3.5 Unpacking com ** ---

def saudar(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

params = {"nome": "Laura", "saudacao": "Boa tarde"}
print(saudar(**params))   # "Boa tarde, Laura!"


# --- 3.6 Inversão de dicionário ---

original_inv = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original_inv.items()}
# Resultado: {1: 'a', 2: 'b', 3: 'c'}
# ⚠️ Só funciona corretamente se os valores forem únicos e hasháveis.


# --- 3.7 Ordenação ---

notas = {"Maria": 9.5, "João": 7.0, "Paula": 8.8}

# Ordenar por chave
por_nome = dict(sorted(notas.items()))

# Ordenar por valor (decrescente)
por_nota = dict(sorted(notas.items(), key=lambda item: item[1], reverse=True))


# --- 3.8 Filtragem via comprehension ---

estoque2 = {"maçã": 0, "banana": 15, "uva": 0, "laranja": 40}
disponivel = {k: v for k, v in estoque2.items() if v > 0}
# Resultado: {'banana': 15, 'laranja': 40}


# --- 3.9 len(), min(), max() com dicionários ---

tamanho = len(notas)                      # Número de pares chave-valor
menor_nota = min(notas, key=notas.get)    # Chave com menor valor
maior_nota = max(notas, key=notas.get)    # Chave com maior valor


# -----------------------------------------------------------------------------
# 4. MELHORES PRÁTICAS
# -----------------------------------------------------------------------------
#
# ✅ Prefira .get() ao invés de acesso direto quando a chave pode não existir.
#    → Evita KeyError e torna o código mais robusto.
#
# ✅ Use dict comprehensions para criar dicionários de forma concisa e legível.
#    → Mais eficiente que um loop for com dict vazio + atribuição.
#
# ✅ Use .items() ao iterar quando precisar de chave e valor ao mesmo tempo.
#    → Mais claro e eficiente do que acessar o valor por chave dentro do loop.
#
# ✅ Prefira o operador | (Python 3.9+) para merge sem efeitos colaterais.
#    → {**a, **b} ainda funciona, mas | é mais legível.
#
# ✅ Use copy.deepcopy() quando o dicionário contiver objetos mutáveis aninhados.
#    → .copy() é raso — alterações nos valores mutáveis afetam o original.
#
# ✅ Documente a estrutura esperada dos dicionários em funções públicas.
#    → Ou melhor ainda: use TypedDict ou dataclasses para contratos mais claros.
#
# ✅ Utilize collections.defaultdict para agrupamentos — evita verificações
#    manuais de existência de chave.
#
# ✅ Mantenha chaves com nomes consistentes (snake_case por convenção Python).
#
# ❌ Não use listas mutáveis como chaves — causam TypeError.
# ❌ Não confie na ordem de iteração em versões anteriores ao Python 3.7.
# ❌ Não faça dicionários profundamente aninhados sem necessidade —
#    prefira dataclasses, NamedTuple ou Pydantic para estruturas complexas.


# -----------------------------------------------------------------------------
# 5. QUANDO USAR DICIONÁRIOS
# -----------------------------------------------------------------------------
#
# ✔ Quando você precisa de acesso rápido a dados por uma chave identificadora.
#   Exemplo: buscar configurações por nome, usuários por ID.
#
# ✔ Para representar objetos sem a formalidade de uma classe.
#   Exemplo: respostas de APIs JSON, configurações, metadados.
#
# ✔ Para contagem e agrupamento de elementos.
#   Exemplo: frequência de palavras, itens por categoria.
#
# ✔ Para representar relacionamentos de mapeamento (chave → valor único).
#   Exemplo: tabela de conversão, mapa de códigos para descrições.
#
# ✔ Quando precisar eliminar duplicatas mantendo informações associadas.
#
# ✔ Como cache / memoização de resultados de funções.
#   Exemplo: guardar resultados de cálculos pesados indexados pelos parâmetros.


# -----------------------------------------------------------------------------
# 6. QUANDO NÃO USAR DICIONÁRIOS
# -----------------------------------------------------------------------------
#
# ✘ Quando a ordem dos elementos é o único critério relevante → use lista.
#
# ✘ Quando os dados são apenas valores sem chave associada → use lista ou set.
#
# ✘ Quando precisar de unicidade sem associação de valor → use set.
#
# ✘ Quando a estrutura for complexa e com tipagem importante → use dataclass,
#   NamedTuple ou Pydantic BaseModel (mais seguro, autodocumentado).
#
# ✘ Quando for necessário acessar elementos por posição/índice → use lista.
#
# ✘ Quando houver múltiplos registros do mesmo formato para análise de dados
#   em escala → prefira pandas DataFrame ou banco de dados.
#
# ✘ Quando as chaves precisam ser objetos mutáveis → dicionário não suporta.


# -----------------------------------------------------------------------------
# 7. RESUMO
# -----------------------------------------------------------------------------
#
#  Estrutura   │ dict (dicionário)
#  Sintaxe     │ {chave: valor}  ou  dict()
#  Acesso      │ O(1) médio (hash table)
#  Ordenação   │ Garantida por inserção a partir do Python 3.7
#  Chaves      │ Apenas objetos imutáveis (str, int, tuple...)
#  Valores     │ Qualquer objeto Python
#  Mutável     │ Sim
#  Duplicatas  │ Chaves únicas; valores podem repetir
#
#  Métodos essenciais:
#  ┌─────────────────────────────────────────────────────────────────┐
#  │ .get(k, default)   → acesso seguro com fallback                 │
#  │ .setdefault(k, v)  → insere somente se a chave não existir      │
#  │ .update(outro)     → merge in-place                             │
#  │ .pop(k, default)   → remove e retorna valor                     │
#  │ .keys()            → view das chaves                            │
#  │ .values()          → view dos valores                           │
#  │ .items()           → view dos pares (chave, valor)              │
#  │ .copy()            → cópia rasa                                 │
#  │ .clear()           → esvazia o dicionário                       │
#  │ dict.fromkeys(ks)  → cria dict com chaves e valor padrão        │
#  └─────────────────────────────────────────────────────────────────┘
#
#  Aliados poderosos do módulo collections:
#    • defaultdict  → valor padrão automático para chaves novas
#    • Counter      → contagem de elementos
#    • OrderedDict  → útil para lógica que depende da ordem explícita
#
#  Operadores modernos (Python 3.9+):
#    • d1 | d2   → novo dict com merge (d2 prevalece em conflitos)
#    • d1 |= d2  → merge in-place
#
#  Regra de ouro:
#    Se você precisa associar um IDENTIFICADOR a um DADO → use dicionário.
#    Se precisar de mais estrutura ou tipagem → use dataclass ou Pydantic.

# =============================================================================
# FIM DO ARQUIVO DE REFERÊNCIA — DICIONÁRIOS EM PYTHON
# =============================================================================