# 🎯 SIMULADO 4 — Sistema de Agendamento de Salas
### 2 Níveis · Validações · Corner Cases 🏫

---

## 📖 O Cenário

Um sistema de reserva de salas de reunião. Salas são cadastradas, pessoas fazem reservas em horários (timestamps), e o sistema precisa impedir conflitos e gerar relatórios.

---

## 🟢 Nível 1 — Cadastro e Reservas

### `create_room(room_id: str, name: str, capacity: int) -> bool`
- Cadastra uma sala
- **Validações:**
  - `room_id` vazio ou None → False
  - `name` vazio ou None → False
  - `capacity` <= 0 → False
  - Sala já existe → False

### `book_room(room_id: str, user_id: str, start: int, end: int) -> bool`
- Reserva uma sala para um usuário no intervalo `[start, end)`
- **Validações:**
  - Sala não existe → False
  - `user_id` vazio ou None → False
  - `start` < 0 ou `end` < 0 → False
  - `start` >= `end` → False (intervalo inválido)
  - **Conflito:** se já existe reserva que se sobrepõe ao intervalo → False
  - Sobreposição: dois intervalos `[a, b)` e `[c, d)` conflitam quando `a < d` e `c < b`
  - Intervalos que apenas **encostam** (ex: `[10, 20)` e `[20, 30)`) NÃO conflitam
- **Guarda:** user_id, start, end

### `get_room_info(room_id: str) -> dict | None`
```python
{
    "room_id": "sala_a",
    "name": "Sala Alpha",
    "capacity": 10,
    "total_bookings": 3
}
```
- **Validações:**
  - Sala não existe → None

---

## 🟡 Nível 2 — Consultas e Relatórios

### `get_room_schedule(room_id: str) -> list[dict]`
- Retorna todas as reservas da sala **ordenadas por `start`** (crescente)
```python
[
    {"user_id": "ana", "start": 10, "end": 20},
    {"user_id": "bruno", "start": 30, "end": 45}
]
```
- **Validações:**
  - Sala não existe → None
  - Sala sem reservas → []

### `user_bookings(user_id: str) -> list[dict]`
- Retorna todas as reservas de um usuário, em **todas as salas**
- Cada item inclui o `room_id`
```python
[
    {"room_id": "sala_a", "start": 10, "end": 20},
    {"room_id": "sala_b", "start": 50, "end": 60}
]
```
- **Ordenado:** por `start` (crescente), desempate por `room_id` (alfabético)
- **Validações:**
  - `user_id` vazio ou None → []
  - Usuário sem reservas → []

### `most_booked_room() -> str | None`
- Retorna o `room_id` da sala com **mais reservas**
- **Desempate:** ordem alfabética do `room_id`
- **Validações:**
  - Nenhuma sala cadastrada → None
  - Nenhuma reserva feita → None

---

## 🧪 Exemplos de Corner Cases

```python
s = Scheduler()

# CORNER CASE 1: Capacidade inválida
s.create_room("sala_a", "Alpha", 0)        # False

# CORNER CASE 2: Intervalo inválido
s.book_room("sala_a", "ana", 20, 10)       # False (start > end)
s.book_room("sala_a", "ana", 10, 10)       # False (start == end)

# CORNER CASE 3: Conflito parcial
s.book_room("sala_a", "ana", 10, 20)       # True
s.book_room("sala_a", "bruno", 15, 25)     # False (sobrepõe)

# CORNER CASE 4: Encostado NÃO é conflito
s.book_room("sala_a", "carla", 20, 30)     # True

# CORNER CASE 5: Sala inexistente
s.get_room_schedule("sala_x")              # None
s.get_room_schedule("sala_a")              # lista ordenada por start

# CORNER CASE 6: Sistema vazio
s2 = Scheduler()
s2.most_booked_room()                      # None
```

---

## 📝 Estrutura de Dados Sugerida

```python
def __init__(self):
    self.rooms = {
        "sala_a": {"name": "Alpha", "capacity": 10}
    }
    self.bookings = {
        "sala_a": [
            {"user_id": "ana", "start": 10, "end": 20}
        ]
    }
```

Pense: por que `bookings` é um dicionário de **listas** e não uma lista única?

---

## 💪 Desafio

**60 minutos. Implemente os 2 níveis.**

Antes de codificar, faça o template mental:
1. Qual é o padrão?
2. Desenhe os dados
3. Valide a entrada

**Bora! 🚀**
