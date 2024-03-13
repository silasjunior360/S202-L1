from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

#1-Retorne o total de vendas por dia
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$data_compra","total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}   
])
writeAJson(result, "Total de vendas por dia")

#2-Retorne o produto mais vendido em todas as compras.
result = db.collection.aggregate([
     {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total_vendas": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total_vendas": -1}},
    {"$limit": 1},
    {"$project": {"_id": 0, "produto_mais_vendido": "$_id", "total_vendas": 1}}
])
writeAJson(result, "produto mais vendido em todas as compras")

# #3-Encontre o cliente que mais gastou em uma única compra.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"total_gasto": -1}},
    {"$limit": 1}
])
writeAJson(result, "cliente que mais gastou em uma única compra")

# #4-Liste todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
result = db.collection.aggregate([
   {"$unwind": "$produtos"},
    {"$match": {"produtos.quantidade": {"$gt": 1}}},
    {"$group": {"_id": "$produtos.descricao"}}
])
writeAJson(result, "Todos os produtos que tiveram uma quantidade vendida acima de 1 unidades")
