from category import Category
from products import Product


class ProdIterator:
    def __init__(self, categ_obj):
        self.categ_obj = categ_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.categ_obj.product_in_list):
            prod = self.categ_obj.product_in_list[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration

if __name__ == "__main__":
    product1 = Product("Apple", "Red", 215.00, 10)
    product2 = Product("Orang", "Yellou", 240.00, 9)
    product3 = Product("Greyp", "Blue", 250.00, 8)
    product4 = Product("Pin", "Big", 220.00, 7)

    cat1 = Category("Fruit", "Japan", [product1, product2, product3, product4])

    iterator = ProdIterator(cat1)

    for prod in iterator:
        print(prod)