import pytest
from src.products import Product


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


def test_middle_product_price(category1, category_non_products):
    assert category1.middle_product_price() == 227.50
    assert category_non_products.middle_product_price() == 0


def test_local_exceptions(capsys, category1):
    assert len(category1.product_in_list) == 2

    product_add = Product("Plum", "Black", 255.00, 0)
    category1.products = product_add
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Нельзя ввести продукт с нулевым количеством"
    assert message.out.strip().split('\n')[-1] == "Задача добавления продукта завершена"

    product_add = Product("Plum", "Black", 255.00, 5)
    category1.products = product_add
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Продукт успешно добавлен"
    assert message.out.strip().split('\n')[-1] == "Задача добавления продукта завершена"
