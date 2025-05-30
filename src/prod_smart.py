from products import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: int, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self. memory = memory
        self.color = color

    def __add__(self, other: str) -> int:
        if type(other) is Smartphone:
            return self.quantity + other.quantity
        else:
            raise TypeError

if __name__ == "__main__":
    smartf = Smartphone("Samsung", "Classs", 21500.00, 10, 1000, "S-5", 8, 'Blue')

    print(smartf.name)
    print(smartf.description)
    print(smartf.gprice)
    print(smartf.quantity)

    print(smartf.efficiency)
    print(smartf.model)
    print(smartf.memory)
    print(smartf.color)

    smartf2 = Smartphone("Samsung", "Classs", 22000.00, 20, 1000, "S-5", 8, 'Blue')

    print(smartf + smartf2)
