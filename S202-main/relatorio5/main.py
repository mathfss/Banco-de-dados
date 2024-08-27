from database import Database
from personModel import PersonModel

db = Database(database="relatorio_5", collection="pessoas")
personModel = PersonModel(database=db)

# 1- Create
#personModel.create_person("Francisco", 20)

# 2- Read
#personModel.read_person_by_id("65f8abf7bcf6648c681243c1")

# 3- Update
#personModel.update_person("65f8abf7bcf6648c681243c1", "Francisco", "20")

# 4- Delete
personModel.delete_person("65f8abf7bcf6648c681243c1")