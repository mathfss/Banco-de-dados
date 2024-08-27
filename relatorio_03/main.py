from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

tipos = ["Grass", "Poison"]
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })

writeAJson(pokemons, "poison or grass pokemon")

pokemons = db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Fire"}]})

writeAJson(pokemons, "fogo ou fraco contra fogo")

fraquezas = ["Psychic", "Ice"]
pokemons = db.collection.find({"weaknesses": {"$all": fraquezas}})

writeAJson(pokemons, "weaknesses Psychic or Ice")

pokemons = db.collection.find({"weaknesses": {"$size": 1}})

writeAJson(pokemons, "uma fraqueza")

pokemons = db.collection.find({"multipliers": {"$exists": False}})

writeAJson(pokemons, "sem o campo multipliers")