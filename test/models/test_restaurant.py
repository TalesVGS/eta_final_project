import pytest
from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):  # Marcelo
        restaurant = Restaurant("Rango Bom", "Italian food")
        expected_result = ["Esse restaturante chama Rango Bom and serve Italian food.",
                           "Esse restaturante está servindo 0 consumidores desde que está aberto."]
        result = restaurant.describe_restaurant()
        assert result == expected_result

    def test_open_closed_restaurant_message(self):  # Marcelo
        restaurant = Restaurant("Rango Bom", "Italian food")
        expected_result = "Rango Bom agora está aberto!"
        result = restaurant.open_restaurant()
        assert result == expected_result

    def test_open_closed_restaurant_state(self):  # Marcelo
        restaurant = Restaurant("Rango Bom", "Italian food")
        restaurant.open_restaurant()
        expected_result = True
        result = restaurant.open
        assert result == expected_result

    def test_open_closed_restaurant_stock_status(self):  # Marcelo
        restaurant = Restaurant("Rango Bom", "Italian food")
        restaurant.open_restaurant()
        expected_result = 0
        restaurant.open_restaurant()
        result = restaurant.number_served
        assert result == expected_result

    def test_open_opened_restaurant_message(self):  # Marcelo
        restaurant = Restaurant("Rango Bom", "Italian food")
        restaurant.open = True
        expected_result = "Rango Bom já está aberto!"
        result = restaurant.open_restaurant()
        assert result == expected_result

    def test_close_opened_restaurant(self):  # Marcelo
        restaurant = Restaurant("Rango Bom", "Italian food")
        restaurant.open = True
        expected_result = "Rango Bom agora está fechado!"
        result = restaurant.close_restaurant()
        assert result == expected_result

    def test_close_closed_restaurant(self):  # Marcelo
        restaurant = Restaurant("Rango Bom", "Italian food")
        restaurant.open = False
        expected_result = "Rango Bom já está fechado!"
        result = restaurant.close_restaurant()
        assert result == expected_result

    def test_set_number_served(self):  # Tales
        restaurant = Restaurant("Tales", "bar")
        restaurant.open = True
        expected_result = "Total de pessoas atendidas é: 5"
        result = restaurant.set_number_served(5)
        assert result == expected_result

    def test_set_number_served_restaurant_closed(self):  # Tales
        restaurant = Restaurant("Tales", "bar")
        restaurant.open = False
        expected_result = "Tales está fechado!"
        result = restaurant.set_number_served(5)
        assert result == expected_result

    def test_increment_number_served(self):  # Elton
        restaurant = Restaurant("Elton", "Japanese")
        restaurant.open = True
        restaurant.number_served = 10
        expected_result = 12
        restaurant.increment_number_served(2)
        result = restaurant.number_served
        assert result == expected_result

    def test_increment_number_served_restaurant_closed(self):  # Elton
        restaurant = Restaurant("Elton", "Japanese")
        restaurant.open = False
        restaurant.number_served = 10
        expected_result = "Elton está fechado!"
        result = restaurant.increment_number_served(2)
        assert result == expected_result