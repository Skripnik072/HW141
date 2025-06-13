import pytest
from src.products import Product
from src.prod_grass import LawnGrass


def test_grass_init(grass1):
    assert grass1.name == "Sama"
    assert grass1.description == "Hich"
    assert grass1.country == "JUSE"
    assert grass1.germination_period == 30
    assert grass1.color == "green"

def test_grass_add(grass1, grass2):
    assert grass1 + grass2 == 14


def test_grass_add_error(grass1):
    with pytest.raises(TypeError):
        result = grass1 + 1