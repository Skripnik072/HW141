# from products import Product


class Category:
    '''Класс с информацией о категориях продуктов'''
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        '''Метод, который инициализирует атрибуты класса Category:'''
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

# if __name__ == "__main__":
#    product1 = Product("Apple", "Red", 215.00, 10)
#    product2 = Product("Orang", "Yellou", 240.00, 9)
#    product3 = Product("Greyp", "Blue", 250.00, 8)
#    product4 = Product("Pin", "Big", 220.00, 7)

#    cat1 = Category("Fruit", "Japan", [product1, product2, product3, product4])

#    print(cat1.name)
#    print(cat1.description)
#    print(cat1.products)

#    print(cat1.category_count)
#    print(cat1.product_count)