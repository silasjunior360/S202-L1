class ClientesDatabase:
    def __init__(self, database):
        self.db = database

    def criar_cliente(self, nome, endereco):
        query = "CREATE (:Cliente {nome: $nome, endereco: $endereco})"
        parameters = {"nome": nome, "endereco": endereco}
        self.db.execute_query(query, parameters)

    def atualizar_cliente(self, cliente_id, novo_nome, novo_endereco):
        query = """
        MATCH (c:Cliente) WHERE ID(c) = $cliente_id
        SET c.nome = $novo_nome, c.endereco = $novo_endereco
        """
        parameters = {"cliente_id": cliente_id, "novo_nome": novo_nome, "novo_endereco": novo_endereco}
        self.db.execute_query(query, parameters)

    def deletar_cliente_por_nome(self, nome_cliente):
        query = """
        MATCH (c:Cliente {nome: $nome_cliente})
        DETACH DELETE c
        """
        parameters = {"nome_cliente": nome_cliente}
        self.db.execute_query(query, parameters)

    def ler_todos_clientes(self):
        query = "MATCH (c:Cliente) RETURN ID(c) AS cliente_id, c.nome AS nome, c.endereco AS endereco"
        results = self.db.execute_query(query)
        return [{"id": result["cliente_id"], "nome": result["nome"], "endereco": result["endereco"]} for result in results]

    def ler_cliente_por_id(self, cliente_id):
        query = "MATCH (c:Cliente) WHERE ID(c) = $cliente_id RETURN ID(c) AS cliente_id, c.nome AS nome, c.endereco AS endereco"
        parameters = {"cliente_id": cliente_id}
        results = self.db.execute_query(query, parameters)
        if results:
            result = results[0]
            return {"id": result["cliente_id"], "nome": result["nome"], "endereco": result["endereco"]}
        else:
            return None
    def separar_endereco(self):
        query = "MATCH (c:Cliente) RETURN c.endereco ORDER BY c.endereco"
        results = self.db.execute_query(query)
        return results
    
    def ordem_alfabetica(self):
        query = "MATCH (c:Cliente) RETURN c.nome ORDER BY c.nome"
        results = self.db.execute_query(query)
        return results

    def maior_nome(self):
        query = "MATCH (c:Cliente) RETURN max(c.nome) as maior_nome"
        results = self.db.execute_query(query)
        return results[0]["maior_nome"]
    
    def ler_cliente_por_nome(self, nome):
        query = "MATCH (c:Cliente) WHERE c.nome = $nome RETURN ID(c) AS cliente_id, c.nome AS nome, c.endereco AS endereco"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        if results:
            result = results[0]
            return {"id": result["cliente_id"], "nome": result["nome"], "endereco": result["endereco"]}
        else:
            return None

    def comprar_produto(self, nome_cliente, nome_produto):
        # Buscar o cliente pelo nome
        cliente = self.ler_cliente_por_nome(nome_cliente)
        if not cliente:
            print("Cliente não encontrado.")
            return

        # Buscar o produto pelo nome e verificar a disponibilidade
        produto_query = "MATCH (p:Produto) WHERE p.nome = $nome_produto AND p.quantidade > 0 RETURN p"
        produto_parameters = {"nome_produto": nome_produto}
        produto_result = self.db.execute_query(produto_query, produto_parameters)

        if not produto_result:
            print("Produto não disponível ou esgotado.")
            return

        produto_id = produto_result[0]["p"].id

        # Criar relação de compra e atualizar a quantidade do produto
        compra_query = """
        MATCH (c:Cliente), (p:Produto)
        WHERE ID(c) = $cliente_id AND ID(p) = $produto_id
        CREATE (c)-[:COMPROU]->(p)
        SET p.quantidade = p.quantidade - 1
        """
        compra_parameters = {"cliente_id": cliente["id"], "produto_id": produto_id}
        self.db.execute_query(compra_query, compra_parameters)
        print("Compra realizada com sucesso.")