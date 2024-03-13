from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
#db.resetDatabase()
result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
])

writeAJson(result, "Média de gasto total")
#1-Retorne o total de vendas por dia
#result = db.collection.aggregate([
    # {"$unwind": "$produtos"},
    # {"$group": {"_id": "$date", "total_vendas": {"$sum": "$quantity"}}}
#])
#writeAJson(result, "Total de vendas por dia")

# #2-Retorne o produto mais vendido em todas as compras.
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$product", "total_vendas": {"$sum": "$quantity"}}},
#     {"$sort": {"total_vendas": -1}},
#     {"$limit": 1}
# ])
# writeAJson(result, "produto mais vendido em todas as compras")

# #3-Encontre o cliente que mais gastou em uma única compra.
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$customer", "total_gasto": {"$sum": {"$multiply": ["$quantity", "$price"]}}}},
#     {"$sort": {"total_gasto": -1}},
#     {"$limit": 1}
# ])
# writeAJson(result, "cliente que mais gastou em uma única compra")

# #4-Liste todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$match": {"quantity": {"$gt": 1}}},
#     {"$group": {"_id": "$product"}}
# ])
# writeAJson(result, "Todos os produtos que tiveram uma quantidade vendida acima de 1 unidades")
