from src.base_products import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    '''Класс для информации о продуктах'''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        '''Метод, который инициализирует атрибуты класса   '''
        self.name = name
        self.description = description
        self.__price = price
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: str) -> int:
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int) -> tuple:
        '''Метод возвращает цену товара, корректирует цену и количество'''
        return (cls, name, description, price, quantity)

    @property
    def gprice(self) -> str:
        '''Метод возвращает цену товара'''
        return f"{self.__price}"

    @gprice.setter
    def gprice(self, price: float) -> str:
        '''Метод для анализа и коррректровки цены товара'''
        if price <= 0:
            return "Цена не должна быть нулевая или отрицательная"
        else:
            self.__price = price
        return

product1 = Product("Plum", "Red", 215.00, 10)

# print(product1.name)
# print(product1.description)
# print(product1.gprice)
# print(product1.quantity)

product2 = Product("Plum", "Black", 255.00, 7)

# print(product2.name)
# print(product2.description)
# print(product2.gprice)
# print(product2.quantity)

# print(str(product1))
# print(product1 + product2)

product3 = Product("Plum", "Black", 255.00, 10)
