class FuncionariosDatabase:
    def __init__(self, database):
        self.db = database

    def criar_funcionario(self, nome, mercado_id, salario, idade):
        query = """
        CREATE (:Funcionario {nome: $nome, mercado_id: $mercado_id, salario: $salario, idade: $idade})
        """
        parameters = {
            "nome": nome,
            "mercado_id": mercado_id,
            "salario": salario,
            "idade": idade
        }
        self.db.execute_query(query, parameters)

    def ler_todos_funcionarios(self):
        query = """
        MATCH (f:Funcionario)
        RETURN ID(f) AS funcionario_id, f.nome AS nome, f.mercado_id AS mercado_id, f.salario AS salario, f.idade AS idade
        """
        results = self.db.execute_query(query)
        return [{
            "id": result["funcionario_id"],
            "nome": result["nome"],
            "mercado_id": result["mercado_id"],
            "salario": result["salario"],
            "idade": result["idade"]
        } for result in results]

    def ler_funcionario_por_id(self, funcionario_id):
        query = """
        MATCH (f:Funcionario) WHERE ID(f) = $funcionario_id
        RETURN ID(f) AS funcionario_id, f.nome AS nome, f.mercado_id AS mercado_id, f.salario AS salario, f.idade AS idade
        """
        parameters = {"funcionario_id": funcionario_id}
        results = self.db.execute_query(query, parameters)
        if results:
            result = results[0]
            return {
                "id": result["funcionario_id"],
                "nome": result["nome"],
                "mercado_id": result["mercado_id"],
                "salario": result["salario"],
                "idade": result["idade"]
            }
        else:
            return None

    def atualizar_funcionario(self, funcionario_id, novo_nome, novo_mercado_id, novo_salario, nova_idade):
        query = """
        MATCH (f:Funcionario) WHERE ID(f) = $funcionario_id
        SET f.nome = $novo_nome, f.mercado_id = $novo_mercado_id, f.salario = $novo_salario, f.idade = $nova_idade
        """
        parameters = {
            "funcionario_id": funcionario_id,
            "novo_nome": novo_nome,
            "novo_mercado_id": novo_mercado_id,
            "novo_salario": novo_salario,
            "nova_idade": nova_idade
        }
        self.db.execute_query(query, parameters)

    def deletar_funcionario(self, nome):
        query = """
        MATCH (f:Funcionario {nome: $nome})
        DETACH DELETE f
        """
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def maior_salario(self):
        query = "MATCH (f:Funcionario) RETURN max(f.salario) as maior_salario"
        results = self.db.execute_query(query)
        return results[0]["maior_salario"]

    def menor_salario(self):
        query = "MATCH (f:Funcionario) RETURN min(f.salario) as menor_salario"
        results = self.db.execute_query(query)
        return results[0]["menor_salario"]

    def maior_sessenta(self):
        query = "MATCH (f:Funcionario) WHERE f.idade > 60 RETURN f.nome ORDER BY f.nome"
        results = self.db.execute_query(query)
        return results
    
    def menor_dezoito(self):
        query = "MATCH (f:Funcionario) WHERE f.idade < 18 RETURN f.nome ORDER BY f.nome"
        results = self.db.execute_query(query)
        return results

    def media_idade(self):
        query = "MATCH (f:Funcionario) RETURN avg(f.idade) as media_idade"
        results = self.db.execute_query(query)
        return results[0]["media_idade"]

    def separar_salario(self):
        query = "MATCH (f:Funcionario) RETURN f.salario ORDER BY f.salario"
        results = self.db.execute_query(query)
        return results