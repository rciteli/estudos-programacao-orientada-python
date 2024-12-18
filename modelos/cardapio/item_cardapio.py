# Classe ItemCardapio para representar os itens do cardápio. Esta é a classe mãe e todas as outras classes dependem dela.
# abc serve para indicar que essa classe é uma classe abstrata, todas as classes derivadas dela devem implementar os metodos abstratos
# esse tipo de método é chamado de poliformismo, que é uma característica da programação orientada a objetos para permitir que classes derivadas de uma mesma classe
# tenham comportamentos diferentes, sem precisar modificar o comportamento da classe base.
# Apesar de serem obrigados a serem adicionados nas classes filhas, eles podem ser usados em classes filhas, sem precisar serem implementados (utilizando um pass, por exemplo).
# Em resumo, utilizamos: 
# Métodos para adicionar itens;
# Refatoração
# Exibição do cardápio
# Métodos abstratos
# Poliformismo

from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    # Construtor da classe
    def __init__(self, nome, preco):
        # Atributos da classe, _ serve para indicar que o atributo é privado (o que significa que ele pode ser acessado apenas dentro da classe)
        self._nome = nome
        self._preco = preco

    # Metodos abstratos servem para indicar que eles devem ser obrigados a serem implementados nas classes filhas
    @abstractmethod
    def aplicar_desconto(self, desconto):
        pass