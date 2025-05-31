import pytest
from src.products import Product
from src.category import Category
from src.prod_smart import Smartphone
from src.prod_grass import LawnGrass


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

@pytest.fixture()
def smartf1():
    return Smartphone("Samsung", "Classs", 21500.00, 10, 1000, "S-5", 8, 'Blue')

@pytest.fixture()
def smartf2():
    return Smartphone("Samsung", "Classs", 22000.00, 20, 1000, "S-5", 8, 'Blue')

@pytest.fixture()
def grass1():
    return LawnGrass("Sama", "Hich", 215.00, 12, "JUSE", 30, "green")

@pytest.fixture()
def grass2():
    return LawnGrass("Gama", "Hich", 235.00, 2, "JUSE", 30, "orange")

