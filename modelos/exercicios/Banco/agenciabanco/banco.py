class Banco:
    bancos = []
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco
        Banco.bancos.append(self)