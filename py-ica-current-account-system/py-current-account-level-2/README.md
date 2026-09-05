# 🎯 Simulado 3 ICA — Nubank (CodeSignal) — Python
### O Terceiro Desafio: Sistema de Conta Corrente com Limites e Análise 🏦

Fala, meu guerreiro(a)! Terceira rodada, vem com TUDO! 

Você já domina o padrão dos 4 níveis progressivos. Agora a gente vai mexer com um cenário bem real de fintech: **operações de conta corrente, limites diários e análise de comportamento**.

Esse simulado vai testar seus conhecimentos de:
- Estruturas de dados complexas
- Validações e regras de negócio
- Análise e processamento de dados
- Relacionamento entre entidades

Vamo lá? 👇

---

## 📖 O Cenário: Sistema de Conta Corrente ("NubankAccount")

Você foi contratado(a) para construir o backend de contas correntes. Usuários vão:
- Criar contas
- Fazer saques e depósitos
- Ter limites diários de saque
- Ter histórico de transações bloqueadas
- Analisar padrões de gasto

**Tempo recomendado:** 90 minutos. **Dificuldade:** Progressiva.

---

## 🟢 Nível 1 — Operações Básicas (o Começo)

Implemente uma classe `CheckingAccount` com os seguintes métodos:

- `create_account(account_id: str, timestamp: int, initial_balance: int) -> bool`
  Cria uma nova conta. Retorna `True` se criou com sucesso, `False` se já existir.

- `get_balance(account_id: str) -> int | None`
  Retorna o saldo atual da conta. Se a conta não existir, retorna `None`.

- `deposit(account_id: str, timestamp: int, amount: int) -> int | None`
  Deposita dinheiro. Retorna o **novo saldo**. Retorna `None` se a conta não existir.

- `withdraw(account_id: str, timestamp: int, amount: int) -> int | None`
  Saca dinheiro. Retorna o **novo saldo**. Retorna `None` se:
  - A conta não existir OU
  - O saldo for insuficiente
  
  **Importante:** Cada saque precisa ser registrado com: valor, timestamp e status ("SUCCESS" ou "BLOCKED").

- `get_account_info(account_id: str) -> dict | None`
  Retorna informações da conta:
  ```python
  {
    "account_id": "user001",
    "balance": 5000,
    "total_deposits": 15000,
    "total_withdrawals": 10000,
    "total_transactions": 5  # número de saques + depósitos
  }
  ```

---

## 🟡 Nível 2 — Análise de Transações (os Insights)

Adicione:

- `get_transaction_history(account_id: str, limit: int) -> list[dict]`
  Retorna as últimas `limit` transações ordenadas por timestamp (mais recentes primeiro).
  
  Cada transação é:
  ```python
  {
    "type": "withdraw" ou "deposit",
    "amount": 500,
    "timestamp": 42,
    "balance_after": 4500
  }
  ```

- `daily_withdrawal_total(account_id: str, timestamp: int) -> int`
  Retorna quanto foi sacado **no mesmo dia** que o `timestamp` fornecido.
  (Dica: considere que um "dia" = 1440 minutos)

- `largest_transaction(account_id: str) -> dict | None`
  Retorna a **maior transação** (saque ou depósito) que a conta já fez.
  
  ```python
  {
    "type": "withdraw",
    "amount": 5000,
    "timestamp": 100
  }
  ```

---

## 🟠 Nível 3 — Limites e Bloqueios (a Segurança)

Adicione:

- `set_daily_limit(account_id: str, limit: int) -> bool`
  Define um limite de saque diário. Retorna `True` se conseguir, `False` se a conta não existir.

- `withdraw_with_limit(account_id: str, timestamp: int, amount: int) -> bool`
  Tenta sacar com base no limite diário.
  
  **Regras:**
  - Se o saque + (já sacado hoje) > limite diário → **bloqueado**
  - Se bloquear, registra na lista de "transações bloqueadas"
  - Retorna `True` se bem-sucedido, `False` se bloqueado ou saldo insuficiente

