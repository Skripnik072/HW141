class Product:
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
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        '''Метод возвращает цену товара, корректирует цену и количество'''
#        from src.category import Category
#        for prod in products:
#            if name in prod["name"]:
#                prod["quantity"] += quantity
#                if price <= prod["price"]:
#                    price = prod["price"]
        return(cls, name, description, price, quantity)

    @property
    def gprice(self):
        '''Метод возвращает цену товара'''
        return f"{self.__price}"

    @gprice.setter
    def gprice(self, price):
        '''Метод для анализа и коррректровки цены товара'''
        if price <= 0:
            print ("Цена не должна быть нулевая или отрицательная")
            return
        else:
            self.__price = price
        return

# product1 = Product("Plum", "Red", 215.00, 10)

# print(product1.name)
# print(product1.description)
# print(product1.gprice)
# print(product1.quantity)

# product2= Product("Plum", "Black",255.00, 7)

# print(product2.name)
# print(product2.description)
# print(product2.gprice)
# print(product2.quantity)
