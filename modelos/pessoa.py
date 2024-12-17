# Exercício para prática de programação orientada a objetos
# Autor: Rciteli

class Pessoa:
    pessoas = []
    
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = int(idade)
        self._profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._profissao}'
    
    def aniversario(self):
        self._idade += 1

    @classmethod
    def listar_pessoas(cls):
        print(f'{"Nome":<25} | {"Idade":<25} | {"Profissão"}')
        for pessoa in cls.pessoas:
            print(f'{pessoa._nome:<25} | {str(pessoa._idade):<25} | {pessoa._profissao}')
    
    def saudacao(self):
        return f'Olá, {self._nome}! Sua idade é {self._idade} e sua profissão é {self._profissao}!'

pessoa_antonio = Pessoa('Antonio', '23', 'Padeiro')
pessoa_caio = Pessoa('Caio', '25', 'Dentista')
pessoa_marcela = Pessoa('Marcela', '31', 'Vendedora')

Pessoa.listar_pessoas()

print(pessoa_antonio.saudacao())

pessoa_antonio.aniversario()

print(pessoa_antonio.saudacao())

print(pessoa_caio.saudacao())

pessoa_caio.aniversario()

print(pessoa_caio.saudacao())

print(pessoa_marcela.saudacao())

pessoa_marcela.aniversario()

print(pessoa_marcela.saudacao())