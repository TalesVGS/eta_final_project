import pytest
from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available_with_stock(self):  # Marcelo
        ice_cream_stand = IceCreamStand("Rango Bom", "Italian food", ["Baunilha", "Chocolate"])
        expected_result = ["No momento temos os seguintes sabores de sorvete disponíveis:",
                           ["Baunilha", "Chocolate"]]
        result = ice_cream_stand.flavors_available()
        assert result == expected_result

    def test_flavors_available_with_empty_stock(self):  # Marcelo
        ice_cream_stand = IceCreamStand("Rango Bom", "Italian food", [])
        expected_result = "Estamos sem estoque atualmente!"
        result = ice_cream_stand.flavors_available()
        assert result == expected_result

    def test_find_flavor(self):  # Tales
        assert False

    def test_add_flavor(self):  # Elton
        assert False
