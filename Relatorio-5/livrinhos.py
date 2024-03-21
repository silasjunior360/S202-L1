from pymongo import MongoClient
from bson.objectid import ObjectId

class Livrinhos:
    def __init__(self, database):
        self.db = database

    def criar_livro(self, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Livro criado com ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o livro: {e}")
            return None

    def ler_todos_livros(self):
        try:
            res = self.db.collection.find()
            for livro in res:
                print(livro)
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler todos os livros: {e}")
            return None

    def ler_livro_por_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Livro encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler o livro: {e}")
            return None

    def atualizar_livro(self, id: str, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            print(f"Livro atualizado: {res.modified_count} documento(s) modificados")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def deletar_livro_por_id(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {res.deleted_count} documento(s) deletados")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None