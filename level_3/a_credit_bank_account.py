"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float) -> str:
        try:
            if income < 0:
                raise ValueError("Нельзя вводить отрицательные значения")
            self.balance += income
            return f"{self.owner_full_name}, {self.balance}"
        except ValueError as err:
            return err

    def decrease_balance(self, income: float) -> str:
        try:
            if income < 0:
                raise ValueError("Нельзя вводить отрицательные значения")
            self.balance -= income

            if self.balance < 0:
                raise ValueError("БАЛАНС НЕ МОЖЕТ БЫТЬ МЕНЬШЕ ОТРИЦАТЕЛЬНЫМ")
            return f"{self.owner_full_name}, {self.balance}"
        except ValueError as error:
            return error


class CreditAccount(BankAccount):

    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    bank_acc = BankAccount("Alice Smith", 1500.0)
    print(bank_acc.increase_balance(1000.0))
    print(bank_acc.decrease_balance(500.0))

    credit = CreditAccount("Bob Smith", 700.0)
    print(credit.is_eligible_for_credit())
    print(credit.increase_balance(1000.0))
    print(credit.decrease_balance(500.0))
