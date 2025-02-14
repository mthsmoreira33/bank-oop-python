# Bank OOP Python

Este projeto é um sistema bancário simples implementado em Python usando princípios de Programação Orientada a Objetos (OOP). Ele permite que os usuários criem contas, façam depósitos e saques, e visualizem o histórico de contas.

## Classes

### Client
Representa um cliente do banco.
- `__init__(self, address)`: Inicializa um cliente com um endereço e uma lista vazia de contas.
- `make_transaction(self, account, transaction)`: Registra uma transação para uma conta específica.
- `add_account(self, account)`: Adiciona uma conta à lista de contas do cliente.

### NaturalPerson
Herdada de `Client` e representa uma pessoa física.
- `__init__(self, address, cpf, birthdate, name)`: Inicializa uma pessoa física com endereço, CPF, data de nascimento e nome.

### BankAccount
Representa uma conta bancária.
- `__init__(self, account_number, client)`: Inicializa uma conta bancária com número da conta, cliente, agência, saldo e histórico.
- `create_new_account(cls, client, number)`: Método de classe para criar uma nova conta bancária.
- Propriedades: `balance`, `history`, `account_number`, `branch`, `client`.
- `withdrawal(self, value)`: Realiza um saque de um valor especificado da conta.
- `__str__(self)`: Retorna uma representação em string da conta.

### CurrentAccount
Herdada de `BankAccount` e representa uma conta corrente.
- `__init__(self, account_number, client, limit=500, withdrawals_limit=3)`: Inicializa uma conta corrente com número da conta, cliente, limite e limite de saques.

### History
Representa o histórico de transações de uma conta.
- `__init__(self)`: Inicializa uma lista vazia de transações.
- `transactions`: Propriedade para obter a lista de transações.
- `add_transaction(self, transaction)`: Adiciona uma transação ao histórico.

### Transaction (Classe Base Abstrata)
Representa uma transação.
- `value`: Propriedade abstrata para o valor da transação.
- `register(self, account)`: Método abstrato para registrar a transação em uma conta.

### Withdrawal
Herdada de `Transaction` e representa uma transação de saque.
- `__init__(self, value)`: Inicializa um saque com um valor especificado.
- `register(self, account)`: Registra o saque em uma conta específica.

### Deposit
Herdada de `Transaction` e representa uma transação de depósito.
- `__init__(self, value)`: Inicializa um depósito com um valor especificado.
- `register(self, account)`: Registra o depósito em uma conta específica.

## Funções

### filter_client(cpf, clients)
Filtra clientes pelo CPF.
- `cpf`: O CPF para filtrar.
- `clients`: A lista de clientes.
- Retorna o cliente filtrado ou `None` se não encontrado.

### get_client_account(client, account_number)
Obtém a conta de um cliente pelo número da conta.
- `client`: O cliente para obter a conta.
- `account_number`: O número da conta para filtrar.
- Retorna a conta filtrada ou imprime uma mensagem se não encontrada.

### deposit(clients)
Lida com o processo de depósito.
- `clients`: A lista de clientes.

### withdrawal(clients)
Lida com o processo de saque.
- `clients`: A lista de clientes.

### list_accounts(accounts)
Lista todas as contas.
- `accounts`: A lista de contas.

### show_history(clients)
Mostra o histórico de transações da conta de um cliente.
- `clients`: A lista de clientes.

### create_account(number_account, clients, accounts)
Cria uma nova conta bancária.
- `number_account`: O número da conta.
- `clients`: A lista de clientes.
- `accounts`: A lista de contas.

### menu()
Exibe o menu e obtém a escolha do usuário.
- Retorna a escolha do usuário.

### main()
Função principal para executar o sistema bancário.

## Uso

Execute o arquivo `script.py` para iniciar o sistema bancário. Siga as opções do menu para criar contas, fazer depósitos e saques, e visualizar o histórico de contas.

```sh
python script.py
