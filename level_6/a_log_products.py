"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс iPrintLoggerMixn и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class iPrintLoggerMixin:
    def log(self, message):
        print(message)


class Product():
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(Product, iPrintLoggerMixin):
    def increase_price(self):
        self.log('Increased price * 1.2')
        self.price *= 1.2

    def get_info(self):
        base_info = super().get_info()
        self.log(f'{super().get_info()} (Premium)')
        return f'{base_info} (Premium)'


class DiscountedProduct(Product, iPrintLoggerMixin):
    def decrease_price(self):
        self.log('Decreased price / 1.2')
        self.price /= 1.2

    def get_info(self):
        self.log(f'{super().get_info()} (Discounted)')
        base_info = super().get_info()

        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    p1 = PremiumProduct('iPhone', 1000)
    p1.log("Creating premium product")
    p1.get_info()
    p1.increase_price()

    p2 = DiscountedProduct('MacBook', 2000)
    p2.log("Creating discounted product")
    p2.get_info()
    p2.decrease_price()
