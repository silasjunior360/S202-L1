class Professor:
    def __init__(self,nome):
        self.nome=nome
        
    def Ministrar_aula(self,assunto):
        print( f'O professor {self.nome}  está ministrando uma aula sobre {assunto}.')
    
class Aluno:
    def __init__(self,nome):
        self.nome=nome
        
    def Presenca(self):
        print( f'O aluno {self.nome} está presente.')
    
class Aula:
    def __init__(self,professor,assunto) :
        self.professor=professor
        self.assunto=assunto
        self.alunos=[]
        
    def Adicionar_aluno(self,aluno):
        self.alunos.append(aluno)
        
    def listar_presenca(self):
        print( f'Presenca na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')  
        presencas = [aluno.Presenca() for aluno in self.alunos]      
        
professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.Adicionar_aluno(aluno1)
aula.Adicionar_aluno(aluno2)
print(aula.listar_presenca())
