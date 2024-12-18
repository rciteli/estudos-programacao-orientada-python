from livro import Livro

def exibir_livros():
    print(f'{"Livros".ljust(20)} | {"Autor".ljust(30)} | {"Ano de Publicação".ljust(25)} | {"Disponibilidade"}')
    for livro in Livro.lista_livros:
        print(f'{livro._titulo.ljust(20)} | {livro._autor.ljust(30)} | {str(livro._ano_publicacao).ljust(25)} | {livro._disponivel}')

def verificar_disponibilidade():
    for livro in Livro.lista_livros:
        if livro._ano_publicacao == 1937:
            print(f'{livro._titulo} | {livro._autor} | {livro._ano_publicacao} | {livro._disponivel}')

# Define a função main
def main():
    Livro.verificar_disponibilidade(cls=Livro)

# Chama a função main
if __name__ == '__main__':
    main()