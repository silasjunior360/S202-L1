from database import Database
from product_analyzer import Product_analyzer

db = Database(database="mercado", collection="compras")
#db.resetDatabase()
p =Product_analyzer(db)

#1 Mostra total de vendas por dia
p.cliente_que_mais_gastou()
#2 mostra produto mais vendido em todas as compras.
p.produto_mais_vendido()
#3 Encontra cliente que mais gastou em uma única compra.
p.produtos_com_quantidade_acima_de_um()
#4 Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
p.total_vendas_por_dia()
