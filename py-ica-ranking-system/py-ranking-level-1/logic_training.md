# 🧠 Treinamento de Padrões de Lógica
### Material Completo: Padrões Visuais + Mini-Exercícios + Template Mental

---

# PARTE 1: PADRÕES VISUAIS
### (Como desenhar sua lógica ANTES de codificar)

---

## 🎯 Padrão 1: AGREGAÇÃO (Somar / Contar)

**Situação:** "Quanto foi vendido no total?" ou "Quantos produtos diferentes?"

**Desenho Visual:**

```
dados = [A, B, C, D, E]
         ↓ ↓ ↓ ↓ ↓
    ACUMULATOR
      ↓ A
     ↓ A+B
    ↓ A+B+C
   ↓ A+B+C+D
  ↓ A+B+C+D+E = RESULTADO
```

**Pseudocódigo:**

```
total = 0
para cada item em dados:
    total += item
retorna total
```

**Exemplo Real:**

```python
total_sold = 0
for sale in self.sales:
    total_sold += sale["quantity"]  # ← Acumula!
return total_sold
```

---

## 🎯 Padrão 2: FILTRO + AGREGAÇÃO

**Situação:** "Quanto foi vendido de MOUSE?" ou "Quantas pessoas acima de 25?"

**Desenho Visual:**

```
dados = [A(mouse), B(teclado), C(mouse), D(mouse), E(teclado)]
         ↓
    FILTRO (pega só mouse)
         ↓
    A(mouse), C(mouse), D(mouse)
         ↓
    ACUMULATOR
      ↓ A
     ↓ A+C
    ↓ A+C+D = RESULTADO
```

**Pseudocódigo:**

```
total = 0
para cada item em dados:
    SE item passa no filtro:
        total += item
retorna total
```

**Exemplo Real:**

```python
total_sold = 0
for sale in self.sales:
    if sale["product_id"] == "mouse":  # ← FILTRO
        total_sold += sale["quantity"]  # ← AGREGAÇÃO
return total_sold
```

---

## 🎯 Padrão 3: AGREGAR POR CATEGORIA

**Situação:** "Quanto vendeu de cada produto?" ou "Pontos de cada jogador?"

**Desenho Visual:**

```
dados = [mouse(5), teclado(3), mouse(2), teclado(1)]
         ↓
    AGRUPAR
         ↓
    mouse: [5, 2]
    teclado: [3, 1]
         ↓
    SOMAR cada grupo
         ↓
    mouse: 7
    teclado: 4
         ↓
    {"mouse": 7, "teclado": 4}
```

**Pseudocódigo:**

```
resultado = {}
para cada item em dados:
    categoria = item.categoria
    
    SE categoria não em resultado:
        resultado[categoria] = item.valor
    SENÃO:
        resultado[categoria] += item.valor

retorna resultado
```

**Exemplo Real:**

```python
product_totals = {}
for sale in self.sales:
    product_id = sale["product_id"]
    quantity = sale["quantity"]
    
    if product_id not in product_totals:
        product_totals[product_id] = quantity
    else:
        product_totals[product_id] += quantity

return product_totals
```

---

## 🎯 Padrão 4: ORDENAÇÃO COM DESEMPATE

**Situação:** "Top 3 produtos?" ou "Leaderboard (maior primeiro, desempate alfabético)?"

**Desenho Visual:**

```
dados = [("alice", 100), ("bob", 100), ("charlie", 80)]
         ↓
    ORDENAR
    Critério 1: valor DESC (maior primeiro)
    Critério 2: nome ASC (alfabético)
         ↓
    [("alice", 100), ("bob", 100), ("charlie", 80)]
      ↑ mesmo valor, alice vem antes de bob (A < B)
```

**Pseudocódigo:**

```
resultado = sorted(dados, key=CRITÉRIO)

CRITÉRIO = (-valor, nome)
    ↑ negativo = inverte ordem (maior primeiro)
```

**Exemplo Real:**

```python
leaderboard = sorted(
    players.items(),
    key=lambda item: (-item[1], item[0])
)
# item[1] = pontos (negativo = maior primeiro)
# item[0] = nome (positivo = alfabético)
```

---

## 🎯 Padrão 5: LOOP ANINHADO (Quando Está Dentro vs Fora)

**Situação Comum:** Você tá criando dados DENTRO do loop quando deveria estar FORA

**Desenho Visual - ERRADO:**

