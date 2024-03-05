"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = ["vasya", "bob", "alice", "admin", "super_admin"]

    def add_user(self, username):
        self.usernames.append(username)
        return f"{username} БЫЛ ДОБАВЛЕН."

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self):
        username = input("Введите юзернэйм: ")
        if username in self.usernames:
            self.usernames.remove(username)
            return f"{username} БЫЛ ЗАБАНЕН."
        else:
            return f"Такого пользователя не существует."


class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        self.usernames.clear()
        return f"ВСЕ ПОЛЬЗОВАТЕЛИ БЫЛИ ЗАБАНЕНЫ."


if __name__ == '__main__':
    ekz = UserManager()
    ekz1 = AdminManager()
    ekz2 = SuperAdminManager()

    print(ekz.get_users())
    print(ekz.add_user("Бубалеххххх"))

    print(ekz1.get_users())
    print(ekz1.add_user("Бубалеххххх"))
    print(ekz1.ban_username())

    print(ekz2.get_users())
    print(ekz2.add_user("Бубалеххххх"))
    print(ekz2.ban_username())
    print(ekz2.ban_all_users())
