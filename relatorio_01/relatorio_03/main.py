from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokedex = Pokedex("pokedex", "pokemons")

# Busca por pokemons dos tipos "Grass" e "Poison"
pokedex.get_pokemons_by_type(["Grass", "Poison"])

# Busca por pokemons pelo nome ou id "bulbasaur"
pokedex.get_pokemons_by_name_or_id("Bulbasaur")

# Busca por pokemons com a fraqueza "Water" e "Ground"
pokedex.get_pokemons_by_weakness(["Fire", "Ground"])

# Busca por pokemons que sejam do tipo "Grass" e que tenham a fraqueza "Fire" e "Flying"
pokedex.get_pokemons_by_type_and_weakness("Grass", ["Fire", "Flying"])

# Busca por pokemons que necessitem de 50 ou menos candies para evoluir
pokedex.get_pokemons_by_candy(50)