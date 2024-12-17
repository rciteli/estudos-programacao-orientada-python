# Exercício para prática de programação orientada a objetos
# Projeto Conta Bancária
# Cada conta bancária tem uma lista de clientes, e cada cliente tem uma lista de contas bancarias
# Autor: Rciteli

class ContaBancaria():
    lista_contas = []

    @classmethod
    def get_lista_contas(cls):
        return cls.lista_contas

    def __init__(self, conta_bancaria, saldo):
        self._conta_bancaria = conta_bancaria
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.lista_contas.append(self)
    
    def __str__(self):
        return f'{self._conta_bancaria} | {self._saldo} | {self._ativo}'
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def ativar_conta(self):
        self._ativo = not self._ativo

    @classmethod
    def listar_contas(cls):
        print(f'{'Conta Bancária'.ljust(15)} | {'Saldo'.ljust(10)} | {'Status'}')
        for conta in cls.lista_contas:
            print(f'{conta._conta_bancaria:<15} | {conta._saldo:<10} | {conta._ativo}')   

class ClienteBanco():
    informacoes_contas = []
    def __init__(self, nome, idade, conta_bancaria, endereco, telefone, email):
        self._nome = nome
        self._idade = idade
        self._conta_bancaria = conta_bancaria
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        ClienteBanco.informacoes_contas.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._conta_bancaria} | {self._endereco} | {self._telefone} | {self._email}'
    
    @classmethod
    def listar_clientes(cls):
        print(f'{'Nome'.ljust(15)} | {'Idade'.ljust(15)} | {'Conta Bancária'.ljust(15)} | {'Endereço'.ljust(15)} | {'Telefone'.ljust(15)} | {'E-mail'.ljust(15)}')
        for cliente in cls.informacoes_contas: 
            print(f'{cliente._nome:<15} | {str(cliente._idade):<15} | {cliente._conta_bancaria:<15} | {cliente._endereco:<15} | {cliente._telefone:<15} | {cliente._email:<15}')

cliente1 = ClienteBanco('João', 25, '1234-5', 'Rua 1', '1234-5678', 'jao@jao')
cliente2 = ClienteBanco('Maria', 30, '1234-6', 'Rua 2', '1234-5678', 'maria@maria')
cliente3 = ClienteBanco('Pedro', 35, '1234-7', 'Rua 3', '1234-5678', 'pedro@pedro')

conta1 = ContaBancaria(cliente1._conta_bancaria, 1000)
conta2 = ContaBancaria(cliente2._conta_bancaria, 2000)
conta3 = ContaBancaria(cliente3._conta_bancaria, 3000)

ContaBancaria.listar_contas()

ClienteBanco.listar_clientes()

