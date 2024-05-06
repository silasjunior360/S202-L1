from database import Database
from game_database import GameDatabase


db = Database("bolt://18.206.64.147:7687", "neo4j", "hertz-sails-collar")
db.drop_all()


game_db = GameDatabase(db)

# Criando alguns jogadores
game_db.create_player("Beiçola")
game_db.create_player("LuanGameplays")
game_db.create_player("Belabelinha")


game_db.create_match(1, [0, 1], [10, 5])  
game_db.create_match(2, [0, 2], [8, 12])  
game_db.create_match(3, [1, 2], [7, 9])   


game_db.update_player(2, "JOAOGAMEPLAY")

game_db.delete_player(0)  


print("Jogadores:")

print(game_db.get_players())


robert_matches = game_db.get_player_matches(2)  
print("Histórico de partidas de Robert:")
for match in robert_matches:
    print(f"Partida ID: {match['match_id']}, Resultado: {match['result']}")


match_info = game_db.get_match_info(2)
print("Informações sobre a Partida ID 2:")
print(f"Jogadores: {', '.join([player['name'] for player in match_info['players']])}")
print(f"Resultado: {[player['result'] for player in match_info['players']]}")


db.close()
