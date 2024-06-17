from uml.Motorista import Motorista
from uml.Corrida import Corrida
from uml.Passageiro import Passageiro
from CLI.cli import SimpleCLI

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao, passageiro_dao, corrida_dao):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.passageiro_dao = passageiro_dao
        self.corrida_dao = corrida_dao
        self.add_command("criar", self.criar_motorista)
        self.add_command("ler", self.ler_motorista)
        self.add_command("atualizar", self.atualizar_motorista)
        self.add_command("deletar", self.deletar_motorista)

    def criar_motorista(self):
        nome = input("Digite o nome do motorista: ")
        corridas = float(input("Digite numero de corrida: "))
        while True:
            nota_corrida = float(input("Digite a nota da corrida: "))
            distancia_corrida = float(input("Digite a distância da corrida: "))
            valor_corrida = float(input("Digite o valor da corrida: "))
            
            nome_passageiro = input("Digite o nome do passageiro: ")
            documento_passageiro = input("Digite o documento do passageiro: ")
           
           
            
            opcao = input("Deseja adicionar outra corrida? (s/n): ")
            if opcao.lower() != 's':
                break
        nota_motorista = float(input("Digite a nota do motorista: "))
        # Crie o objeto Motorista e corrida
        corrida = Corrida(nota_corrida, distancia_corrida, valor_corrida, Passageiro(nome_passageiro, documento_passageiro))
        motorista = Motorista(nome, corridas, nota_motorista)
        
        # Chame o método do DAO para criar o motorista
        self.corrida_dao.criar_corrida(corrida)
        
        self.motorista_dao.criar_motorista(motorista)
        
        

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