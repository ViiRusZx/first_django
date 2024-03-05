"""Задания: 1. Создайте экземпляр класса юзера, наполнив любыми данными. 2.
Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм,
возраст, телефон."""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone

    def _show(self) -> str:
        return (f"Информация о пользователе: {self.name}, {self.username}, {self.age}, "
                f"{self.phone}")

    def lets_print(self) -> None:
        print(self._show())


if __name__ == "__main__":
    # код писать тут

    ekz = User(name = "Aleksey", username = "Viirus", age = 37, phone = "112")

    ekz.lets_print()
