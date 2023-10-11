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

    def test_find_flavor_available(self):  # Tales
        icecreamstand = IceCreamStand("Tales", "bar", ["Teste", "Caipirinha", "suco"])
        expected_result = 'Temos Caipirinha no momento!'  # melhorar
        result = icecreamstand.find_flavor("Caipirinha")
        assert result == expected_result

    def test_find_flavor_unavailable(self):  # Tales
        icecreamstand = IceCreamStand("Tales", "bar", ["Teste", "drink", "petiscos"])
        expected_result = 'Não temos Cerveja no momento!'  # melhorar
        result = icecreamstand.find_flavor("Cerveja")
        assert result == expected_result

    def test_find_flavor_out_of_stock(self): # Tales
        icecreamstand = IceCreamStand("Tales", "bar", [])
        expected_result = 'Estamos sem estoque atualmente!'
        result = icecreamstand.find_flavor("Cerveja")
        assert result == expected_result

    def test_add_flavor_with_stock(self):  # Elton
        icecreamstand = IceCreamStand("Superburguer", "Snack Bar", ["Morango"])
        expected_result = "Sabor já disponivel!"
        result = icecreamstand.add_flavor("Morango")
        assert result == expected_result

    def test_add_flavor_out_of_stock(self):  # Elton
        icecreamstand = IceCreamStand("Superburguer", "Snack Bar", [])
        expected_result = 'Morango adicionado ao estoque!'
        result = icecreamstand.add_flavor("Morango")
        assert result == expected_result