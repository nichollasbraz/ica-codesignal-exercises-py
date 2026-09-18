# 🎯 SIMULADO 2.0 — Corner Cases & Validações Rigorosas
### Para o Próximo Teste Técnico 🚀

---

## 📖 O Cenário: Sistema de Biblioteca ("NuBank Library")

Um sistema de gerenciamento de biblioteca onde leitores podem pegar livros emprestados e devolá-los com multas por atraso.

**Por que esse cenário?**
- Força validações em cascata
- Testes com valores extremos
- Cálculos com múltiplas condições
- Histórico que interage com presentes

---

## 🟢 Nível 1 — Operações Básicas (COM VALIDAÇÕES!)

Implemente a classe `Library` com:

### `create_reader(reader_id: str, timestamp: int) -> bool`
- Cria um leitor na biblioteca
- **Corner Cases:**
  - `reader_id` vazio ("") → False
  - `reader_id` já existe → False
  - `timestamp` negativo → aceita (pode ser timestamp de antes da época Unix)
  - `timestamp` 0 → aceita

### `add_book(book_id: str, title: str, quantity: int) -> bool`
- Adiciona um livro (mesmo livro pode ter múltiplas cópias)
- **Corner Cases:**
  - `book_id` vazio ("") → False
  - `title` vazio ("") → False
  - `quantity` <= 0 → False
  - Mesmo `book_id` já existe → atualiza quantidade (não falha!)

### `borrow_book(reader_id: str, book_id: str, timestamp: int) -> bool`
- Leitor pega emprestado um livro
- Tira 1 unidade do estoque
- **Guarda:** quem pegou, qual livro, quando pegou
- **Corner Cases:**
  - Leitor não existe → False
  - Livro não existe → False
  - Sem estoque disponível → False
  - `reader_id` vazio → False
  - Mesmo leitor tenta pegar 2x o mesmo livro sem devolver → ??? (você decide!)

### `get_reader_info(reader_id: str) -> dict | None`
- Retorna:
```python
{
    "reader_id": "alice",
    "books_borrowed": 2,        # Livros que ainda está com
    "books_returned": 1,        # Livros que já devolveu
    "total_fines_paid": 0,      # Multas já pagas
    "current_fine": 0           # Multa pendente
}
```
- **Corner Cases:**
  - Leitor não existe → None
  - Leitor existe mas nunca pegou nada → todos os valores = 0

---

## 🟡 Nível 2 — Devoluções e Cálculo de Multas

### `return_book(reader_id: str, book_id: str, timestamp: int) -> dict | None`
- Leitor devolve um livro
- Calcula multa se estiver atrasado
- **Regras:**
  - Prazo de devolução: 1440 minutos (1 dia) após pegar
  - Multa: 10 pontos por minuto de atraso
- **Retorna:**
```python
{
    "reader_id": "alice",
    "book_id": "1984",
    "borrowed_at": 100,
    "returned_at": 2000,
    "due_date": 1540,           # borrowed_at + 1440
    "days_late": 1,             # floor((returned_at - due_date) / 1440)
    "fine_amount": 4600,        # (returned_at - due_date) * 10
    "fine_paid": False          # Leitor pagou multa?
}
```
- **Corner Cases:**
  - Leitor não tem esse livro emprestado → None
  - Leitor nunca pegou nada → None
  - Devolveu no prazo (fine_amount = 0) → retorna dict mesmo assim
  - Devolveu 1 minuto antes do prazo → fine_amount = 0
  - Devolveu EXATAMENTE no due_date → fine_amount = 0
  - Devolveu com huge atraso (10.000 minutos) → calcula normal
  - `timestamp` < borrowed_at (devolveu antes de pegar?) → ??? (você decide!)

### `get_fine_status(reader_id: str) -> dict | None`
- Retorna todas as multas (pagas e não pagas):
```python
{
    "reader_id": "alice",
    "total_fines": 4600,        # Todas as multas geradas
    "paid_fines": 0,            # Já pagou
    "pending_fines": 4600,      # Ainda deve
    "fine_history": [
        {
            "book_id": "1984",
            "fine_amount": 4600,
            "paid": False,
            "returned_at": 2000
        }
    ]
}
```
- **Corner Cases:**
  - Leitor não existe → None
  - Leitor nunca pegou nada → retorna dict com 0s
  - Leitor pagou todas as multas → pending_fines = 0

### `pay_fine(reader_id: str, amount: int) -> bool`
- Leitor paga multa
- **Regras:**
  - Paga multas mais antigas primeiro (FIFO)
  - Se `amount` > multa pendente total → só paga o que deve
- **Corner Cases:**
  - Leitor não existe → False
  - `amount` <= 0 → False
  - Não tem multa pendente → False
  - `amount` > multa total → True (paga tudo que pode)

---

## 🟠 Nível 3 — Restrições e Limites

### `set_borrow_limit(reader_id: str, max_books: int) -> bool`
- Define quantos livros o leitor pode ter emprestado simultaneamente
- **Corner Cases:**
  - `max_books` <= 0 → False
  - `max_books` > 1000 → False (limite sensato)
  - Leitor não existe → False

