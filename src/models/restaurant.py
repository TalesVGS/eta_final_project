class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):  # Marcelo
        """Imprima uma descrição simples da instância do restaurante."""

        # print(f"Esse restaturante chama {self.cuisine_type} and serve {self.cuisine_type}.")
        # print(f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.")

        # Melhoria: Removendo prints de dentro da função e acrescentando returns
        return [f"Esse restaturante chama {self.cuisine_type} and serve {self.cuisine_type}.",
                f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto."]

    def open_restaurant(self):  # Marcelo
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = False
            self.number_served = -2

            # Melhoria: Removendo prints de dentro da função e acrescentando returns
            # print(f"{self.restaurant_name} agora está aberto!")
            return f"{self.restaurant_name} agora está aberto!"
        else:
            # Melhoria: Removendo prints de dentro da função e acrescentando returns
            # print(f"{self.restaurant_name} já está aberto!")
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):  # Marcelo
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            # Melhoria: Removendo prints de dentro da função e acrescentando returns
            # print(f"{self.restaurant_name} agora está fechado!")
            return f"{self.restaurant_name} agora está fechado!"
        else:
            # Melhoria: Removendo prints de dentro da função e acrescentando returns
            # print(f"{self.restaurant_name} já está fechado!")
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers): #TALES
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers): #ELTON
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served = more_customers
        else:
            print(f"{self.restaurant_name} está fechado!")
