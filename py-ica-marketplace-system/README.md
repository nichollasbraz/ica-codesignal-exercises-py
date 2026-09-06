# 🚀 SIMULADO FINAL — Revisão Integrada ICA
### Tudo Que Você Aprendeu em Um Lugar 🎯

Fala, guerreiro(a)! **HOJE É O DIA!** 

Esse é seu último treino antes do teste real. Vamos revisar TUDO que você aprendeu nos 3 simulados em um ÚNICO cenário.

---

## 📖 O Cenário: Sistema de Marketplace ("NubankMarket")

Um sistema simples de marketplace onde vendedores podem criar lojas, adicionar produtos, fazer vendas e ter limites diários.

**Conceitos que você vai usar:**
- ✅ Estruturas de dados (dicionários, listas)
- ✅ Validações e regras de negócio
- ✅ Histórico e rastreamento
- ✅ Cálculos e análise
- ✅ Limites e bloqueios
- ✅ Ordenação e filtros

---

## 🟢 Nível 1 — Operações Básicas

Implemente a classe `Marketplace` com:

- `create_store(store_id: str, timestamp: int) -> bool`
  Cria uma loja. Retorna `True` se criou, `False` se já existir.

- `add_product(store_id: str, product_id: str, price: int, stock: int) -> bool`
  Adiciona um produto à loja. Retorna `True` se bem-sucedido.

- `make_sale(store_id: str, product_id: str, timestamp: int, quantity: int) -> int | None`
  Faz uma venda. Retorna o **novo saldo de estoque** do produto. Retorna `None` se não conseguir.
  
  **Guarda cada venda com:** produto, quantidade, timestamp, estoque_restante.

- `get_store_info(store_id: str) -> dict | None`
  Retorna informações da loja:
  ```python
  {
    "store_id": "loja1",
    "total_revenue": 5000,          # Total arrecadado
    "total_products_sold": 50,      # Total de unidades vendidas
    "total_sales": 10,              # Número de transações
    "products_count": 3             # Quantos produtos diferentes tem
  }
  ```

---

## 🟡 Nível 2 — Análise de Dados

Adicione:

- `get_sales_history(store_id: str, limit: int) -> list[dict]`
  Retorna as últimas `limit` vendas ordenadas por timestamp (mais recentes primeiro).
  
  Cada venda:
  ```python
  {
    "product_id": "prod1",
    "quantity": 5,
    "timestamp": 100,
    "revenue": 2500        # quantidade * preço
  }
  ```

- `top_products(store_id: str, n: int) -> list[tuple[str, int]]`
  Retorna os N produtos mais vendidos (por quantidade).
  
  ```python
  [("prod1", 50), ("prod2", 30), ("prod3", 10)]
  ```

- `daily_revenue(store_id: str, timestamp: int) -> int`
  Retorna a receita do **mesmo dia** do timestamp fornecido.
  (Um dia = 1440 minutos)

---

## 🟠 Nível 3 — Limites e Bloqueios

Adicione:

- `set_daily_sale_limit(store_id: str, max_units: int) -> bool`
  Define limite diário de unidades que podem ser vendidas.

- `make_sale_with_limit(store_id: str, product_id: str, timestamp: int, quantity: int) -> bool`
  Tenta fazer uma venda respeitando o limite diário.
  
  **Se ultrapassar limite → bloqueado, registra em lista de bloqueados.**
  
  Retorna `True` se bem-sucedido, `False` se bloqueado.

- `get_blocked_sales(store_id: str) -> list[dict]`
  Retorna todas as vendas que foram **bloqueadas**:
  
  ```python
  {
    "product_id": "prod1",
    "quantity": 100,
    "timestamp": 150,
    "reason": "daily_limit_exceeded"
  }
  ```

---

## 🔴 Nível 4 — Análise Avançada

Adicione:

- `get_best_seller_product(store_id: str) -> dict | None`
  Retorna o produto mais vendido (por quantidade total):
  
  ```python
  {
    "product_id": "prod1",
    "quantity_sold": 150,
    "revenue_generated": 7500
  }
  ```

- `sales_pattern(store_id: str) -> dict`
  Retorna padrão de vendas:
  
  ```python
  {
    "average_sale_quantity": 5,
    "average_sale_price": 500,
    "total_blocked_sales": 2,
    "most_active_day": 0,  # qual "dia" teve mais vendas
    "unique_products_sold": 3
  }
  ```

---

## 🧪 Exemplo de Uso

```python
m = Marketplace()
m.create_store("loja1", 0)
m.add_product("loja1", "prod1", 500, 100)
m.add_product("loja1", "prod2", 200, 50)

m.make_sale("loja1", "prod1", 10, 5)    # 5 unidades vendidas
m.make_sale("loja1", "prod1", 20, 3)    # 3 unidades vendidas
m.make_sale("loja1", "prod2", 30, 10)   # 10 unidades vendidas

print(m.get_store_info("loja1"))
# {
#   "store_id": "loja1",
#   "total_revenue": 4500,    # (5*500) + (3*500) + (10*200)
#   "total_products_sold": 18,
#   "total_sales": 3,
#   "products_count": 2
# }

m.set_daily_sale_limit("loja1", 15)
m.make_sale_with_limit("loja1", "prod1", 40, 5)   # Bloqueado (20 > 15)
m.make_sale_with_limit("loja1", "prod1", 40, 10)  # Bem-sucedido (10 <= 15)
```

---

## 📝 Dicas de Ouro

1. **Cada venda precisa guardar:** produto, quantidade, timestamp, estoque, receita
2. **Um "dia" = 1440 minutos:** Para calcular "mesmo dia"
3. **Estrutura de dados desde o início:** `__init__` bem planejado é 90% do sucesso
4. **Reutiliza lógica:** Métodos já implementados (tipo `daily_revenue`) podem ser usados como base para outros
5. **Não complica:** Foco em funcionar, não em ser perfeito

---

## 💪 Seu Desafio

**Tenta implementar tudo sozinho em 90 minutos.**

Se travar:
1. Releia o enunciado
2. Pense na estrutura de dados necessária
3. Quebre o problema em partes menores
4. Me chama se precisar destrinchar um CONCEITO, não o código

---

## 🎯 Você Consegue!

Você já fez 3 simulados completos. Você já sabe como fazer isso. É só aplicar de novo!

**BOA SORTE! 🚀🐍**
