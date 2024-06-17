from uml.Corrida import Corrida
from uml.Passageiro import Passageiro
from CLI.cli import SimpleCLI

class CorridaCLI(SimpleCLI):
    def __init__(self, corrida_dao):
        super().__init__()
        self.corrida_dao = corrida_dao
        self.add_command("criar", self.criar_corrida)
        self.add_command("ler", self.ler_corrida)
        self.add_command("atualizar", self.atualizar_corrida)
        self.add_command("deletar", self.deletar_corrida)

    def criar_corrida(self):
        nota = float(input("Digite a nota da corrida: "))
        distancia = float(input("Digite a distância percorrida: "))
        valor = float(input("Digite o valor da corrida: "))
        nome_passageiro = input("Digite o nome do passageiro: ")
        documento_passageiro = input("Digite o documento do passageiro: ")
        passageiro = Passageiro(nome_passageiro, documento_passageiro)
        corrida = Corrida(nota, distancia, valor, passageiro)
        self.corrida_dao.criar_corrida(corrida)
        print("Corrida criada com sucesso!")

    def ler_corrida(self):
        nota = float(input("Digite a nota da corrida que deseja ler: "))
        corrida = self.corrida_dao.ler_corrida(nota)
        if corrida:
            print(f"Nota: {corrida.nota}")
            print(f"Distância: {corrida.distancia}")
            print(f"Valor: {corrida.valor}")
            print(f"Passageiro: {corrida.passageiro.nome} - {corrida.passageiro.documento}")

    def atualizar_corrida(self):
        nota = float(input("Digite a nota da corrida que deseja atualizar: "))
        nova_nota = float(input("Digite a nova nota da corrida: "))
        nova_distancia = float(input("Digite a nova distância percorrida: "))
        novo_valor = float(input("Digite o novo valor da corrida: "))
        self.corrida_dao.atualizar_corrida(nota, nova_nota, nova_distancia, novo_valor)

    def deletar_corrida(self):
        nota = float(input("Digite a nota da corrida que deseja deletar: "))
        self.corrida_dao.deletar_corrida(nota)

    def executar(self):
        print("Bem-vindo ao sistema de Corridas!")
        print("Comandos disponíveis: criar, ler, atualizar, deletar, sair")
        super().executar()
