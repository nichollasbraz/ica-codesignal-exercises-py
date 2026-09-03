# 🎯 Simulado ICA — Nubank (CodeSignal) — Python
### E aí, salve salve! Bora treinar juntos? 💪

Fala, futuro(a) estagiário(a)! Aqui quem fala é o seu parceiro de código — e hoje a gente vai simular exatamente o tipo de prova que você vai encontrar no ICA (Industry Coding Assessment) da CodeSignal, que é o formato usado pelo Nubank.

Antes de mais nada, deixa eu te explicar uma coisa importante: **o ICA não é tipo aquele monte de exercício solto do LeetCode**. É **um projeto único**, que vai crescendo em complexidade a cada nível. Ou seja: o que você constrói no Nível 1 vai ser usado (e ampliado) no Nível 2, 3 e 4. É tipo construir uma casa: primeiro a fundação, depois as paredes, depois o telhado. Se a fundação estiver torta, o resto desmorona. Por isso a organização do seu código desde o começo é TUDO.

Bora pro cenário? 👇

---

## 📖 O Cenário: Sistema de Carteira Digital ("PyPay")

Você foi contratado(a) para construir o backend de uma carteira digital simples. O sistema vai evoluir em 4 níveis. **Tente resolver cada nível sozinho(a) antes de olhar o gabarito lá no final do arquivo!** Essa é a parte mais importante — se você só ler a solução, seu cérebro não vai criar o "caminho neural" de como resolver isso na hora do aperto.

Recomendo: cronometre 90 minutos, abra um editor Python (VS Code, PyCharm, ou até o `python3` no terminal) e vai tentando level por level, igual no teste real.

---

## 🟢 Nível 1 — Operações Básicas (o "arroz com feijão")

Implemente uma classe `Wallet` (carteira) com os seguintes métodos:

- `create_account(account_id: str, timestamp: int) -> bool`
  Cria uma nova conta com saldo zero. Retorna `True` se criou com sucesso, `False` se a conta já existir.

- `deposit(account_id: str, timestamp: int, amount: int) -> int | None`
  Deposita um valor na conta. Retorna o **novo saldo**. Se a conta não existir, retorna `None`.

- `withdraw(account_id: str, timestamp: int, amount: int) -> int | None`
  Saca um valor da conta. Retorna o **novo saldo**. Se a conta não existir OU não tiver saldo suficiente, retorna `None` (e o saldo não muda).

**Dica de quem já passou por isso:** No ICA de verdade, cada método desses é testado com "corner cases" (casos extremos) — tipo tentar depositar numa conta que não existe, ou sacar mais do que tem. Sempre pensa: "e se o valor for zero? E se a conta não existir? E se for negativo?"

---

## 🟡 Nível 2 — Processamento de Dados (agora fica mais gostoso)

Adicione ao seu `Wallet`:

- `transfer(from_id: str, to_id: str, timestamp: int, amount: int) -> bool`
  Transfere dinheiro entre contas. Retorna `True` se a transferência foi bem-sucedida. Deve falhar (`False`) se qualquer uma das contas não existir ou se o saldo for insuficiente.

- `top_spenders(timestamp: int, n: int) -> list[str]`
  Retorna os **N** IDs de conta que mais **gastaram** (soma de saques + valores enviados em transferências), ordenados do maior gasto para o menor. Em caso de empate, ordena pelo `account_id` em ordem alfabética crescente.

**Sacada importante:** Repara que `top_spenders` depende do histórico que você guardou desde o Nível 1! Por isso eu já avisei: pensa na estrutura de dados certa desde o início. Uma dica de ouro é guardar, para cada conta, um "total gasto" que você vai atualizando a cada saque/transferência, em vez de recalcular tudo toda hora.

---

## 🟠 Nível 3 — Regras de Negócio (aqui separa quem treinou de quem não treinou)

Adicione:

- `pay_with_cashback(account_id: str, timestamp: int, amount: int, cashback_percentage: float) -> str`
  Faz um pagamento com cashback. O cashback é **creditado 24h depois** (considere que os timestamps estão em **minutos**, então 24h = 1440 minutos). Retorna um `payment_id` no formato `"payment{numero_sequencial}"` (ex: `"payment1"`, `"payment2"`...).

- `get_payment_status(account_id: str, timestamp: int, payment_id: str) -> str | None`
  Retorna o status do pagamento: `"IN_PROGRESS"` se o cashback ainda não caiu, ou `"CASHBACK_RECEIVED"` se já passou o tempo. Retorna `None` se o pagamento não existir.

**Dica de leitura de enunciado (isso é PARA VALER):** repara que eu escrevi "considere que os timestamps estão em minutos". No teste real, esse tipo de detalhe geralmente vem escondido em uma frase no meio do parágrafo — e é fácil de passar batido. Sempre sublinhe (ou anote num rascunho) os números e unidades que aparecem no enunciado.

---

## 🔴 Nível 4 — Complexidade Total (é aqui que separam os campeões)

