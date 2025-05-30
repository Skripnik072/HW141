import pytest


def test_catecory_init(category1, category2):
    assert category1.name == "Fruit"
    assert category1.description == "Japan"
    assert len(category1.product_in_list) == 2
    assert category1.category_count == 2
    assert category2.product_count == 4
    assert category1.category_count == 2
    assert category1.product_count == 4


def test_category_property(category1):
    assert category1.products == "Apple, 215.0 руб. Остаток: 10 шт.\nOrang, 240.0 руб. Остаток: 9 шт.\n"


def test_category_setter(category1, product1):
    assert len(category1.product_in_list) == 2
    category1.products = product1
    assert len(category1.product_in_list) == 3


def test_category_str(category1):
    assert str(category1) == "Fruit, количество продуктов: 19 шт."


def test_category_setter_error(category1, product1):
    with pytest.raises(TypeError):
        category1.products = 1


def test_category_setter_smart(category1, smartf1):
    category1.products = smartf1
    assert category1.product_in_list[-1].name == "Samsung"
