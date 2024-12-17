# Exercício para prática de programação orientada a objetos
# Autor: Rciteli

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
        Restaurante.restaurantes.append(self)
    
    ## retorna o nome e a categoria do restaurante em forma de String ##
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    ## exibe o nome, categoria e estado do restaurante, com argumento CLS que é a convenção, e o cls indica que é um método da classe (?) ##    
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')

    ## determina o estado do restaurante (ativo ou inativo), property  ##
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    ## metodo para os objetos
    def alternar_estado(self):
        self._ativo = not self._ativo