# 🎯 Simulado 2 ICA — Nubank (CodeSignal) — Python
### O Próximo Desafio: Sistema de Limite de Crédito e Fatura 💳

Fala, guerreiro(a)! Segunda rodada, vem com tudo! Dessa vez a gente tira a cartilha direto de como funciona **de verdade** em uma fintech como Nubank.

Você já dominou o padrão (4 níveis progressivos, cada um construindo em cima do anterior). Agora vamos explorar um sistema bem mais realista: **gestão de crédito, faturas e pagamentos**.

Lembra do padrão? **Um projeto único que cresce**. O código que você escreve no Nível 1 vai ser reutilizado, estendido e refinado nos níveis seguintes. Isso é o ICA.

Vamo lá? 👇

---

## 📖 O Cenário: Sistema de Cartão de Crédito ("NubankPy")

Você foi contratado(a) para construir o backend de um sistema de cartão de crédito simples. Usuários vão:
- Criar cartões com limite
- Fazer compras (gastando crédito)
- Receber faturas em datas específicas
- Pagar faturas

**Tempo recomendado:** 90 minutos. **Dificuldade:** Progressiva.

---

## 🟢 Nível 1 — Operações Básicas (o Alicerce)

Implemente uma classe `CreditCard` com os seguintes métodos:

- `create_card(card_id: str, timestamp: int, credit_limit: int) -> bool`
  Cria um novo cartão com um limite de crédito. Retorna `True` se criou com sucesso, `False` se o cartão já existir.

- `get_available_balance(card_id: str) -> int | None`
  Retorna quanto de crédito ainda está disponível. Se o cartão não existir, retorna `None`.
  Fórmula: `available = credit_limit - amount_used`

- `make_purchase(card_id: str, timestamp: int, amount: int, category: str) -> bool`
  Registra uma compra. Retorna `True` se bem-sucedida, `False` se o cartão não existir ou não tiver saldo suficiente.
  
  **Importante:** Você precisa guardar cada compra com:
  - O valor
  - A categoria (tipo: "alimentação", "uber", "streaming")
  - O timestamp de quando foi feita

- `get_card_balance(card_id: str) -> dict | None`
  Retorna um dicionário com informações do cartão:
  ```python
  {
    "credit_limit": 5000,
    "amount_used": 1200,
    "available_balance": 3800,
    "total_purchases": 5  # número de compras realizadas
  }
  ```

**Dica:** Você vai precisar guardar, para cada cartão:
- Seu limite
- Quanto já foi gasto
- Todas as compras (pra poder analisar depois)

---

## 🟡 Nível 2 — Análise de Gastos (os Insights)

Adicione:

- `top_spending_categories(card_id: str, n: int) -> list[tuple[str, int]]`
  Retorna as **N categorias** em que o usuário mais gastou, ordenadas pela maior despesa primeiro.
  
  **Formato de retorno:**
  ```python
  [("alimentação", 800), ("uber", 500), ("streaming", 200)]
  ```
  
  Em caso de empate, ordena pela categoria em ordem alfabética.

- `spending_by_period(card_id: str, start_timestamp: int, end_timestamp: int) -> int`
  Retorna quanto foi gasto em um período específico (entre `start_timestamp` e `end_timestamp`, inclusive ambos).

- `get_purchase_history(card_id: str) -> list[dict]`
  Retorna **todas as compras** do cartão, ordenadas por timestamp (mais recentes primeiro).
  
  Cada compra é um dicionário:
  ```python
  {
    "amount": 150,
    "category": "uber",
    "timestamp": 42
  }
  ```

---

## 🟠 Nível 3 — Fatura e Pagamento (o Núcleo do Negócio)

Adicione:

- `create_invoice(card_id: str, timestamp: int, invoice_timestamp: int) -> str | None`
  Cria uma fatura. Retorna um `invoice_id` no formato `"invoice1"`, `"invoice2"`, etc.
  
  **O que é uma fatura:**
  - Agrupa todas as compras não pagas de um período
  - Tem uma data de vencimento (`invoice_timestamp + 2880` minutos = 48h, pra simplificar)
  - Começa com status `"OPEN"`
  
  **Regra importante:** Uma fatura só pode incluir compras feitas **antes do timestamp da fatura**. Compras depois não entram nela.

