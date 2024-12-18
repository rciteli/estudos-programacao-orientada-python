# Exercício para prática de programação orientada a objetos
# Autor: Rciteli

from avaliacao import Avaliacao
from cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    ## Função que grava os atributos do restaurante na lista, método init para iniciar uma instância da classe ##
    def __init__(self, nome, categoria):
        ## o atributo .title() mantém a primeira letra sempre como maiúscula, e o upper mantém todas as letras como maiúsculas ##
        ## ao usar a tecla 'F2' com uma variável selecionada, é possível mudar todas as varíaveis que referenciam ela. ##
        self._nome = nome.title()
        self._categoria = categoria.upper()
        ## O atributo com underscore _ é usado para constar que a informação é segura, e que não queremos alterar seu valor ##
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    ## retorna o nome e a categoria do restaurante em forma de String ##
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    ## exibe o nome, categoria e estado do restaurante, com argumento CLS que é a convenção, e o cls indica que é um método da classe (?) ##    
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')

    ## determina o estado do restaurante (ativo ou inativo), property  ##
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    ## metodo para os objetos
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print('A nota deve estar entre 1 e 5')

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliação'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    # Será verdadeiro se o item for uma instância da classe ItemCardapio
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descricao: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Volume(ml): {item._volume_ml}'
                print(mensagem_bebida)