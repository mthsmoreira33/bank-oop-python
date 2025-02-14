from abc import ABC
import datetime
import textwrap

class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def make_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)

class NaturalPerson(Client):
    def __init__(self, address, cpf, birthdate, name):
        super().__init__(address)
        self._cpf = cpf
        self._birthdate = birthdate
        self._name = name

class BankAccount:
    def __init__(self, account_number, client):
        self._client = client
        self._account_number = account_number
        self._branch = "0001"
        self._balance = 0
        self._history = History()

    @classmethod
    def create_new_account(cls, client, number):
        return cls(number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def history(self):
        return self._history

    @property
    def account_number(self):
        return self._account_number

    @property
    def branch(self):
        return self._branch

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    def withdrawal(self, value):
        balance = self._balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("\n@@@ Saldo insuficiente! @@@")
            return False

        elif value > 0:
            self._balance -= value
            print("\n@@@ Saque realizado com sucesso! @@@")
            return True

        else:
            print("\n@@@ Valor inválido! @@@")

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self._branch}
            C/C:\t\t{self._account_number}
            Titular:\t{self.client._name}
        """

class CurrentAccount(BankAccount):
    def __init__(self, account_number, client, limit = 500, withdrawals_limit = 3):
        super().__init__(account_number, client)
        self._limit = limit
        self._withdrawals_limit = withdrawals_limit

class History:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "tipo": transaction.__class__.__name__,
                "valor": transaction.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transaction(ABC):
    @property
    def value(self):
        pass

    @classmethod
    def register(self, account):
        pass

class Withdrawal(Transaction):
    def __init__(self, value):
        self._value = value

    def register(self, account):
        account._history._history.append(f"withdrawal of {self._value}")

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value

    def register(self, account):
       success_transaction = account.deposit(self._value)

       if success_transaction:
           account._history.add_transaction(self)

def filter_client(cpf, clients):
    filtered_client = [client for client in clients if client._cpf == cpf]

    return filtered_client[0] if filtered_client else None

def get_client_account(client, account_number):
    if not client.accounts:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    filtered_bank_account = [bank_account for bank_account in client.accounts if bank_account._account_number == account_number]

    return filtered_bank_account[0] if filtered_bank_account else print("\n@@@ Cliente não possui conta com este número @@@")

def deposit(clients):
    cpf = input("CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    account_number = input("Número da conta: ")
    value = float(input("Valor: "))
    transaction = Deposit(value)

    bank_account = get_client_account(client, account_number)

    if not bank_account:
        return

    client.make_transaction(bank_account, transaction)

def withdrawal(clients):
    cpf = input("CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    account_number = input("Número da conta: ")
    value = float(input("Valor: "))
    transaction = Withdrawal(value)

    bank_account = get_client_account(client, account_number)

    if not bank_account:
        return

    client.make_transaction(bank_account, transaction)

def list_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(textwrap.dedent(str(account)))

def show_history(clients):
    cpf = input("CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    account_number = input("Número da conta: ")

    bank_account = get_client_account(client, account_number)

    if not bank_account:
        return

    transactions = bank_account.history.transactions

    history = ""

    if not transactions:
        history = "Não há transações para esta conta!"
    else:
        for transaction in transactions:
            history += f"Tipo: {transaction['tipo']}\nValor: {transaction['valor']}\nData: {transaction['data']}\n\n"

    print(history)
    print(f"\nSaldo atual: {bank_account.balance:.2f}")
    print("=" * 100)

def create_account(number_account, clients, accounts):
    cpf = input("CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    bank_account = BankAccount.create_new_account(client, number_account)
    accounts.append(bank_account)
    client.add_account(bank_account)

    print("\n@@@ Conta criada com sucesso! @@@\n")

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == "d":
            deposit(clients)
        elif option == "s":
            withdrawal(clients)
        elif option == "e":
            show_history(clients)
        elif option == "nc":
            number_account = len(accounts) + 1
            create_account(number_account, clients, accounts)
        elif option == "lc":
            list_accounts(accounts)
        elif option == "nu":
            name = input("Nome: ")
            cpf = input("CPF: ")
            address = input("Endereço: ")
            birthdate = input("Data de nascimento: ")

            client = NaturalPerson(address, cpf, birthdate, name)
            clients.append(client)
        elif option == "q":
            break
        else:
            print("\n@@@ Opção inválida! @@@\n")

main()
