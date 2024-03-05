"""
Задания:
    1. Cоздайте экземпляр класса студенда.
    2. Получите его полное имя используя метод get_full_name.
    3. Положите результат вызова метода get_full_name в переменную и распечатайте ее.
"""


class Student:
    def __init__(self, name: str, surname: str, faculty: str, course: int):
        self.name = name
        self.surname = surname
        self.faculty = faculty
        self.course = course

    def get_full_name(self):
        return f"Student's full name: {self.surname}, {self.name}"

    def get_full_information(self):
        full_info = f"Полная информация о студенте: {self.name} {self.surname} {self.faculty} {self.course}"
        return full_info


if __name__ == '__main__':
    student = Student(name = "Ivan", surname = "Ivanov", faculty = "IT", course = 3)
    ask = student.get_full_name()
    ask_full = student.get_full_information()
    print(ask)
    print(ask_full)
