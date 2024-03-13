from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database):
        self.database = database

    def fun1(self,tipos):
        self.tipos=tipos
        pokemons= self.database.collection.find({"type":{"$in": tipos}, "next_evolution": {"$exists": True} })
        writeAJson (pokemons,"tipos fogo")
        print(f'Foi adicionado os pokemons que tem evoluçao do tipo {self.tipos} no Log')
        
    def fun2(self,tipos):
        self.tipos=tipos
        pokemons = self.database.collection.find({"weaknesses": {"$all":tipos}})
        writeAJson (pokemons,"Fraquezas")
        print(f'Foi adicionado os pokemons que tem fraqueza contra o tipo {self.tipos} no Log')
        

    def fun3(self, pokemon_id):
        self.pokemon_id=pokemon_id
        pokemons = self.database.collection.find({"id": pokemon_id})
        writeAJson(pokemons,"id pokemon")
        print(f'Foi adicionado o pokemon com id {self.pokemon_id} no Log')
        

    def fun4(self, pokemon_name):
        self.pokemon_name=pokemon_name
        pokemons = self.database.collection.find({"name": pokemon_name})
        writeAJson(pokemons,"pokemon name")
        print(f'Foi adicionado o pokemon com nome {self.pokemon_name} no Log')
        

    def fun5(self,egg):
        self.egg=egg
        pokemons = self.database.collection.find_one({"egg": egg})
        writeAJson (pokemons,"eggs")
        print(f'Foi adicionado os pokemons que tem ovos de {self.egg} no Log')
        
