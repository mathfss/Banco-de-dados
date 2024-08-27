from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return [record for record in result]

def query1_1(db):
    query = "MATCH (t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf"
    return db.execute_query(query)

def query1_2(db):
    query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
    return db.execute_query(query)

def query1_3(db):
    query = "MATCH (c:City) RETURN c.name"
    return db.execute_query(query)

def query1_4(db):
    query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
    return db.execute_query(query)

def query2_1(db):
    query = "MATCH (t:Teacher) RETURN min(t.ano_nasc) as oldest, max(t.ano_nasc) as youngest"
    return db.execute_query(query)

def query2_2(db):
    query = "MATCH (c:City) RETURN avg(c.population) as avg_population"
    return db.execute_query(query)

def query2_3(db):
    query = "MATCH (c:City{cep:'37540-000'}) RETURN replace(c.name, 'a', 'A') as modified_name"
    return db.execute_query(query)

def query2_4(db):
    query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) as third_char"
    return db.execute_query(query)
