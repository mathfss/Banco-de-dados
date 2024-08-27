from neo4j import GraphDatabase

class GameDatabase:
    def __init__(self, uri, username, password):
        self._driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self._driver.close()

    def create_player(self, player_name):
        with self._driver.session() as session:
            session.write_transaction(self._create_player, player_name)

    def _create_player(self, tx, player_name):
        tx.run("CREATE (p:Player {name: $name})", name=player_name)

    def get_players(self):
        with self._driver.session() as session:
            return session.read_transaction(self._get_players)

    def _get_players(self, tx):
        result = tx.run("MATCH (p:Player) RETURN p.name AS player_name")
        return [record["player_name"] for record in result]

    def delete_player(self, player_name):
        with self._driver.session() as session:
            session.write_transaction(self._delete_player, player_name)

    def _delete_player(self, tx, player_name):
        tx.run("MATCH (p:Player {name: $name}) DETACH DELETE p", name=player_name)

    def create_match(self, players, result=None):
        with self._driver.session() as session:
            session.write_transaction(self._create_match, players, result)

    def _create_match(self, tx, players, result):
        result_query = ", result: $result" if result else ""
        result = tx.run(f"CREATE (m:Match {result_query}) RETURN id(m) AS match_id", result=result)
        match_id = result.single()["match_id"]
        for player in players:
            tx.run("MATCH (p:Player {name: $name}), (m:Match) WHERE id(m) = $match_id "
                   "CREATE (p)-[:PARTICIPATED_IN]->(m)", name=player, match_id=match_id)

    def get_match(self, match_id):
        with self._driver.session() as session:
            return session.read_transaction(self._get_match, match_id)

    def _get_match(self, tx, match_id):
        result = tx.run("MATCH (m:Match) WHERE id(m) = $match_id "
                        "RETURN id(m) AS match_id", match_id=match_id)
        record = result.single()
        return record["match_id"] if record else None

    def register_match_result(self, match_id, result):
        with self._driver.session() as session:
            session.write_transaction(self._register_match_result, match_id, result)

    def _register_match_result(self, tx, match_id, result):
        tx.run("MATCH (m:Match) WHERE id(m) = $match_id SET m.result = $result",
               match_id=match_id, result=result)

    def get_player_match_history(self, player_name):
        with self._driver.session() as session:
            return session.read_transaction(self._get_player_match_history, player_name)

    def _get_player_match_history(self, tx, player_name):
        result = tx.run("MATCH (p:Player {name: $name})-[:PARTICIPATED_IN]->(m:Match) "
                        "RETURN id(m) AS match_id, m.result AS result", name=player_name)
        return [{"match_id": record["match_id"], "result": record["result"]} for record in result]