Adicione:

- `merge_accounts(account_id_1: str, account_id_2: str, timestamp: int) -> bool`
  Funde duas contas: o saldo e o histórico de `account_id_2` são transferidos para `account_id_1`, e `account_id_2` é removida. Falha se alguma conta não existir, ou se `account_id_1 == account_id_2`.

- `get_balance_timeline(account_id: str) -> list[tuple[int, int]]`
  Retorna uma lista de tuplas `(timestamp, saldo)` mostrando como o saldo da conta mudou ao longo do tempo (ordenado por timestamp).

**Real: não se cobre por não terminar esse nível.** No teste de verdade, a maioria dos candidatos nem chega aqui completo — e tudo bem! O que os avaliadores querem ver é: seu código dos níveis anteriores está limpo, funciona, e você mostrou raciocínio. Um Nível 4 incompleto, mas com uma tentativa organizada, vale muito mais do que gastar todo seu tempo tentando decorar algo.

---
---

# 📝 GABARITO COMENTADO

### Antes de ver a solução: você tentou? De verdade? 😄
Se sim, bora comparar. Se não... volta lá em cima e tenta pelo menos o Nível 1 e 2, viu? Eu prometo que vale a pena.

---

## ✅ Nível 1 — Solução

```python
class Wallet:
    def __init__(self):
        # Guardamos cada conta como uma entrada no dicionário
        # A chave é o account_id, o valor é o saldo
        self.accounts = {}

    def create_account(self, account_id: str, timestamp: int) -> bool:
        if account_id in self.accounts:
            return False  # já existe, não faz nada
        self.accounts[account_id] = 0
        return True

    def deposit(self, account_id: str, timestamp: int, amount: int):
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        return self.accounts[account_id]

    def withdraw(self, account_id: str, timestamp: int, amount: int):
        if account_id not in self.accounts:
            return None
        if self.accounts[account_id] < amount:
            return None  # saldo insuficiente
        self.accounts[account_id] -= amount
        return self.accounts[account_id]
```

**Por que um dicionário (`dict`)?** Porque buscar uma conta por ID em um dicionário é **O(1)** — praticamente instantâneo, não importa se você tem 10 ou 10 milhões de contas. Se você tivesse usado uma lista de contas e precisasse percorrer tudo pra achar uma conta, isso seria O(n) — mais lento. Estrutura de dados certa desde o início = metade do problema resolvido.

**Erro comum:** esquecer de checar se a conta existe ANTES de mexer no saldo. Isso quebra vários testes de corner case.

---

## ✅ Nível 2 — Solução

```python
class Wallet:
    def __init__(self):
        self.accounts = {}
        self.total_spent = {}  # NOVO: total gasto por conta

    def create_account(self, account_id, timestamp):
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        self.total_spent[account_id] = 0
        return True

    def deposit(self, account_id, timestamp, amount):
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        return self.accounts[account_id]

    def withdraw(self, account_id, timestamp, amount):
        if account_id not in self.accounts:
            return None
        if self.accounts[account_id] < amount:
            return None
        self.accounts[account_id] -= amount
        self.total_spent[account_id] += amount  # conta como gasto
        return self.accounts[account_id]

    def transfer(self, from_id, to_id, timestamp, amount) -> bool:
        if from_id not in self.accounts or to_id not in self.accounts:
            return False
        if self.accounts[from_id] < amount:
            return False
        self.accounts[from_id] -= amount
        self.accounts[to_id] += amount
        self.total_spent[from_id] += amount  # quem envia "gastou"
        return True

    def top_spenders(self, timestamp, n):
        # sorted() com chave composta: primeiro por gasto (desc),
        # depois por account_id (asc) em caso de empate
        ordenado = sorted(
            self.total_spent.items(),
            key=lambda item: (-item[1], item[0])
        )
        return [account_id for account_id, gasto in ordenado[:n]]
```

**Explicando a mágica do `sorted()`:** a chave `key=lambda item: (-item[1], item[0])` é o pulo do gato. Isso diz: "ordena primeiro pelo gasto, mas do MAIOR pro menor (por isso o `-` no gasto), e se empatar, ordena pelo `account_id` do menor pro maior (ordem alfabética normal)". Isso é MUITO comum em problemas de ranking — guarde esse padrão!

**Sacada de arquitetura:** eu já criei o `total_spent` desde o Nível 2 pensando lá na frente. É por isso que eu falei pra você pensar bem na estrutura desde o Nível 1 — o candidato que só pensa "no que o nível pede agora" acaba tendo que refatorar tudo depois, perdendo tempo precioso.

---

## ✅ Nível 3 — Solução

