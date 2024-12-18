# Classe ItemCardapio para representar os itens do cardápio. Esta é a classe mãe e todas as outras classes dependem dela.
class ItemCardapio:
    # Construtor da classe
    def __init__(self, nome, preco):
        # Atributos da classe, _ serve para indicar que o atributo é privado (o que significa que ele pode ser acessado apenas dentro da classe)
        self._nome = nome
        self._preco = preco