from uml.Passageiro import Passageiro

class PassageiroDAO:
    def __init__(self, database):
        self.db = database

    def criar_passageiro(self, passageiro):
        try:
            self.db.colecao.insert_one({
                "nome": passageiro.nome,
                "documento": passageiro.documento
            })
            print("Passageiro criado com sucesso!")
        except Exception as e:
            print(e)

    def ler_passageiro(self, documento):
        try:
            dados_passageiro = self.db.colecao.find_one({"documento": documento})
            if dados_passageiro:
                return Passageiro(dados_passageiro["nome"], dados_passageiro["documento"])
            else:
                print("Passageiro não encontrado.")
                return None
        except Exception as e:
            print(e)

    def atualizar_passageiro(self, documento, novo_documento):
        try:
            self.db.colecao.update_one({"documento": documento}, {"$set": {"documento": novo_documento}})
            print("Passageiro atualizado com sucesso!")
        except Exception as e:
            print(e)

    def deletar_passageiro(self, documento):
        try:
            self.db.colecao.delete_one({"documento": documento})
            print("Passageiro deletado com sucesso!")
        except Exception as e:
            print(e)