```python
class Wallet:
    def __init__(self):
        self.accounts = {}
        self.total_spent = {}
        self.payments = {}  # payment_id -> dados do pagamento
        self.payment_counter = 0

    # ... (métodos anteriores continuam iguais) ...

    def pay_with_cashback(self, account_id, timestamp, amount, cashback_percentage):
        if account_id not in self.accounts or self.accounts[account_id] < amount:
            return None

        self.accounts[account_id] -= amount
        self.total_spent[account_id] += amount

        self.payment_counter += 1
        payment_id = f"payment{self.payment_counter}"

        cashback_amount = round(amount * cashback_percentage / 100)
        cashback_time = timestamp + 1440  # 24h em minutos

        self.payments[payment_id] = {
            "account_id": account_id,
            "cashback_time": cashback_time,
            "cashback_amount": cashback_amount,
            "cashback_paid": False,
        }
        return payment_id

    def get_payment_status(self, account_id, timestamp, payment_id):
        if payment_id not in self.payments:
            return None
        pagamento = self.payments[payment_id]

        if timestamp >= pagamento["cashback_time"] and not pagamento["cashback_paid"]:
            self.accounts[pagamento["account_id"]] += pagamento["cashback_amount"]
            pagamento["cashback_paid"] = True

        return "CASHBACK_RECEIVED" if pagamento["cashback_paid"] else "IN_PROGRESS"
```

**Por que guardar o pagamento num dicionário com vários campos?** Porque no ICA, quase sempre você vai precisar consultar o "estado" de alguma coisa mais tarde (status de um pagamento, histórico de uma conta...). Um dicionário representando um "objeto" com vários atributos é seu melhor amigo aqui. Se quiser deixar ainda mais elegante, dá pra usar um `dataclass` — mas num teste cronometrado, dicionário simples resolve rápido.

**Pegadinha que eu destaquei no enunciado:** "cashback é creditado 24h depois" — muita gente esquece de fazer a conversão de horas pra minutos (1440), ou credita o cashback na hora errada. Sempre teste esse tipo de cálculo com um exemplo numérico na mão antes de codar.

---

## ✅ Nível 4 — Solução

```python
class Wallet:
    def __init__(self):
        self.accounts = {}
        self.total_spent = {}
        self.payments = {}
        self.payment_counter = 0
        self.balance_history = {}  # NOVO: account_id -> lista de (timestamp, saldo)

    def create_account(self, account_id, timestamp):
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        self.total_spent[account_id] = 0
        self.balance_history[account_id] = [(timestamp, 0)]
        return True

    def _registrar_historico(self, account_id, timestamp):
        self.balance_history[account_id].append(
            (timestamp, self.accounts[account_id])
        )

    def merge_accounts(self, account_id_1, account_id_2, timestamp) -> bool:
        if account_id_1 == account_id_2:
            return False
        if account_id_1 not in self.accounts or account_id_2 not in self.accounts:
            return False

        self.accounts[account_id_1] += self.accounts[account_id_2]
        self.total_spent[account_id_1] += self.total_spent[account_id_2]
        self.balance_history[account_id_1].extend(self.balance_history[account_id_2])
        self.balance_history[account_id_1].sort(key=lambda x: x[0])

        del self.accounts[account_id_2]
        del self.total_spent[account_id_2]
        del self.balance_history[account_id_2]
        return True

    def get_balance_timeline(self, account_id):
        if account_id not in self.balance_history:
            return []
        return sorted(self.balance_history[account_id], key=lambda x: x[0])
```

**O segredo do Nível 4:** repara que eu criei um método "privado" `_registrar_historico` (o `_` na frente é uma convenção do Python pra dizer "esse método é de uso interno da classe"). Você precisaria chamar esse método dentro de `deposit`, `withdraw` e `transfer` também, pra manter o histórico sempre atualizado — eu deixei isso como "dever de casa" pra você mesmo(a) ir lá e integrar! Essa é a beleza (e o desafio) do ICA: cada nível te faz **voltar e mexer** no código anterior. Por isso, desde o Nível 1, escreva um código fácil de estender, não um código "gambiarra" que só funciona pro que foi pedido naquele momento.

---

## 🎓 Resumo da Ópera — O que levar pra prova de verdade

1. **Pense em estrutura de dados ANTES de codar.** Dicionários (`dict`) são seus melhores amigos pra buscas rápidas por ID.
2. **Cada nível se apoia no anterior** — não escreva código "descartável", escreva código que você vai conseguir estender.
3. **Leia com calma as regras de negócio** (unidades de tempo, critérios de desempate, condições de erro). É ali que moram as pegadinhas.
4. **Teste seu código com exemplos na mão** antes de confiar que está certo — principalmente cálculos (como o cashback).
5. **Não trave.** Se o Nível 4 estiver difícil, garanta que 1, 2 e 3 estão sólidos e bem testados. Isso vale muito mais.
6. Lembra: **o teste é em inglês.** Pratique ler enunciados assim mesmo — e se quiser, escreva os nomes de variáveis e comentários em inglês também, pra já ir destravando esse "modo teste".

Bora, guerreiro(a)! Você já entendeu a lógica — agora é treino, treino e treino. Bons estudos e boa sorte no ICA! 🚀🐍