```
para cada PRODUTO:
    para cada VENDA:
        SE venda é desse produto:
            soma
        CRIA recomendação  ← DENTRO! Vai repetir!
        ADICIONA resultado ← DENTRO! Vai repetir!
```

**Resultado:** Se 5 vendas desse produto, cria 5 recomendações iguais ❌

---

**Desenho Visual - CERTO:**

```
para cada PRODUTO:
    para cada VENDA:
        SE venda é desse produto:
            soma
    SAIR do loop de vendas
    CRIA recomendação  ← FORA! Cria uma vez!
    ADICIONA resultado ← FORA! Adiciona uma vez!
```

**Resultado:** Uma recomendação por produto ✅

---

**Pseudocódigo - CERTO:**

```
para cada produto:
    total = 0
    para cada venda:
        se venda é do produto:
            total += venda
    # ← Saiu do loop de vendas
    recomendacao = cria(total)
    resultado.adiciona(recomendacao)
```

---

## 🎯 Padrão 6: FILTRO SIMPLES (Retornar Lista)

**Situação:** "Quais produtos têm preço entre 100-200?"

**Desenho Visual:**

```
dados = [A(150), B(50), C(180), D(300), E(120)]
         ↓
    FILTRO: 100-200?
         ↓
    [A(150), C(180), E(120)]
```

**Pseudocódigo:**

```
resultado = []
para cada item em dados:
    SE item passa no filtro:
        resultado.adiciona(item)
retorna resultado
```

**Exemplo Real:**

```python
products = []
for product_id in self.products:
    price = self.products[product_id]["price"]
    if price >= min_price and price <= max_price:
        products.append(product_id)
return products
```

---

# PARTE 2: MINI-EXERCÍCIOS (10x 5 minutos)
### (Prática pura dos padrões)

---

## Exercício 1: AGREGAÇÃO BÁSICA

**Dados:**

```python
vendas = [10, 20, 15, 30]
```

**Pergunta:** Qual é o total?

**Seu Código:**

```python
total = 0
# ... seu código aqui ...
print(total)  # Deve retornar: 75
```

**Resposta:**

```python
total = 0
for venda in vendas:
    total += venda
print(total)  # 75
```

---

## Exercício 2: FILTRO + AGREGAÇÃO

**Dados:**

```python
vendas = [
    {"produto": "mouse", "quantidade": 5},
    {"produto": "teclado", "quantidade": 3},
    {"produto": "mouse", "quantidade": 2},
]
```

**Pergunta:** Quanto vendeu de MOUSE?

**Seu Código:**

```python
total = 0
# ... seu código aqui ...
print(total)  # Deve retornar: 7
```

**Resposta:**

```python
total = 0
for venda in vendas:
    if venda["produto"] == "mouse":
        total += venda["quantidade"]
print(total)  # 7
```

---

## Exercício 3: AGREGAR POR CATEGORIA

**Dados:**

```python
vendas = [
    {"produto": "mouse", "quantidade": 5},
    {"produto": "teclado", "quantidade": 3},
    {"produto": "mouse", "quantidade": 2},
    {"produto": "teclado", "quantidade": 1},
]
```

**Pergunta:** Quanto de cada produto?

**Seu Código:**

```python
resultado = {}
# ... seu código aqui ...
print(resultado)  # Deve retornar: {"mouse": 7, "teclado": 4}
```

**Resposta:**

```python
resultado = {}
for venda in vendas:
    produto = venda["produto"]
    quantidade = venda["quantidade"]
    
    if produto not in resultado:
        resultado[produto] = quantidade
    else:
        resultado[produto] += quantidade

print(resultado)  # {"mouse": 7, "teclado": 4}
```

---

## Exercício 4: ENCONTRAR MÁXIMO

**Dados:**

```python
produtos = {"mouse": 5, "teclado": 3, "monitor": 8}
```

**Pergunta:** Qual produto vendeu mais?

**Seu Código:**

```python
maior = None
maior_quantidade = 0
# ... seu código aqui ...
print(maior)  # Deve retornar: "monitor"
```

**Resposta:**

```python
maior = None
maior_quantidade = 0

for produto, quantidade in produtos.items():
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        maior = produto

print(maior)  # "monitor"
```

---

## Exercício 5: ORDENAÇÃO COM DESEMPATE

**Dados:**

```python
jogadores = [("alice", 100), ("bob", 100), ("charlie", 80)]
```

**Pergunta:** Ordene (maior pontuação, desempate alfabético)

**Seu Código:**

