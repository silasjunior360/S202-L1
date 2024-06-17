from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def create_and_return_example(tx, nome, sexo, idade):
    query = """
        CREATE (n:Pessoa {
            nome: $nome,
            sexo: $sexo,
            idade: $idade})
    """
    tx.run(
        query,
        nome=nome,
        sexo=sexo,
        idade=idade
        )
    try:
        tx.run(query, nome=nome, sexo=sexo, idade=idade)
        
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

def get_amount_data(tx):
    query = """
        MATCH(n) RETURN COUNT(n) AS amount;
    """
    try:
        result = tx.run(query)
        return [{'amount':row['amount']} for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

# Função para encontrar os pets na família
def pets(tx):
    query = """
        MATCH (p:Pessoa)-[:DONO_DE]->(pet:Pet) 
        RETURN p.nome AS pessoa, pet.nome AS pet
    """
    try:
        result = tx.run(query)
        return [{'pessoa': row['pessoa'], 'pet': row['pet']} for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

# Função para encontrar a avó de Silas Jr
def avo_silasjr(tx):
    query = """
        MATCH (avo:Pessoa)-[:AVO_DE]->(:Pessoa {nome: 'Silas Jr'})
        RETURN avo.nome AS nome
    """
    try:
        result = tx.run(query)
        return [{'nome': row['nome']} for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

# Função para encontrar a esposa de Silas
def esposa(tx):
    query = """
        MATCH (esposa:Pessoa)-[:ESPOSA_DE]->(:Pessoa)
        RETURN esposa.nome AS nome_da_esposa
    """
    try:
        result = tx.run(query)
        return [{'nome': row['nome_da_esposa']} for row in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

# Função para exibir o menu e realizar ações com base na escolha do usuário
def menu(driver):
    print("1. Criar novo nó de família")
    print("2. Quem é Pet na família?")
    print("3. Quem é avô de Silas Jr?")
    print("4. Quem sé a esposa de Silas")
    print("5. Numero de nós:")
    print("6. Sair")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        nome = input("Digite o nome: ")
        sexo = input("Digite o sexo: ")
        idade = int(input("Digite a idade: "))
        with driver.session() as session:
            session.write_transaction(create_and_return_example, nome, sexo, idade)
    elif choice == "2":
        with driver.session() as session:
            result = session.read_transaction(pets)
            print("Pets na família:")
            for row in result:
                print(f"{row['pessoa']} tem um pet chamado {row['pet']}")
            
    elif choice == "3":
        with driver.session() as session:
            result = session.execute_read(avo_silasjr)
            for row in result:
                print(f"A avô de Silas Jr é: {row['nome']}")
           
    elif choice == "4":
        with driver.session() as session:
            result = session.read_transaction(esposa)
            if result:
                print(f"A esposa de Silas é: {result[0]['nome']}")
            else:
                print("Não foi encontrada a esposa de Silas.")
            
                
    elif choice == "6":
        return False
    elif choice == "5":
        with driver.session() as session:
            result = session.execute_read(get_amount_data)
            print(result[0]['amount'])
    else:
        print("Escolha inválida!")
    return True

uri = "neo4j+s://a57719eb.databases.neo4j.io"
user = "neo4j"
password = "BQYOY8eviKvnAV42X2Hd6Txu8bcPbWYSdj6_7Mi3vSk"

driver = GraphDatabase.driver(uri, auth=(user, password))


while True:
    menu(driver)
    cont = input("Deseja continuar? (s/n): ")
    if cont.lower() != "s":
        break