from teacher_crud import TeacherCRUD
from database import Database


db = Database("neo4j+s://a57719eb.databases.neo4j.io", "neo4j", "BQYOY8eviKvnAV42X2Hd6Txu8bcPbWYSdj6_7Mi3vSk")
teacher_crud = TeacherCRUD(db)

#questao 3
#b            
teacher_crud.create('Chris Lima', 1956, '189.052.396-66')
#c
teacher = teacher_crud.read('Chris Lima')
print(teacher)
#d
teacher_crud.update('Chris Lima', '162.052.777-77')
teacher = teacher_crud.read('Chris Lima')
print(teacher)
teacher_crud.delete('Chris Lima')

#e
while True:
        print("1. Create Teacher")
        print("2. Read Teacher")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. Saida")

        choice = input("Escolha uma opçao: ")

        if choice == '1':
            name = input("Entre com nome: ")
            ano_nasc = int(input("Entre com data de nascimento: "))
            cpf = input("Entre com CPF: ")
            teacher_crud.create(name, ano_nasc, cpf)
        elif choice == '2':
            name = input("Entre com nome: ")
            teacher = teacher_crud.read(name)
            if teacher:
                print(teacher)
            else:
                print("Teacher nao encontrado")
        elif choice == '3':
            name = input("Entre com nome: ")
            newCpf = input("Entre com o novo cpf")
            teacher_crud.update(name, newCpf)
        elif choice == '4':
            name = input("Entre com nome:")
            teacher_crud.delete(name)
        elif choice == '5':
            break
        else:
            print("opcao invalida")


db.close()


    