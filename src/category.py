from src.products import Product


class Category:
    '''Класс с информацией о категориях продуктов'''
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        '''Метод, который инициализирует атрибуты класса:'''
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        all_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {all_quantity} шт."

    def add_product(self, product: Product) -> str:
        self.__products.append(product)
        return f"{self.__products}"

    @property
    def products(self) -> str:
        prod_str = ""
        for prod in self.__products:
            prod_str += f"{str(prod)}\n"
        return prod_str

    @products.setter
    def products(self, product: Product) -> int:
        if isinstance(product, Product):
            self.add_product(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def product_in_list(self) -> list:
        return self.__products


if __name__ == "__main__":
    product1 = Product("Apple", "Red", 215.00, 10)
    product2 = Product("Orang", "Yellou", 240.00, 9)
    product3 = Product("Greyp", "Blue", 250.00, 8)
    product4 = Product("Pin", "Big", 220.00, 7)

    cat1 = Category("Fruit", "Japan", [product1, product2, product3, product4])

    print(cat1.name)
    print(cat1.description)
    print(cat1.products)
    print(cat1.category_count)
    print(cat1.product_count)

    product5 = Product("Plum", "Black", 270.00, 7)
    cat1.products = product5
    print(cat1.products)
    print(cat1.product_count)
