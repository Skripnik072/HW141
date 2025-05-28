import pytest
from src.products import Product
from src.category import Category

@pytest.fixture()
def category1():
    return Category("Fruit", "Japan",
                    [Product("Apple", "Red", 215.00, 10),
                     Product("Orang", "Yellou", 240.00, 9),])

@pytest.fixture()
def category2():
    return Category("Fruit", "Austr",
                    [Product("Greyp", "Blue", 250.00, 8),
                     Product("Pin", "Big", 220.00, 7),])

@pytest.fixture()
def product1():
    return Product("Apple", "Red", 215.00, 10)

@pytest.fixture()
def product2():
    return Product("Apple", "Red", 0, 10)
