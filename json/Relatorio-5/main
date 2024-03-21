from database import Database
from livrinhos import *

db = Database(database="Relatorio-5", collection="Livros")

liv=Livrinhos(db)

print("===== MENU CRUD Livros =====")
print("1. Criar um novo livro")
print("2. Ler todos os livros")
print("3. Ler um livro por ID")
print("4. Atualizar um livro")
print("5. Deletar um livro por ID")
print("6. Sair do programa")

while True:
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            ano = int(input("Digite o ano de publicação: "))
            preco = float(input("Digite o preço do livro: "))
            
            liv.criar_livro(titulo,autor,ano,preco)
            
        elif opcao == "2":
            
            liv.ler_todos_livros()
            
        elif opcao == "3":
            
            id = input("Digite o ID do livro: ")
            
            liv.ler_livro_por_id(id)
            
        elif opcao == "4":
            
            id = input("Digite o ID do livro que deseja atualizar: ")
            titulo = input("Digite o novo título do livro: ")
            autor = input("Digite o novo nome do autor: ")
            ano = int(input("Digite o novo ano de publicação: "))
            preco = float(input("Digite o novo preço do livro: "))
    
            liv.atualizar_livro(id, titulo, autor,ano,preco)
            
        elif opcao == "5":
            id = input("Digite o ID do livro que deseja deletar: ")
            
            liv.deletar_livro_por_id(id)
            
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")