"""Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и
уменьшать его.

Задания: 1. Возьмите итоговый класс из прошлого примера и добавьте ему метод,
который уменьшает баланс. Если итоговое значение будет отрицательным, то нужно будет
вызывать исключение ValueError. 2. Создайте экземпляр класса и уменьшите баланс до
положительного значения и распечатайте результат. 3. Затем уменьшите баланс до
отрицательного значения и посмотрите на результат"""

from d_bank_account_increase_balance import BankAccount


class BankAccount1:
    def __init__(self) -> None:
        self.acc = BankAccount(owner_full_name = "Aleksey", balance = 500)
        self.balance = self.acc.balance

    def decrease_balance(self, income: float) -> str:
        try:
            if income < 0:
                raise ValueError("Нельзя вводить отрицательные значения")
            self.acc.balance -= income

            if self.acc.balance < 0:
                raise ValueError("БАЛАНС НЕ МОЖЕТ БЫТЬ МЕНЬШЕ ОТРИЦАТЕЛЬНЫМ")
            return f"{self.acc.owner_full_name}, {self.acc.balance}"
        except ValueError as error:
            return error


if __name__ == "__main__":
    ekz = BankAccount1()

    print(ekz.decrease_balance(300))