- `pay_invoice(card_id: str, timestamp: int, invoice_id: str, amount: int) -> bool`
  Faz um pagamento de fatura.
  
  **Regras:**
  - `amount` deve ser maior que zero e menor ou igual ao valor total da fatura
  - Se `amount` >= valor total, a fatura fica com status `"PAID"`
  - Se `amount` < valor total, a fatura fica com status `"PARTIALLY_PAID"` (e há saldo restante)
  - Compras pagas não entram na próxima fatura
  - Retorna `True` se bem-sucedido, `False` caso contrário

- `get_invoice_status(card_id: str, invoice_id: str) -> dict | None`
  Retorna o status completo de uma fatura:
  ```python
  {
    "invoice_id": "invoice1",
    "total_amount": 1500,
    "paid_amount": 500,
    "remaining_amount": 1000,
    "status": "PARTIALLY_PAID",  # ou "OPEN", ou "PAID"
    "due_timestamp": 2880
  }
  ```

**Dica de design:** Você vai precisar rastrear:
- Qual compra foi paga ou não
- Qual fatura agrupa quais compras
- Quanto ainda falta pagar em cada fatura

---

## 🔴 Nível 4 — Complexidade Total (os Desafios Reais)

Adicione:

- `transfer_credit_limit(from_card_id: str, to_card_id: str, timestamp: int, amount: int) -> bool`
  Transfere limite de crédito de um cartão pra outro.
  
  **Regras:**
  - Ambos os cartões devem existir
  - O cartão de origem deve ter saldo disponível suficiente (não pode ficar devendo)
  - Retorna `True` se bem-sucedido, `False` caso contrário

- `get_spending_forecast(card_id: str, current_timestamp: int) -> dict`
  Prevê quanto será gasto no **próximo período de fatura** (baseado na média histórica).
  
  **Retorna:**
  ```python
  {
    "average_spending_per_day": 150,
    "estimated_next_invoice_total": 7200,  # 48 dias * 150/dia
    "recommendation": "increase_limit"  # ou "no_action"
  }
  ```
  
  **Lógica:**
  - Calcula quanto foi gasto por dia (em média) até agora
  - Projeta pro próximo período de fatura (48 horas = 2880 minutos)
  - Se a previsão > 80% do limite, retorna `"increase_limit"`
  - Se a previsão <= 80% do limite, retorna `"no_action"`

- `get_account_snapshot(card_id: str, timestamp: int) -> dict`
  Retorna um "snapshot" completo da situação do cartão em um determinado momento:
  
  ```python
  {
    "card_id": "card001",
    "credit_limit": 5000,
    "available_balance": 2000,
    "total_spent": 3000,
    "open_invoices": 2,
    "total_invoice_balance": 1500,
    "purchases_this_period": 12,
    "avg_purchase_value": 250
  }
  ```

---

## 🧪 Testes de Corner Case

Antes de começar, pensa nessas situações:

- ✓ Tentar fazer compra com cartão inexistente
- ✓ Tentar fazer compra maior que o limite
- ✓ Fazer compra, criar fatura, depois fazer mais uma compra (qual entra na fatura?)
- ✓ Pagar fatura parcialmente e depois criar nova fatura (o restante entra na nova?)
- ✓ Transferir limite entre cartões
- ✓ Consultar status de fatura inexistente

---

## 🎓 Dicas de Ouro pra Você

1. **Estrutura de dados:** Use dicionários pra tudo. Pra compras, use uma **lista de dicionários** dentro de cada cartão.

2. **Timestamp em minutos:** Lembra disso ainda? 48 horas = 2880 minutos.

3. **Rastreabilidade:** Cada compra precisa saber se já foi paga ou não. Você pode colocar uma flag tipo `"paid": False` em cada compra.

4. **Faturas agrupam compras:** Uma fatura não é um número mágico — é um **agrupamento de compras**. Pensa bem em como guardar isso.

5. **Integração:** O Nível 3 mexe bastante no Nível 1 e 2. Estrutura bem desde o início!

---

## 📝 Checklist antes de começar

- [ ] Entendi que é um projeto único que cresce
- [ ] Entendi que timestamps estão em minutos
- [ ] Entendi que compras precisam ser rastreáveis (pagas vs não pagas)
- [ ] Entendi que faturas agrupam compras de um período
- [ ] Estou pronto pra estruturar bem a classe desde o `__init__`

---

## 💪 Seu Turno!

**Não olha no gabarito antes!** Tenta implementar os 4 níveis sozinho(a). Se travar em algum ponto específico, me chama e a gente destrincha junto.

Boa sorte e bora codar! 🚀🐍

