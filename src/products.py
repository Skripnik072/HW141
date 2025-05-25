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
        self.price = price
        self.quantity = quantity


product1 = Product("Apple", "Red", 215.00, "10")

#    print(product1.name)
#    print(product1.description)
#    print(product1.price)
#    print(product1.quantity)
