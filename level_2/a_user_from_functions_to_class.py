"""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""


class User:
    def __init__(self, username: str = None, user_id: int = None,
            name: str = None) -> None:
        self.username = username
        self.user_id = user_id
        self.name = name

    def _make_username_capitalized(self, username: str) -> str:
        return username.capitalize()

    def _make_name_capitalized(self, name: str) -> str:
        return name.capitalize()

    def generate_short_user_description(self, username: str, user_id: int,
            name: str) -> str:
        return (f'User with id {user_id} has '
                f'{self._make_username_capitalized(username)} username and '
                f'{self._make_name_capitalized(name)} '
                f'name')


if __name__ == "__main__":
    ekz = User()

    print(ekz.generate_short_user_description("viirus", 1, "aleksey"))
