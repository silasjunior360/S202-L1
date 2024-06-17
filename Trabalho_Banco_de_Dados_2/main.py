from database import Database
from produtos import ProdutosDatabase
from cliente import ClientesDatabase
from funcionarios import FuncionariosDatabase
from mecado import MercadosDatabase

db = Database("neo4j+s://1618bdb4.databases.neo4j.io", "neo4j", "MDusU809ta-0TUbjH-_2SdR6225l8v1FRO1Rk1XKMz8")
#db.drop_all()

prod = ProdutosDatabase(db)
clientes = ClientesDatabase(db)
funcionarios = FuncionariosDatabase(db)
mercados = MercadosDatabase(db)

def menu_mercados():
    while True:
        print("===== MENU CRUD Mercados =====")
        print("1. Criar um novo mercado")
        print("2. Voltar ao menu principal")
    
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do mercado: ")
            endereco = input("Digite o endereço do mercado: ")

            mercados.criar_mercado(nome, endereco)

        elif opcao == "2":
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

def menu_produtos():
    while True:
        print("===== MENU CRUD Produtos =====")
        print("1. Criar um novo produto")
        print("2. Ler todos os produtos")
        print("3. Ler um produto por ID")
        print("4. Atualizar um produto")
        print("5. Deletar um produto por ID")
        print("Funcoes extras:")
        print("6. Maior preço")
        print("7. Menor preço")
        print("8. Ordem alfabética")
        print("9. total de preco por categoria")
        print("10. total de produtos")
        print("11. Adicionar produto ao mercado")
        print("12. Listar produtos por mercado")
        print("13. Voltar ao menu principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            categoria = input("Digite a categoria do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            preco = float(input("Digite o preço do produto: "))

            prod.criar_produto(nome, categoria, quantidade, preco)

        elif opcao == "2":
            produtos = prod.ler_todos_produtos()
            for produto in produtos:
                print(produto)

        elif opcao == "3":
            id = input("Digite o ID do produto: ")
            produto = prod.ler_produto_por_id(id)
            if produto:
                print(produto)
            else:
                print("Produto não encontrado!")

        elif opcao == "4":
            id = input("Digite o nome do produto que deseja atualizar: ")
            nome = input("Digite o novo nome do produto: ")
            categoria = input("Digite a nova categoria do produto: ")
            quantidade = int(input("Digite a nova quantidade do produto: "))
            preco = float(input("Digite o novo preço do produto: "))

            prod.atualizar_produto(id, nome, categoria, quantidade, preco)

        elif opcao == "5":
            id = input("Digite o nome do produto que deseja deletar: ")
            prod.deletar_produto(id)

        elif opcao == "6":
            print("o produto com maior preço: "+ prod.maior_preco())

        elif opcao == "7":
            print("o produto com menor preço: "+prod.menor_preco())

        elif opcao == "8":
            print("os produtos em ordem alfabetica: "+prod.ordem_alfabetica())

        elif opcao == "9":
            print("os produtos em total por categoria:  "+prod.total_categoria())

        elif opcao == "10":
            print("tem no total "+prod.total_produto()+" produtos no estoque")
            
        elif opcao == "11":
            nome_produto = input("Digite o nome do produto: ")
            nome_mercado = input("Digite o nome do mercado: ")
            prod.adicionar_produto_ao_mercado(nome_produto, nome_mercado)

        elif opcao == "12":
            nome_mercado = input("Digite o nome do mercado: ")
            produtos_lista = prod.ler_produtos_por_mercado(nome_mercado)
            for produto in produtos_lista:
                print(produto)    

        elif opcao == "13":
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
            
def menu_clientes():
    

    while True:
        print("===== MENU CRUD Clientes =====")
        print("1. Criar um novo cliente")
        print("2. Ler todos os clientes")
        print("3. Ler um cliente por ID")
        print("4. Atualizar um cliente")
        print("5. Deletar um cliente pelo nome")
        print("Funcoes extras:")
        print("6. Separar endereço")
        print("7. Ordem alfabética")
        print("8. Maior nome")
        print("9. Comprar um produto")
        print("10. Voltar ao menu principal")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            endereco = input("Digite o endereço do cliente: ")

            clientes.criar_cliente(nome, endereco)

        elif opcao == "2":
            clientes_lista = clientes.ler_todos_clientes()
            for cliente in clientes_lista:
                print(cliente)

        elif opcao == "3":
            id = input("Digite o ID do cliente: ")
            cliente = clientes.ler_cliente_por_id(id)
            if cliente:
                print(cliente)
            else:
                print("Cliente não encontrado!")

        elif opcao == "4":
            id = input("Digite o ID do cliente que deseja atualizar: ")
            nome = input("Digite o novo nome do cliente: ")
            endereco = input("Digite o novo endereço do cliente: ")

            clientes.atualizar_cliente(id, nome, endereco)

        elif opcao == "5":
            id = input("Digite o nome do cliente que deseja deletar: ")
            clientes.deletar_cliente_por_nome(id)
        
        elif opcao =="6":
            print(clientes.separar_endereco())
        
        elif opcao == "7":
            print(clientes.ordem_alfabetica())

        elif opcao == "8":
            print(clientes.maior_nome())
            
        elif opcao == "9":
            nome_cliente = input("Digite o nome do cliente: ")
            nome_produto = input("Digite o nome do produto: ")
            clientes.comprar_produto(nome_cliente, nome_produto)  

        elif opcao == "10":
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

def menu_funcionarios():
    

    while True:
        print("===== MENU CRUD Funcionarios =====")
        print("1. Criar um novo funcionario")
        print("2. Ler todos os funcionarios")
        print("3. Ler um funcionario por ID")
        print("4. Atualizar um funcionario")
        print("5. Deletar um funcionario por nome")
        print("Funcoes extras:")
        print("6. Maior salario")
        print("7. Menor salario")
        print("8. Funcionarios com mais de 60 anos")
        print("9. Funcionarios com menos de 18 anos")
        print("10. Media de idade dos funcionarios")
        print("11. Separar salario")
        print("12. Voltar ao menu principal")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do funcionario: ")
            mercado_id = input("Digite o ID do mercado: ")
            salario = float(input("Digite o salario do funcionario: "))
            idade = int(input("Digite a idade do funcionario: "))

            funcionarios.criar_funcionario(nome, mercado_id, salario, idade)

        elif opcao == "2":
            funcionarios_lista = funcionarios.ler_todos_funcionarios()
            for funcionario in funcionarios_lista:
                print(funcionario)

        elif opcao == "3":
            id = input("Digite o ID do funcionario: ")
            funcionario = funcionarios.ler_funcionario_por_id(id)
            if funcionario:
                print(funcionario)
            else:
                print("Funcionario não encontrado!")

        elif opcao == "4":
            id = input("Digite o ID do funcionario que deseja atualizar: ")
            nome = input("Digite o novo nome do funcionario: ")
            mercado_id = input("Digite o novo ID do mercado: ")
            salario = float(input("Digite o novo salario do funcionario: "))
            idade = int(input("Digite a nova idade do funcionario: "))

            funcionarios.atualizar_funcionario(id, nome, mercado_id, salario, idade)

        elif opcao == "5":
            id = input("Digite o nome do funcionario que deseja deletar: ")
            funcionarios.deletar_funcionario(id)
        
        elif opcao == "6":
            print(funcionarios.maior_salario())
        
        elif opcao == "7":
            print(funcionarios.menor_salario())

        elif opcao == "8":
            print(funcionarios.maior_sessenta())
        
        elif opcao == "9":
            print(funcionarios.menor_dezoito())
        
        elif opcao == "10":
            print(funcionarios.media_idade())
        
        elif opcao == "11":
            print(funcionarios.separar_salario())

        elif opcao == "12":
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
            
def main():
    

    while True:
        print("===== MENU PRINCIPAL =====")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Clientes")
        print("3. Gerenciar Funcionarios")
        print("4. Gerenciar Mercados")
        print("5. Sair do programa")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            menu_produtos()
        elif opcao == "2":
            menu_clientes()
        elif opcao == "3":
            menu_funcionarios()
        elif opcao == "4":
            menu_mercados()    
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()            