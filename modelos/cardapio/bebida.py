from cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, volume_ml):
        # Superclasse que herda os atributos da classe ItemCardapio
        super().__init__(nome, preco)
        self._volume_ml = volume_ml

    def __str__(self):
        return self._nome