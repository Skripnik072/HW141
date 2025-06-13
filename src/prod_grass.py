from src.products import Product


class LawnGrass(Product):
    '''Создан класс-наследник с функциональностью сложения одинаковых продуктов'''
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: int,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: str) -> int:
        if type(other) is LawnGrass:
            return self.quantity + other.quantity
        else:
            raise TypeError


# if __name__ == "__main__":
#    grass = LawnGrass("Sama", "Hich", 215.00, 12, "JUSE", 30, "green")
#    grass1 = LawnGrass("Gama", "Hich", 235.00, 2, "JUSE", 30, "orange")
#    smartf = Smartphone("Samsung", "Classs", 21500.00, 10, 1000, "S-5", 8, 'Blue')
#    product1 = Product("Plum", "Red", 215.00, 10)

#    print(grass.name)
#    print(grass.description)
#    print(grass.gprice)
#    print(grass.quantity)

#    print(grass.name)
#    print(grass.country)
#    print(grass.germination_period)
#    print(grass.color)

#    print(grass + grass1)
