"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""

from os import name


class Product:
    def __init__(self, name: str = None, description: str = None, price: int = None, weight: float = None) -> None:
        self.name = name
        self.discription = description
        self.price = price
        self.weight = weight

    def _full_info(self):
        return f"Информация о продукте: {self.name}, {self.discription}, {self.price}, {self.weight}"

    def show(self):
        print(self._full_info())


if __name__ == "__main__":
    product = Product(name="Молоко", description="Молочное", price=100, weight=0.5)
    product.show()
    product1 = Product(name="Молоко", price=100, weight=0.5)
    product1.show()
