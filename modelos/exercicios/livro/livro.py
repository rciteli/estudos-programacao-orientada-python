class Livro():
    lista_livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.lista_livros.append(self)
    
    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self._disponivel}'
    
    def exibir_livros(cls):
        print(f'{'Livros'.ljust(20)} | {'Autor'.ljust(30)} | {'Ano de Publicação'.ljust(25)} | {'Disponibilidade'}')
        for livro in cls.lista_livros:
            print(f'{livro._titulo.ljust(20)} | {livro._autor.ljust(30)} | {str(livro._ano_publicacao).ljust(25)} | {livro._disponivel}')
    
    def emprestar_livro(cls, livro):
        livro._disponivel = False

    def verificar_disponibilidade(cls):
        for livro in cls.lista_livros:
            if livro._ano_publicacao == 1937:
                print(f'{livro._titulo} | {livro._autor} | {livro._ano_publicacao} | {livro._disponivel}')

        
    
livro1 = Livro('O Senhor dos Aneis', 'JRR Tolkien', 1954)
livro2 = Livro('O Hobbit', 'JRR Tolkien', 1937)

