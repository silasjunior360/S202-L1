from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex


db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

poke = Pokedex(db)
type = ["Fire"]
# Normal = ["Normal"]
# Fire = ["Fire"]
# Water = ["Water"]
# Grass = ["Grass"]
# Electric = ["Electric"]
# Ice = ["Ice"]
# Fighting = ["Fighting"]
# Poison = ["Poison"]
# Ground = ["Ground"]
# Flying = ["Flying"]
# Psychic = ["Psychic"]
# Bug = ["Bug"]
# Rock = ["Rock"]
# Ghost = ["Ghost"]
# Dark = ["Dark"]
# Steel = ["Steel"]
# Dragon = ["Dragon"]
# Fairy = ["Fairy"]
# tipos_pokemon = [
#     Normal, Fire, Water, Grass, Electric, Ice, Fighting, Poison,
#     Ground, Flying, Psychic, Bug, Rock, Ghost, Dark, Steel, Dragon, Fairy
# ]



print(f"1: Pokemons que tem evoluçao que sao do tipo FIRE:")
print(f"2: Fraqueza dos tipo Fire:")
print(f"3: busca po id do pokemon")
print(f"4: busca por nome do pokemon")
print(f"5: ovos por km")
    
opcao = int(input("Digite a opção desejada (1 a 5): "))
if opcao==1:
    # print(f"Escolha um tipo:")
    # for i, tipo in enumerate(tipos_pokemon, start=1):
    #     print(f"{i}-{tipo[0]}")
    # type=int(input ("Digite o numero do tipo:") )
    # for i, tipo in enumerate(tipos_pokemon, start=1):
    #     if i==type:        
    #         print(f"Tipo selecionado: {tipo[0]}")   
    #         poke.fun1(tipo[0])
    tipo= poke.fun1(type)
if opcao ==2:
    #Fraqueza=input("Digite o tipo:")
    fraqueza = poke.fun2(type)
if opcao==3:
    id= int(input("Digite o id:"))
    poke.fun3(id)     
if opcao==4:
    nome=input("Digite o nome:")
    poke.fun4(nome)
if opcao==5:
    egg=input("Digite numero e km:")
    poke.fun5(egg)          

