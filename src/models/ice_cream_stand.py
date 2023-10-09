from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):  # Marcelo
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            # Melhoria: Removendo prints (e formatação) de dentro da função e acrescentando returns
            # print("No momento temos os seguintes sabores de sorvete disponíveis:")
            flavors = []
            for flavor in self.flavors:
                # Melhoria: Removendo prints (e formatação) de dentro da função e acrescentando returns
                # print(f"\t-{flavor}")
                flavors.append(f"{flavor}")
            return ["No momento temos os seguintes sabores de sorvete disponíveis:", flavors]
        else:
            # Melhoria: Removendo prints de dentro das funções e acrescentando returns
            # print("Estamos sem estoque atualmente!")
            return "Estamos sem estoque atualmente!"

        # Refatorar

    def find_flavor(self, flavor):  # TALES
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                # Alterado para return
                # Alterado {self.flavors}
                return f"Temos {flavor} no momento!"
            else:
                # Alterado para return
                # Alterado {self.flavors}
                return f"Não temos {flavor} no momento!"
            # Alterado para return
        return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor): #ELTON
        """Add o sabor informado ao estoque."""
        if self.flavors:
            if flavor in self.flavors:
                print("\nSabor já disponivel!")
            else:
                self.flavors.append(flavor)
                print(f"{flavor} adicionado ao estoque!")
        else:
            print("Estamos sem estoque atualmente!")
