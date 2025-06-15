from src.products import Product
from src.prod_smart import Smartphone
from src.prod_grass import LawnGrass


def test_print_mixin(capsys):
    Product("Apple", "Red", 215.00, 10)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Apple, Red, 215.0, 10)"

    Smartphone("Samsung", "Classs", 21500.00, 10, 1000, "S-5", 8, 'Blue')
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung, Classs, 21500.0, 10)"

    LawnGrass("Gama", "Hich", 235.00, 2, "JUSE", 30, "orange")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Gama, Hich, 235.0, 2)"
