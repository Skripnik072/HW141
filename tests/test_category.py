
def test_catecory_init(category1, category2):
    assert category1.name == "Fruit"
    assert category1.description == "Japan"
    assert len(category1.products) == 2

    assert category1.category_count == 2
    assert category2.product_count == 4

    assert category1.category_count == 2
    assert category1.product_count == 4
