from uml.Motorista import Motorista

class MotoristaDAO:
    def __init__(self, database):
        self.db = database
        self.collection = self.db.collection  # Certifique-se de definir a coleção corretamente

    def criar_motorista(self, motorista):
        try:

            self.collection.insert_one({
                "tipo": "motorista",
                "nome": motorista.nome,
                "corridas": motorista.corridas,
                "nota": motorista.nota
            })
            print("Motorista criado com sucesso!")
        except Exception as e:
            print(e)

    def ler_motorista(self, nota):
        try:
            dados_motorista = self.collection.find_one({"nota": nota})
            if dados_motorista:
                return Motorista(dados_motorista["nome"], dados_motorista["corridas"], dados_motorista["nota"])
            else:
                print("Motorista não encontrado.")
                return None
        except Exception as e:
            print(e)

    def atualizar_motorista(self, nota, nova_nota):
        try:
            self.collection.update_one({"nota": nota}, {"$set": {"nota": nova_nota}})
            print("Motorista atualizado com sucesso!")
        except Exception as e:
            print(e)

    def deletar_motorista(self, nota):
        try:
            self.collection.delete_one({"nota": nota})
            print("Motorista deletado com sucesso!")
        except Exception as e:
            print(e)
