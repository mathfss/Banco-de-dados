from neo4j import GraphDatabase
from game_database import GameDatabase

uri = "bolt://3.238.0.229:7687"
username = "neo4j"
password = "pitch-quarterdeck-anthem"

db = GameDatabase(uri, username, password)

db.create_player("Player 1")
db.create_player("Player 2")
db.create_player("Player 3")

print("Lista de jogadores:")
print(db.get_players())

db.create_match(["Player 1", "Player 2", "Player 3"])

match_id = db.get_match(1)
print("\nInformações da partida:")
print(match_id)

db.register_match_result(match_id, "Player 1 venceu")

print("\nHistórico de partidas do jogador:")
print(db.get_player_match_history("Player 1"))

db.delete_player("Player 3")

db.close()