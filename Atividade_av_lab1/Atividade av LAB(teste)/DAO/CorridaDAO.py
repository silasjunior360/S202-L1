from uml.Corrida import Corrida
class CorridaDAO:
    def __init__(self, database):
        self.db = database

    def criar_corrida(self, corrida):
        try:
            self.db.colecao.insert_one({
                "nota": corrida.nota,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro": corrida.passageiro,
                "motorista": corrida.motorista
            })
            print("Corrida criada com sucesso!")
        except Exception as e:
            print(e)

    def ler_corrida(self, nota):
        try:
            dados_corrida = self.db.colecao.find_one({"nota": nota})
            if dados_corrida:
                return Corrida(dados_corrida["nota"], dados_corrida["distancia"], dados_corrida["valor"], dados_corrida["passageiro"], dados_corrida["motorista"])
            else:
                print("Corrida não encontrada.")
                return None
        except Exception as e:
            print(e)

    def atualizar_corrida(self, nota, nova_nota):
        try:
            self.db.colecao.update_one({"nota": nota}, {"$set": {"nota": nova_nota}})
            print("Corrida atualizada com sucesso!")
        except Exception as e:
            print(e)

    def deletar_corrida(self, nota):
        try:
            self.db.colecao.delete_one({"nota": nota})
            print("Corrida deletada com sucesso!")
        except Exception as e:
            print(e)