### `borrow_book_with_limit(reader_id: str, book_id: str, timestamp: int) -> bool`
- Tenta pegar emprestado respeitando limite
- **Corner Cases:**
  - Leitor já tem limite de livros atingido → False
  - Leitor tem multa pendente → False (bloqueia empréstimo!)
  - Mesmo livro já pegou mas não devolveu → ??? (você decide!)

### `get_borrowing_history(reader_id: str) -> list[dict]`
- Retorna histórico de empréstimos (todos, pagos e não pagos):
```python
[
    {
        "book_id": "1984",
        "borrowed_at": 100,
        "returned_at": 2000,
        "was_late": True,
        "fine_amount": 4600
    },
    {
        "book_id": "Brave New World",
        "borrowed_at": 300,
        "returned_at": None,        # Ainda tem emprestado!
        "was_late": False,
        "fine_amount": 0
    }
]
```
- **Corner Cases:**
  - Leitor não existe → None
  - Leitor nunca pegou livro → retorna lista vazia []
  - Livros emprestados (sem devolver) → returned_at = None

---

## 🔴 Nível 4 — Análise Avançada

### `get_most_borrowed_books(n: int) -> list[tuple[str, int]]`
- Top N livros mais pegados (total de vezes):
```python
[("1984", 15), ("Brave New World", 12), ("Dune", 8)]
```
- **Corner Cases:**
  - `n` <= 0 → return []
  - `n` > total de livros → retorna todos
  - Nenhum livro foi pegado → return []

### `get_reader_with_most_fines() -> dict | None`
- Leitor que mais tem multa:
```python
{
    "reader_id": "bob",
    "total_fines": 25000,
    "pending_fines": 10000,
    "books_borrowed_count": 20
}
```
- **Corner Cases:**
  - Nenhum leitor tem multa → None
  - Múltiplos leitores com mesma multa máxima → retorna o primeiro

### `system_summary() -> dict`
```python
{
    "total_readers": 5,
    "total_books": 10,
    "active_borrows": 8,        # Livros que estão com leitor
    "total_fines_generated": 50000,
    "total_fines_paid": 30000,
    "average_fine_per_late_return": 5000,
    "books_in_stock": 25,       # Total de cópias disponíveis
    "overdue_books": 3          # Livros que passaram do prazo
}
```

---

## 🧪 Exemplos de Teste (Corner Cases!)

```python
lib = Library()

# CORNER CASE 1: Leitor vazio
lib.create_reader("", 0)  # False

# CORNER CASE 2: Quantidade 0
lib.add_book("1984", "1984", 0)  # False

# CORNER CASE 3: Sem estoque
lib.add_book("1984", "1984", 1)
lib.borrow_book("alice", "1984", 100)  # True
lib.borrow_book("bob", "1984", 110)    # False (sem estoque)

# CORNER CASE 4: Devolveu no prazo exato
lib.add_book("1984", "1984", 1)
lib.create_reader("alice", 0)
lib.borrow_book("alice", "1984", 100)
lib.return_book("alice", "1984", 1540)  # due_date = 1540, fine = 0

# CORNER CASE 5: Multa pendente bloqueia empréstimo
lib.create_reader("charlie", 0)
lib.add_book("Dune", "Dune", 1)
lib.borrow_book("charlie", "1984", 100)
lib.return_book("charlie", "1984", 2000)  # 460 minutos de atraso = 4600 de multa
lib.borrow_book_with_limit("charlie", "Dune", 2050)  # False (tem multa pendente!)

# CORNER CASE 6: Pagar mais do que deve
lib.pay_fine("charlie", 10000)  # True (paga os 4600 que deve, sobra 5400)

# CORNER CASE 7: Histórico com alguns ainda emprestados
lib.borrow_book("charlie", "Dune", 2100)
history = lib.get_borrowing_history("charlie")
# Tem 2 livros: 1984 (devolvido) e Dune (ainda emprestado)
```

---

## 📝 Dicas Finais

1. **Pense na estrutura ANTES de codificar:**
   - Precisa guardar empréstimo atual (não devolvido)?
   - Precisa guardar histórico completo?
   - Como saber se um livro tá emprestado?

2. **Valide TUDO:**
   - Strings vazias?
   - Valores <= 0?
   - Índices fora do range?
   - Estados impossíveis?

3. **Casos de Cascata:**
   - Se não tem livro, não pode devolver
   - Se tem multa, não pode pegar novo
   - Se paga multa, pode pegar novo

4. **Teste mentalmente:**
   - Pegou 1 livro, devolveu com atraso, pagou multa, pegou outro
   - 2 leitores pegam o mesmo livro (em cópias diferentes)
   - Leitor paga multa parcial

---

## 💪 Seu Desafio

**90 minutos. Implemente tudo.**

Dessa vez, quando tiver dúvida sobre corner case, PENSA PRIMEIRO antes de me chamar!

**Você consegue! Agora você já sabe o que procurar! 🚀**
