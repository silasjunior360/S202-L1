class MercadosDatabase:
    def __init__(self, database):
        self.db = database

    def criar_mercado(self, nome, endereco):
        query = "CREATE (:Mercado {nome: $nome, endereco: $endereco})"
        parameters = {"nome": nome, "endereco": endereco}
        self.db.execute_query(query, parameters)
        
    def ler_mercado_por_id(self, mercado_id):
        query = "MATCH (m:Mercado) WHERE ID(m) = $mercado_id RETURN ID(m) AS mercado_id, m.nome AS nome, m.endereco AS endereco"
        parameters = {"mercado_id": mercado_id}
        results = self.db.execute_query(query, parameters)
        if results:
            result = results[0]
            return {"id": result["mercado_id"], "nome": result["nome"], "endereco": result["endereco"]}
        else:
            return None

    def ler_mercado_por_nome(self, nome):
        query = "MATCH (m:Mercado) WHERE m.nome = $nome RETURN ID(m) AS mercado_id, m.nome AS nome, m.endereco AS endereco"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        if results:
            result = results[0]
            return {"id": result["mercado_id"], "nome": result["nome"], "endereco": result["endereco"]}
        else:
            return None    