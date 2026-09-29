# 🎯 SIMULADO 3 — Sistema de Placar de Competição
### Foco: Validações, Ordenação e Corner Cases 🏆

---

## 📖 O Cenário: Placar de Campeonato

Um sistema simples de placar onde jogadores competem em rodadas e ganham pontos. Sem times, sem multas, sem chateação — só placar!

---

## 🟢 Nível 1 — Operações Básicas

### `create_player(player_id: str, name: str) -> bool`
- Cria um novo jogador
- **Validações:**
  - `player_id` vazio ou None → False
  - `name` vazio ou None → False
  - Player já existe → False
  - Começa com **0 pontos**

### `add_points(player_id: str, points: int, round_number: int) -> bool`
- Adiciona pontos a um jogador em uma rodada
- **Validações:**
  - Player não existe → False
  - `points` é negativo? ACEITA (pode perder pontos!)
  - `points` é 0? ACEITA
  - `round_number` <= 0 → False
  - Mesmo player já fez registro na mesma rodada? ??? (você decide!)
- **Guarda:** player_id, points, round_number, timestamp

### `get_player_info(player_id: str) -> dict | None`
```python
{
    "player_id": "alice",
    "name": "Alice Silva",
    "total_points": 150,
    "total_rounds": 3,
    "average_points_per_round": 50  # floor(150 / 3)
}
```

### `get_leaderboard() -> list[tuple[str, int]]`
- Retorna ranking de jogadores (nome, pontos totais)
- **Ordenado:** Maior pontuação primeiro, desempate alfabético
- **Formato:** `[("Alice", 150), ("Bob", 120)]`
- **Validações:**
  - Nenhum player criado → []

---

## 🟡 Nível 2 — Análise de Desempenho

### `best_round(player_id: str) -> dict | None`
- Qual foi a melhor rodada do jogador?
```python
{
    "player_id": "alice",
    "round_number": 2,
    "points": 75
}
```
- **Validações:**
  - Player não existe → None
  - Player nunca jogou → None

### `worst_round(player_id: str) -> dict | None`
- Qual foi a pior rodada? (menor pontuação)
- Mesmo formato que `best_round`

### `get_round_results(round_number: int) -> list[dict]`
- Retorna TODOS os jogadores e suas pontuações em uma rodada
```python
[
    {"player_id": "alice", "name": "Alice", "points": 50},
    {"player_id": "bob", "name": "Bob", "points": 45}
]
```
- **Ordenado:** Maior pontuação primeiro
- **Validações:**
  - `round_number` <= 0 → None
  - Ninguém jogou nessa rodada → []

### `player_history(player_id: str) -> list[dict]`
- Histórico de todas as rodadas do jogador
```python
[
    {"round_number": 1, "points": 50},
    {"round_number": 2, "points": 75},
    {"round_number": 3, "points": 25}
]
```
- **Ordenado:** Por round_number (ascendente)
- **Validações:**
  - Player não existe → None
  - Player nunca jogou → []

---

## 🟠 Nível 3 — Filtros e Rankings

### `players_above_average() -> list[tuple[str, int]]`
- Retorna jogadores com pontuação acima da média geral
- **Formato:** `[("Alice", 150), ("Bob", 120)]`
- **Validações:**
  - Nenhum player → []
  - Todos abaixo da média → []

### `get_round_winner(round_number: int) -> str | None`
- Quem venceu a rodada? (maior pontuação naquela rodada)
- **Validações:**
  - `round_number` <= 0 → None
  - Ninguém jogou → None
  - Empate (2 players com mesma pontuação)? Retorna o primeiro (ordem de id)

### `round_range_points(round_start: int, round_end: int) -> dict`
- Total de pontos de cada player entre rodadas (inclusive)
```python
{
    "alice": 150,
    "bob": 100
}
```
- **Validações:**
  - `round_start` > `round_end` → {}
  - `round_start` <= 0 ou `round_end` <= 0 → {}
  - Nenhum player nesse range → {}

---

## 🔴 Nível 4 — Análises Avançadas

### `competition_stats() -> dict`
- Resumo estatístico da competição
```python
{
    "total_players": 3,
    "total_rounds": 4,
    "average_points_all": 45,           # Média geral de todos
    "highest_score": 100,               # Maior pontuação individual
    "lowest_score": -10,                # Menor (pode ser negativa!)
    "highest_single_round": 90          # Maior pontuação em uma rodada
}
```

### `inconsistency_check() -> list[str]`
- Retorna player_ids com desempenho inconsistente
- **Lógica:** Variação grande entre melhor e pior rodada
  - Se (best - worst) > média_geral * 1.5 → inconsistente
  - Formato: lista de player_ids ordenada alfabeticamente
- **Validações:**
  - Nenhum player → []

---

## 🧪 Exemplos de Corner Cases

```python
# CORNER CASE 1: Pontos negativos
add_points("alice", -10, 1)  # True (aceita!)

# CORNER CASE 2: Zero pontos
add_points("bob", 0, 1)  # True (aceita!)

# CORNER CASE 3: Pior rodada é negativa
player = get_player_info("alice")
# Se alice tiver [-10, 50, 30], worst_round é -10

# CORNER CASE 4: Average com divisão
# alice: 100 pontos em 3 rodadas = 33 (floor)
average = 100 // 3  # = 33

# CORNER CASE 5: Empate no leaderboard
# alice: 100
# bob: 100
# Resultado: [("alice", 100), ("bob", 100)]  (alfabético)

# CORNER CASE 6: Ninguém acima da média
# alice: 10, bob: 20
# Média: 15
# players_above_average() → [("bob", 20)]

# CORNER CASE 7: Rodada inexistente
get_round_results(999)  # []

# CORNER CASE 8: Comparação de ranges
round_range_points(5, 3)  # {} (start > end)
```

---

## 📝 Estrutura de Dados Recomendada

```python
def __init__(self):
    self.players = {
        "alice": {
            "name": "Alice Silva",
            "total_points": 150
        }
    }
    
    self.scores = {
        "alice": [
            {"round_number": 1, "points": 50},
            {"round_number": 2, "points": 75},
            {"round_number": 3, "points": 25}
        ]
    }
```

---

## 💪 Desafio

**120 minutos. Implemente os 4 níveis.**

Dicas:
- ✅ Pontos podem ser negativos ou zero
- ✅ Sempre valide entrada
- ✅ Ordenação é crítica (maior primeiro, desempate alfabético)
- ✅ Divisão com `//` (floor, não float)
- ✅ Corner cases com empate, rodadas vazias, etc

**Você consegue! 🚀**
