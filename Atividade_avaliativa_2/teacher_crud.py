#Questao 3 
#a
class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = f"CREATE (:Teacher{{name:'{name}', ano_nasc:{ano_nasc}, cpf:'{cpf}'}})"
        self.db.run(query)

    def read(self, name):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) RETURN t"
        result = self.db.run(query)
        return result.single()

    def delete(self, name):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) DELETE t"
        self.db.run(query)

    def update(self, name, newCpf):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) SET t.cpf = '{newCpf}'"
        self.db.run(query)
