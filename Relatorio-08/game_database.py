class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, match_id, player_ids, results):
        query = """
        CREATE (m:Match {match_id: $match_id})
        WITH m
        UNWIND $player_ids AS player_id
        MATCH (p:Player) WHERE ID(p) = player_id
        MERGE (m)-[:PARTICIPATES]->(p)
        SET p.result = $results[POSITION(player_ids, player_id)]
        """
        parameters = {"match_id": match_id, "player_ids": player_ids, "results": results}
        self.db.execute_query(query, parameters)

    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player) WHERE ID(p) = $player_id SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_id):
        query = "MATCH (p:Player) WHERE ID(p) = $player_id DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN ID(p) AS player_id, p.name AS name"
        results = self.db.execute_query(query)
        return [{"id": result["player_id"], "name": result["name"]} for result in results]

    def get_player_matches(self, player_id):
        query = """
        MATCH (p:Player)-[:PARTICIPATES]->(m:Match)
        WHERE ID(p) = $player_id
        RETURN m.match_id AS match_id, p.result AS result
        """
        parameters = {"player_id": player_id}
        results = self.db.execute_query(query, parameters)
        return [{"match_id": result["match_id"], "result": result["result"]} for result in results]

    def get_match_info(self, match_id):
        query = """
        MATCH (m:Match {match_id: $match_id})
        RETURN m.match_id AS match_id, [(p.name, p.result) | (m)-[:PARTICIPATES]->(p:Player)]
        """
        parameters = {"match_id": match_id}
        result = self.db.execute_query(query, parameters)
        if result:
            match_info = result[0]
            return {
                "match_id": match_info["match_id"],
                "players": [{"name": player[0], "result": player[1]} for player in match_info[1]]
            }
        else:
            return None
