from uml.Motorista import Motorista
from CLI.cli import SimpleCLI

class MotoristaCLI(SimpleCLI):
    def __init__(self, dao_motorista):
        super().__init__()
        self.dao_motorista = dao_motorista
        self.add_command("criar", self.criar_motorista)
        self.add_command("ler", self.ler_motorista)
        self.add_command("atualizar", self.atualizar_motorista)
        self.add_command("deletar", self.deletar_motorista)

    def criar_motorista(self):
        nome = input("Digite o nome do motorista: ")
        corridas = int(input("Digite o número de corridas do motorista: "))
        nota = int(input("Digite a nota do motorista: "))
        motorista = Motorista(nome, corridas, nota)
        self.dao_motorista.criar_motorista(motorista)
        print("Motorista criado com sucesso!")

    def ler_motorista(self):
        nota = int(input("Digite a nota do motorista que deseja ler: "))
        motorista = self.dao_motorista.ler_motorista(nota)
        if motorista:
            print(f"Nome: {motorista.nome}")
            print(f"Nota: {motorista.nota}")
            print(f"Número de corridas: {motorista.corridas}")

    def atualizar_motorista(self):
        nota = int(input("Digite a nota do motorista que deseja atualizar: "))
        nova_nota = int(input("Digite a nova nota do motorista: "))
        self.dao_motorista.atualizar_motorista(nota, nova_nota)

    def deletar_motorista(self):
        nota = int(input("Digite a nota do motorista que deseja deletar: "))
        self.dao_motorista.deletar_motorista(nota)

    def executar(self):
        print("Bem-vindo ao sistema de Motoristas!")
        super().executar()