def test_products_init(product1):
    assert product1.name == "Apple"
    assert product1.description == "Red"
    assert product1.price == 215
    assert product1.quantity == 10