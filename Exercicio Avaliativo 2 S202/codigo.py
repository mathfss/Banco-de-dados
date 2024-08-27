from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

class FamiliaGrafo:
    def __init__(self, uri, usuario, senha):
        self.driver = GraphDatabase.driver(uri, auth=(usuario, senha))

    def close(self):
        self.driver.close()

    def pais(self, filho):
        with self.driver.session() as session:
            query = """
                MATCH (filho:Pessoa {nome: $filho})<-[:PAI_MAE_DE]-(pai:Pessoa)
                RETURN pai
            """
            resultado = session.run(query, filho=filho)
            return [registro["pai"] for registro in resultado]

    def filhos(self, pai):
        with self.driver.session() as session:
            query = """
                MATCH (pai:Pessoa {nome: $pai})-[:PAI_MAE_DE]->(filho:Pessoa)
                RETURN filho
            """
            resultado = session.run(query, pai=pai)
            return [registro["filho"] for registro in resultado]

    def animais(self, dono):
        with self.driver.session() as session:
            query = """
                MATCH (dono:Pessoa {nome: $dono})-[:DONO_DE]->(pet:Pet)
                RETURN pet
            """
            resultado = session.run(query, dono=dono)
            return [registro["pet"] for registro in resultado]

uri = "bolt://localhost:7687"
user = "neo4j"
password = "neo4j"

driver = FamiliaGrafo(uri, user, password)

# quem são os pais de Carlos?
pais = driver.pais("Carlos")
print("Os pais de Carlos são:")
for pai in pais:
    print(pai["nome"])

# quais são os filhos de Maria?
filhos = driver.filhos("Maria")
print("Os filhos de Maria são:")
for filho in filhos:
    print(filho["nome"])

# quais são os animais de estimação de João?
animais = driver.animais("João")
print("Os animais de estimação de João são:")
for animal in animais:
    print(animal["nome"])

driver.close()