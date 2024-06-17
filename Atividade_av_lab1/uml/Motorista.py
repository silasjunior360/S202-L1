from typing import List
class Motorista:
    def __init__(self, nome, corridas, nota):
        self.nome = nome
        self.corridas = corridas
        self.nota = nota

    def adicionar_corrida(self, corridas):
        self.corridas.append(corridas)