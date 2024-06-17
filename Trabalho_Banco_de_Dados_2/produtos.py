class ProdutosDatabase:
    def __init__(self, database):
        self.db = database

    def criar_produto(self, nome, categoria, quantidade, preco):
        query = "CREATE (:Produto {nome: $nome, categoria: $categoria, quantidade: $quantidade, preco: $preco})"
        parameters = {"nome": nome, "categoria": categoria, "quantidade": quantidade, "preco": preco}
        self.db.execute_query(query, parameters)

    def atualizar_produto(self, nome_produto, novo_nome, nova_categoria, nova_quantidade, novo_preco):
        query = """
        MATCH (p:Produto {nome: $nome_produto})
        SET p.nome = $novo_nome, p.categoria = $nova_categoria, p.quantidade = $nova_quantidade, p.preco = $novo_preco
        """
        parameters = {
            "nome_produto": nome_produto,
            "novo_nome": novo_nome,
            "nova_categoria": nova_categoria,
            "nova_quantidade": nova_quantidade,
            "novo_preco": novo_preco
        }
        self.db.execute_query(query, parameters)

    def deletar_produto(self, nome_produto):
        query = """
        MATCH (p:Produto {nome: $nome_produto})
        DETACH DELETE p
        """
        parameters = {"nome_produto": nome_produto}
        self.db.execute_query(query, parameters)

    def ler_todos_produtos(self):
        query = "MATCH (p:Produto) RETURN ID(p) AS produto_id, p.nome AS nome, p.categoria AS categoria, p.quantidade AS quantidade, p.preco AS preco"
        results = self.db.execute_query(query)
        return [{"id": result["produto_id"], "nome": result["nome"], "categoria": result["categoria"], "quantidade": result["quantidade"], "preco": result["preco"]} for result in results]
    def ler_produto_por_id(self, produto_id):
        query = "MATCH (p:Produto) WHERE ID(p) = $produto_id RETURN ID(p) AS produto_id, p.nome AS nome, p.categoria AS categoria, p.quantidade AS quantidade, p.preco AS preco"
        parameters = {"produto_id": produto_id}
        results = self.db.execute_query(query, parameters)
        if results:
            result = results[0]
            return {
                "id": result["produto_id"],
                "nome": result["nome"],
                "categoria": result["categoria"],
                "quantidade": result["quantidade"],
                "preco": result["preco"]
            }
        else:
            return None

    def maior_preco(self):
        query = """
        MATCH (p:Produto)
        RETURN p.nome AS nome, p.preco AS preco
        ORDER BY p.preco DESC
        LIMIT 1
        """
        result = self.db.execute_query(query)
        if result:
            return f"Produto com maior preço: {result[0]['nome']} - R${result[0]['preco']}"
        else:
            return "Não há produtos cadastrados."

    def menor_preco(self):
        query = """
        MATCH (p:Produto)
        RETURN p.nome AS nome, p.preco AS preco
        ORDER BY p.preco ASC
        LIMIT 1
        """
        result = self.db.execute_query(query)
        if result:
            return f"Produto com menor preço: {result[0]['nome']} - R${result[0]['preco']}"
        else:
            return "Não há produtos cadastrados."

    def ordem_alfabetica(self):
        query = """
        MATCH (p:Produto)
        RETURN p.nome AS nome
        ORDER BY p.nome
        """
        results = self.db.execute_query(query)
        if results:
            produtos = [result['nome'] for result in results]
            return ", ".join(produtos)
        else:
            return "Não há produtos cadastrados."

    def total_categoria(self):
        query = """
        MATCH (p:Produto)
        RETURN p.categoria AS categoria, sum(p.preco) AS total_preco
        ORDER BY p.categoria
        """
        results = self.db.execute_query(query)
        if results:
            categorias = [f"{result['categoria']}: R${result['total_preco']}" for result in results]
            return "\n".join(categorias)
        else:
            return "Não há produtos cadastrados."

    def total_produto(self):
        query = """
        MATCH (p:Produto)
        RETURN count(p) AS total
        """
        result = self.db.execute_query(query)
        if result:
            total = result[0]['total']
            return f"Total de produtos: {total}"
        else:
            return "Não há produtos cadastrados."

    def adicionar_produto_ao_mercado(self, nome_produto, nome_mercado):
        query = """
        MATCH (p:Produto {nome: $nome_produto})
        MATCH (m:Mercado {nome: $nome_mercado})
        CREATE (p)-[:DISPONIVEL_EM]->(m)
        """
        parameters = {
            "nome_produto": nome_produto,
            "nome_mercado": nome_mercado
        }
        self.db.execute_query(query, parameters)

    def ler_produtos_por_mercado(self, nome_mercado):
        query = """
        MATCH (p:Produto)-[:DISPONIVEL_EM]->(m:Mercado {nome: $nome_mercado})
        RETURN p.nome AS nome
        """
        parameters = {"nome_mercado": nome_mercado}
        results = self.db.execute_query(query, parameters)
        if results:
            produtos = [result['nome'] for result in results]
            return produtos
        else:
            return f"Nenhum produto disponível no mercado {nome_mercado}"