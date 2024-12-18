from restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato

# Em resumo, utilizamos: 
# Métodos para adicionar itens;
# Refatoração
# Exibição do cardápio
# Métodos abstratos
# Poliformismo

# instancia um restaurante, pratos, bebidas e adiciona os items ao cardapio.
restaurante_praca = Restaurante('Restaurante da Praca', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 500)
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pão de Frango com Catupiry', 10, 'O melhor lanche da cidade!')
prato_pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)


# Define a função main
def main():
    restaurante_praca.exibir_cardapio

# Chama a função main
if __name__ == '__main__':
    main()