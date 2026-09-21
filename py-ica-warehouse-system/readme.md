# 🎯 SIMULADO SIMPLES — Sistema de Estoque
### Foco: Validações e Corner Cases (Sem Extras!) 🚀

---

## 📖 O Cenário: Sistema de Estoque

Uma loja que vende produtos. Só isso. Sem multas, sem limites malucos, sem coisa cheia.

---

## 🟢 Nível 1 — Operações Básicas

### `create_product(product_id: str, name: str, price: int) -> bool`
- Cria um produto
- **Validações:**
  - `product_id` vazio ou None → False
  - `name` vazio ou None → False
  - `price` <= 0 → False
  - Produto já existe → False

### `add_stock(product_id: str, quantity: int) -> bool`
- Adiciona estoque (quantidade) de um produto
- **Validações:**
  - Produto não existe → False
  - `quantity` <= 0 → False
- **Retorna:** True se bem-sucedido

### `remove_stock(product_id: str, quantity: int) -> int | None`
- Remove estoque de um produto
- **Validações:**
  - Produto não existe → None
  - `quantity` <= 0 → None
  - Quantidade > estoque → None (não pode vender mais do que tem!)
- **Retorna:** estoque restante APÓS remover
- **Guarda cada venda:** { product_id, quantity, timestamp }

### `get_product_info(product_id: str) -> dict | None`
```python
{
    "product_id": "mouse",
    "name": "Mouse Logitech",
    "price": 150,
    "current_stock": 5,
    "total_sold": 10  # Unidades vendidas até agora
}
```

---

## 🟡 Nível 2 — Análise Simples

### `get_sales_history(product_id: str) -> list[dict]`
- Retorna histórico de vendas do produto (mais recentes primeiro)
```python
[
    {"product_id": "mouse", "quantity": 2, "timestamp": 100},
    {"product_id": "mouse", "quantity": 3, "timestamp": 50}
]
```
- **Validações:**
  - Produto não existe → None
  - Nunca vendeu nada → retorna lista vazia []

### `best_seller() -> str | None`
- Qual produto foi mais vendido (por quantidade total)?
- **Validações:**
  - Nenhum produto criado → None
  - Nenhuma venda feita → None
- **Retorna:** product_id do mais vendido

### `total_revenue() -> int`
- Receita total da loja (preço * quantidade vendida)
- Validações: Se nada vendeu → 0

---

## 🧪 Exemplos de Teste (Focando Corner Cases)

```python
store = Warehouse()

# CORNER CASE 1: String vazia
store.create_product("", "Mouse", 100)  # False

# CORNER CASE 2: Preço 0 ou negativo
store.create_product("mouse", "Mouse", 0)  # False
store.create_product("mouse", "Mouse", -50)  # False

# CORNER CASE 3: Produto existe
store.create_product("mouse", "Mouse", 100)  # True
store.create_product("mouse", "Mouse", 100)  # False (já existe)

# CORNER CASE 4: Quantidade <= 0
store.add_stock("mouse", 0)  # False
store.add_stock("mouse", -5)  # False

# CORNER CASE 5: Produto não existe
store.remove_stock("teclado", 1)  # None (não existe)

# CORNER CASE 6: Vender mais do que tem
store.add_stock("mouse", 5)
store.remove_stock("mouse", 10)  # None (só tem 5!)

# CORNER CASE 7: Vender 0 ou negativo
store.remove_stock("mouse", 0)  # None
store.remove_stock("mouse", -1)  # None

# CORNER CASE 8: Vendeu tudo?
store.add_stock("mouse", 3)
store.remove_stock("mouse", 3)  # Retorna 0 (estoque zerou)

# CORNER CASE 9: Histórico vazio
store.get_sales_history("mouse")
# Se criou mas nunca vendeu → []

# CORNER CASE 10: Melhor vendedor quando nada foi vendido
store.create_product("teclado", "Teclado", 200)
store.best_seller()  # None (nada vendeu)
```

---

## 📝 Estrutura de Dados Recomendada

```python
def __init__(self):
    self.products = {
        "mouse": {
            "name": "Mouse Logitech",
            "price": 150,
            "stock": 5
        }
    }
    
    self.sales = {
        "mouse": [
            {"quantity": 2, "timestamp": 100},
            {"quantity": 3, "timestamp": 50}
        ]
    }
```

---

## 💪 Desafio

**60 minutos. Implemente os 2 níveis.**

Essa é **bem mais tranquila** que a biblioteca. Foco em:
- ✅ Validações rígidas
- ✅ Corner cases óbvios
- ✅ Estrutura de dados limpa

**Bora! 🚀**
