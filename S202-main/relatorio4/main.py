from database import Database
from helper.writeAJson import writeAJson
from ProductAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

# 1- Média de gasto total:
#result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
#])
#
#writeAJson(result, "Média de gasto total")

# 2- Cliente que mais comprou em cada dia:
#result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$sort": {"_id.data": 1, "total": -1}},
#     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
#])
#
#writeAJson(result, "Cliente que mais comprou em cada dia")

# 3- Produto mais vendido:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])

writeAJson(result, "Produto mais vendido")

analyzer = ProductAnalyzer(db)

result1 = analyzer.total_de_vendas_por_dia()
writeAJson(result1, "Total de vendas por dia")

result2 = analyzer.produto_mais_vendido()
writeAJson(result2, "Produto mais vendido")

result3 = analyzer.cliente_que_mais_gastou()
writeAJson(result3, "Cliente que mais gastou em uma única compra")

result4 = analyzer.produtos_com_vendas_acima_de_um()
writeAJson(result4, "Produtos vendidos acima de uma unidade")
