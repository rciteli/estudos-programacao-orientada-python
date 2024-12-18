from agenciabanco.banco import Banco
from agenciabanco.agencia import Agencia

agencia1 = Agencia('Agencia 1', 'Rua Conde de Bonfim, 798', 1, 'Agência Tijuca')
agencia2 = Agencia('Agencia 2', 'Rua Mem de Sá, 32', 2, 'Agência Lapa')
agencia3 = Agencia('Agencia 3', 'Avenida Bartolomeu Mitre, 137', 3, 'Agência Leblon')
agencia4 = Agencia('Agencia 4', 'Praia de Botafogo, 58', 4, 'Agência Botafogo')

banco1 = Banco('Itaú', 'Rua 1')
banco2 = Banco('Bradesco', 'Rua 2')
banco3 = Banco('Santander', 'Rua 3')
banco4 = Banco('Caixa', 'Rua 4')



def main():
    Agencia.listar_agencias()

if __name__ == '__main__':
    main()