```python
resultado = sorted(# ... seu código aqui ...)
print(resultado)  # Deve retornar: [("alice", 100), ("bob", 100), ("charlie", 80)]
```

**Resposta:**

```python
resultado = sorted(jogadores, key=lambda item: (-item[1], item[0]))
print(resultado)  # [("alice", 100), ("bob", 100), ("charlie", 80)]
```

---

## Exercício 6: FILTRO SIMPLES

**Dados:**

```python
produtos = {"mouse": 150, "teclado": 50, "monitor": 500, "mousepad": 80}
```

**Pergunta:** Quais produtos custam entre 100-400?

**Seu Código:**

```python
resultado = []
# ... seu código aqui ...
print(resultado)  # Deve retornar: ["mouse", "monitor"]
```

**Resposta:**

```python
resultado = []
for nome, preco in produtos.items():
    if 100 <= preco <= 400:
        resultado.append(nome)

resultado.sort()  # Ordenar alfabeticamente
print(resultado)  # ["monitor", "mouse"]
```

---

## Exercício 7: MÉDIA

**Dados:**

```python
vendas = [10, 20, 15, 30, 25]
```

**Pergunta:** Qual é a média (usar //, não /)

**Seu Código:**

```python
total = 0
# ... seu código aqui ...
media = # ...
print(media)  # Deve retornar: 20
```

**Resposta:**

```python
total = 0
for venda in vendas:
    total += venda

media = total // len(vendas)  # floor division
print(media)  # 20
```

---

## Exercício 8: ENCONTRAR PIOR (Mínimo)

**Dados:**

```python
rodadas = [
    {"round": 1, "pontos": 50},
    {"round": 2, "pontos": 75},
    {"round": 3, "pontos": 25},
]
```

**Pergunta:** Qual foi a pior rodada?

**Seu Código:**

```python
pior = None
menor_pontos = float('inf')  # começa muito grande
# ... seu código aqui ...
print(pior)  # Deve retornar: {"round": 3, "pontos": 25}
```

**Resposta:**

```python
pior = None
menor_pontos = float('inf')

for rodada in rodadas:
    if rodada["pontos"] < menor_pontos:
        menor_pontos = rodada["pontos"]
        pior = rodada

print(pior)  # {"round": 3, "pontos": 25}
```

---

## Exercício 9: CONTAR COM FILTRO

**Dados:**

```python
produtos = [
    {"nome": "mouse", "stock": 0},
    {"nome": "teclado", "stock": 5},
    {"nome": "monitor", "stock": 0},
    {"nome": "mousepad", "stock": 2},
]
```

**Pergunta:** Quantos produtos estão fora de estoque (stock == 0)?

**Seu Código:**

```python
fora_estoque = 0
# ... seu código aqui ...
print(fora_estoque)  # Deve retornar: 2
```

**Resposta:**

```python
fora_estoque = 0
for produto in produtos:
    if produto["stock"] == 0:
        fora_estoque += 1

print(fora_estoque)  # 2
```

---

## Exercício 10: FILTRO + ORDENAÇÃO

**Dados:**

```python
vendas = [
    {"produto": "mouse", "quantidade": 5, "timestamp": 100},
    {"produto": "teclado", "quantidade": 3, "timestamp": 50},
    {"produto": "mouse", "quantidade": 2, "timestamp": 150},
    {"produto": "teclado", "quantidade": 1, "timestamp": 75},
]
```

**Pergunta:** Vendas de MOUSE, ordenadas por timestamp (mais recentes primeiro)

**Seu Código:**

```python
resultado = []
# ... seu código aqui ...
resultado = sorted(# ...)
print(resultado)
# Deve retornar: [
#     {"produto": "mouse", "quantidade": 2, "timestamp": 150},
#     {"produto": "mouse", "quantidade": 5, "timestamp": 100},
# ]
```

**Resposta:**

```python
resultado = []
for venda in vendas:
    if venda["produto"] == "mouse":
        resultado.append(venda)

resultado = sorted(resultado, key=lambda item: -item["timestamp"])
print(resultado)
```

---

# PARTE 3: TEMPLATE MENTAL
### (Checklist para usar sempre)

---

## 🎯 ANTES DE CODIFICAR (Leia 2x)

### Passo 1: Identifique o Padrão

```
[ ] É somar/contar? → AGREGAÇÃO
[ ] É filtrar itens? → FILTRO SIMPLES
[ ] É somar de UM tipo? → FILTRO + AGREGAÇÃO
[ ] É somar de CADA tipo? → AGREGAR POR CATEGORIA
[ ] É ordenar e retornar? → ORDENAÇÃO COM DESEMPATE
[ ] É encontrar maior/menor? → MAX/MIN
[ ] Tem 2 loops? → LOOP ANINHADO (cuidado!)
```

### Passo 2: Desenhe (Mesmo que Mentalmente)

```
Dados iniciais?
      ↓
Transformação?
      ↓
Resultado?
```

### Passo 3: Valide Entrada

```python
if condicao_invalida:
    return tipo_correto_pra_falha  # None, [], False, etc
```

### Passo 4: Implementar Padrão

**Se AGREGAÇÃO:**

```python
resultado = 0  # ou [] ou {}
for item in dados:
    if filtro_necessario:
        resultado += item
return resultado
```

**Se AGREGAR POR CATEGORIA:**

```python
resultado = {}
for item in dados:
    categoria = item.categoria
    if categoria not in resultado:
        resultado[categoria] = 0
    resultado[categoria] += item.valor
return resultado
```

**Se LOOP ANINHADO:**

```python
for item1 in dados1:
    acumulator = 0
    for item2 em dados2:
        if filtro:
            acumulator += item2
    # ← SAIR do loop 2
    fazer_algo_com(acumulator)
    adicionar_resultado
```

---

## 🎯 DURANTE A CODIFICAÇÃO

### Checklist de Debugging

```
[ ] Validei entrada (None, vazio, negativo)?
[ ] Inicializei variáveis ANTES do loop?
[ ] Estou retornando do tipo certo?
[ ] Se tem 2 loops, está a indentação correta?
[ ] Se tem ordenação, o desempate tá certo?
[ ] Se tem filtro, estou verificando antes de agregar?
```

### Testes Rápidos

```python
# ANTES de submeter, teste:

# 1. Entrada vazia
resultado = funcao()  # []? None? Depende!

# 2. Um item só
resultado = funcao_com_1_item()  # Funciona igual?

# 3. Vários items
resultado = funcao_com_varios()  # Soma certo?

# 4. Valores extremos
resultado = funcao(-100)  # Negativo tá ok?
resultado = funcao(0)     # Zero tá ok?
```

---

## 📋 TABELA RÁPIDA: RETORNE O TIPO CERTO

| Função | Validação Falha | Vazio | Sucesso |
|--------|---|---|---|
| `bool` | False | N/A | True |
| `int \| None` | None | N/A | int |
| `dict \| None` | None | {} (vazio ok) | {} |
| `list[dict]` | None | [] (vazio ok!) | [...] |
| `str \| None` | None | N/A | "string" |

---

## 💡 DICA: LEI DO TIPO DE RETORNO

**Se volta `list`: validação falha é SEMPRE None**

```python
def get_items() -> list[dict]:
    if condicao_ruim:
        return None  # ← Tipo errado! Deveria ser []
```

**Correto:**

```python
def get_items() -> list[dict]:
    if condicao_ruim:
        return []  # ← Lista vazia é ok!
```

---

## 🎯 EXEMPLO COMPLETO: Tudo Junto

**Problema:**

"Retorne os 3 melhores vendedores, com total vendido > 50, ordenado por vendas DESC e nome ASC"

**Meu Pensamento:**

```
1. Padrão: FILTRO + AGREGAÇÃO + ORDENAÇÃO
2. Desenho:
   dados → agregar por vendedor → filtrar > 50 → ordenar → retornar top 3
3. Validações:
   - Dados vazios?
   - Ninguém com > 50?
4. Código:

# Agregação
vendedores = {}
for venda in dados:
    vendedor = venda.vendedor
    if vendedor not in vendedores:
        vendedores[vendedor] = 0
    vendedores[vendedor] += venda.quantidade

# Filtro
filtrado = {v: qty for v, qty in vendedores.items() if qty > 50}

# Ordenação
resultado = sorted(filtrado.items(), key=lambda item: (-item[1], item[0]))

# Top 3
return resultado[:3]
```

---

## 🚀 COMO USAR ESTE DOCUMENTO

1. **Leia os Padrões Visuais** (10 min)
2. **Faça os 10 Mini-Exercícios** (50 min, 5 cada)
3. **Salve o Template Mental** (consulte sempre!)
4. **Antes de cada função, desenhe!**

---

## 💪 Última Dica

**Se tá ficando complicado, você tá codificando sem desenhar!**

Sempre:
1. Entenda o padrão
2. Desenhe (papel ou mentalmente)
3. Código sai natural

Boa sorte! 🚀
