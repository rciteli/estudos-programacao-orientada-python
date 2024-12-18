from agenciabanco.banco import Banco

class Agencia(Banco):
    agencias = []
    def __init__(self, nome, endereco, numero_agencia, nome_agencia):
        super().__init__(nome, endereco)
        self._numero_agencia = numero_agencia
        self._nome_agencia = nome_agencia
        Agencia.agencias.append(self)

    def __str__(self):
        return f'{self._nome} | {self._endereco} | {self._numero_agencia} | {self._nome_agencia}'
    
    @classmethod
    def listar_agencias(cls):
        print(f'{"Agência".ljust(20)} | {"Endereço".ljust(50)} | {"Número da agência".ljust(30)} | {"Nome da Agência"}')
        for agencia in cls.agencias:
            print(f'{agencia._nome.ljust(20)} | {agencia._endereco.ljust(50)} | {str(agencia._numero_agencia).ljust(30)} | {agencia._nome_agencia}')
    
    