- `get_blocked_transactions(account_id: str) -> list[dict]`
  Retorna todas as transações que foram **bloqueadas** pela conta.
  
  ```python
  {
    "amount": 10000,
    "timestamp": 150,
    "reason": "daily_limit_exceeded"  # ou "insufficient_balance"
  }
  ```

- `get_daily_limit_info(account_id: str, timestamp: int) -> dict | None`
  Retorna informações sobre o limite do dia:
  
  ```python
  {
    "daily_limit": 5000,
    "withdrawn_today": 2000,
    "remaining_today": 3000,
    "timestamp": 150
  }
  ```

---

## 🔴 Nível 4 — Análise Avançada (os Relatórios)

Adicione:

- `detect_unusual_activity(account_id: str, current_timestamp: int) -> bool`
  Detecta se houve atividade incomum (muitos saques em pouco tempo, saques maiores que o padrão, etc).
  
  **Critérios:**
  - Se fez mais de 5 transações em 60 minutos → `True`
  - Se algum saque > 2x a média histórica → `True`
  - Caso contrário → `False`

- `get_spending_pattern(account_id: str) -> dict`
  Retorna análise do padrão de gastos:
  
  ```python
  {
    "average_withdrawal": 450,
    "average_deposit": 3000,
    "most_active_hour": 14,  # hora do dia (0-23, baseado em minutos)
    "total_activity_days": 7  # quantos "dias" diferentes teve transação
  }
  ```

- `account_summary(account_id: str, current_timestamp: int) -> dict`
  Retorna um resumo completo da conta:
  
  ```python
  {
    "account_id": "user001",
    "current_balance": 4500,
    "total_deposited": 15000,
    "total_withdrawn": 10500,
    "daily_limit": 5000,
    "remaining_limit_today": 3000,
    "blocked_transactions_count": 2,
    "unusual_activity_detected": False,
    "average_withdrawal": 500,
    "total_transactions": 21
  }
  ```

---

## 🧪 Testes de Corner Case

Antes de começar, pensa nessas situações:

- ✓ Sacar de conta que não existe
- ✓ Depositar com valor negativo
- ✓ Sacar mais que o limite diário (bloqueado)
- ✓ Muitos saques em pouco tempo (atividade incomum)
- ✓ Sacar valor maior que a média histórica
- ✓ Consultar histórico de conta com poucas transações

---

## 🎓 Dicas de Ouro

1. **Guarde tudo com timestamp:** Cada transação precisa saber quando aconteceu.

2. **Um "dia" = 1440 minutos:** Quando você verificar limite diário, separe por períodos de 1440 minutos.

3. **Transações bloqueadas são importantes:** Guarde num lugar separado pra depois consultar.

4. **Análise de padrão:** Calcule médias, conte transações, compare com histórico.

5. **Estrutura clara desde o início:** `__init__` bem pensado = código fluido.

---

## 📝 Checklist Antes de Começar

- [ ] Entendi que é um projeto único que cresce
- [ ] Entendi que timestamps estão em minutos
- [ ] Entendi que limite diário funciona por período de 1440 minutos
- [ ] Entendi que preciso rastrear transações bloqueadas
- [ ] Estou pronto pra estruturar bem a classe desde o `__init__`

---

## 💪 Seu Turno!

**Não olha no gabarito antes!** Tenta implementar os 4 níveis sozinho(a). 

Dessa vez você vai fazer de verdade sem minha ajuda — eu só vou revisar quando você chamar!

Se ficar muito preso, me chama pra destrinchar o **conceito**, não o código!

Bora codar! 🚀🐍

---

## 🏁 Bora!

Esse é seu teste real de aprendizado. Você consegue! 💪

Boa sorte e que a força esteja com você! 🌟
