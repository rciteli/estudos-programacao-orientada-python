
from cardapio.bebida import Bebida
from cardapio.prato import Prato


bebida_suco = Bebida('Suco de Melancia', 5, 500)
prato_pao = Prato('Pão de Frango com Catupiry', 10, 'O melhor lanche da cidade!')

# Define a função main
def main():
    print(bebida_suco)
    print(prato_pao)

# Chama a função main
if __name__ == '__main__':
    main()