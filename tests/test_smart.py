import pytest
from src.products import Product
from src.prod_smart import Smartphone


def test_smart_init(smartf1):
    assert smartf1.name == "Samsung"
    assert smartf1.description == "Classs"
    assert smartf1.efficiency == 1000
    assert smartf1.model == "S-5"
    assert smartf1.memory == 8
    assert smartf1.color == 'Blue'

def test_smart_add(smartf1, smartf2):
    assert smartf1 + smartf2 == 30


def test_smart_add_error(smartf1):
    with pytest.raises(TypeError):
        result = smartf1 + 10