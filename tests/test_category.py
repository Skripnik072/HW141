
def test_catecory_init(category1, category2):
    assert category1.name == "Fruit"
    assert category1.description == "Japan"
    assert len(category1.products) == 2

    assert category1.numbers_cat == 2
    assert category2.numbers_cat == 2

    assert category1.numbers_cat == 2
    assert category1.numbers_cat == 2
