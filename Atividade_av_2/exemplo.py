from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def create_and_return_example(tx, code, test_data):
        query = """
            CREATE(n:FAMILIA{
                nome: $nome,
                sexo: $sexo,
                idade: $idade
            })
        """
        result = tx.run(
            query, 
            test_data = test_data,
            code = code
        )

        try:
            return [{"test_data": row["n"]["description"]} for row in result]

        # Capture any errors along with the query and data for traceability

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

uri = "neo4j+s://a57719eb.databases.neo4j.io"
user = "neo4j"
password = "BQYOY8eviKvnAV42X2Hd6Txu8bcPbWYSdj6_7Mi3vSk"

driver = GraphDatabase.driver(uri, auth=(user, password))

#nome=input("Digite o nome: ")
#sexo=input("Digite sexo: ")
#idade=int(input("Digite a idade: "))

#with driver.session() as session:
#    session.execute_write(create_and_return_example, nome, sexo, idade)

with driver.session() as session:
    result = session.execute_read(get_amount_data)
    print(result[0]['amount'])
driver.close()