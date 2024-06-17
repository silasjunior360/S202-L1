from uml.Passageiro import Passageiro
from CLI.cli import SimpleCLI

class PassageiroCLI(SimpleCLI):
    def __init__(self, passageiro_dao):
        super().__init__()
        self.passageiro_dao = passageiro_dao
        
        self.add_command("criar", self.criar_passageiro)
        self.add_command("ler", self.ler_passageiro)
        self.add_command("atualizar", self.atualizar_passageiro)
        self.add_command("deletar", self.deletar_passageiro)

    def criar_passageiro(self):
        nome = input("Digite o nome do passageiro: ")
        documento = input("Digite o documento do passageiro: ")
        passageiro = Passageiro(nome, documento)
        self.passageiro_dao.criar_passageiro(passageiro)

    def ler_passageiro(self):
        documento = input("Digite o documento do passageiro que deseja ler: ")
        passageiro = self.passageiro_dao.ler_passageiro(documento)
        if passageiro:
            print(f"Nome: {passageiro.nome}")
            print(f"Documento: {passageiro.documento}")

    def atualizar_passageiro(self):
        documento = input("Digite o documento do passageiro que deseja atualizar: ")
        novo_documento = input("Digite o novo documento do passageiro: ")
        self.passageiro_dao.atualizar_passageiro(documento, novo_documento)

    def deletar_passageiro(self):
        documento = input("Digite o documento do passageiro que deseja deletar: ")
        self.passageiro_dao.deletar_passageiro(documento)

    def executar(self):
        print("Bem-vindo ao sistema de Passageiros!")
        super().executar()
