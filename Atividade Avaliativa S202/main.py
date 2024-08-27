from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def consultar_estoque(carro):
    cloud_config = {
        'secure_connect_bundle': 'C:\Users\jaspi\Downloads\secure-connect-automoveis-db.zip'
    }
    auth_provider = PlainTextAuthProvider('<QSPoIzUMacnJrjzJZkDDYvOZ>', '<-,C_snezWee0_AaWKCFN76KxLICMdCaLR_lsYvSe4_TFXX4RChMyzRrL27blQENIxhI+GLoxrJw,g99Ggy1lmwwhPfFzRASiW3G0f5sZk8uTloiq1Ek1+UZl0t0602Cz>')

    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()

    session.set_keyspace('default_keyspace')

    query = "SELECT nome, estante, quantidade FROM estoque WHERE carro = %s"
    
    result = session.execute(query, [carro])

    print(f"Consulta de estoque para o carro '{carro}':")
    for row in result:
        print(f"Nome: {row.nome}, Estante: {row.estante}, Quantidade: {row.quantidade}")

    cluster.shutdown()

carro = input("Digite o nome do carro para consultar o estoque: ")

consultar_estoque(carro)
