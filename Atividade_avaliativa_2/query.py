from database import Database

db = Database("bneo4j+s://a57719eb.databases.neo4j.io", "neo4j", "BQYOY8eviKvnAV42X2Hd6Txu8bcPbWYSdj6_7Mi3vSk")
# questao 1
#a
result = db.run("MATCH (t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf")
for record in result:
    print(record)

#b
result = db.run("MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf")
for record in result:
    print(record)

#c
result = db.run("MATCH (c:City) RETURN c.name")
for record in result:
    print(record)

#d
result = db.run("MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number")
for record in result:
    print(record)

#questao 2
#a
result = db.run("MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS mais_jovem, MAX(t.ano_nasc) AS mais_velho")
for record in result:
    print(record)

#b
result = db.run("MATCH (c:City) RETURN AVG(c.population) AS media_populacional")
for record in result:
    print(record)

#c
result = db.run("MATCH (c:City{cep:'37540-000'}) RETURN REPLACE(c.name, 'a', 'A') AS nome_modificado")
for record in result:
    print(record)

#d
result = db.run("MATCH (t:Teacher) RETURN SUBSTRING(t.name, 3, 1) AS terceira_letra")
for record in result:
    print(record)

db.close()
