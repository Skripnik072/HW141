from src.products import Product

def test_products_init(product1):
    assert product1.name == "Apple"
    assert product1.description == "Red"
    assert product1.gprice == "215.0"
    assert product1.quantity == 10


def test_product_create():
    product1 = Product("Plum", "Red", 215.00, 10)
    product1.name = "Plum"
    product1.description = "Red"
    product1.gprice = 215.00
    product1.quantity = 10

def test_product_upgrade(product1):
    product1.gprice = -1
    assert product1.gprice == "215.0"

def test_product_str(product1):
    assert str(product1) == "Apple, 215.0 руб. Остаток: 10 шт."

def test_product_add(product1, product2):
    assert product1 + product2 == 2150
