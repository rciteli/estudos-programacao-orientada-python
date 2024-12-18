from cardapio.item_cardapio import ItemCardapio

# Classe Prato que herda de ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        # Superclasse que herda os atributos da classe ItemCardapio
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome