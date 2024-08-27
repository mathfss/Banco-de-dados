from UML import Motorista, Passageiro, Corrida

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def criar_motorista(self, motorista):
        motorista_dict = {
            "nota": motorista.nota,
            "corridas": [
                {
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                } for corrida in motorista.corridas
            ]
        }
        result = self.db.collection.insert_one(motorista_dict)
        print("Motorista criado com ID:", result.inserted_id)

    def ler_motorista(self, id_motorista):
        motorista_dict = self.db.collection.find_one({"_id": id_motorista})
        if motorista_dict:
            motorista = self._doc_para_motorista(motorista_dict)
            return motorista
        else:
            print("Motorista não encontrado")

    def atualizar_motorista(self, id_motorista, novo_motorista):
        motorista_dict = {
            "nota": novo_motorista.nota,
            "corridas": [
                {
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                } for corrida in novo_motorista.corridas
            ]
        }
        result = self.db.collection.update_one({"_id": id_motorista}, {"$set": motorista_dict})
        if result.modified_count > 0:
            print("Motorista atualizado com sucesso")
        else:
            print("Nenhum motorista foi atualizado")

    def deletar_motorista(self, id_motorista):
        result = self.db.collection.delete_one({"_id": id_motorista})
        if result.deleted_count > 0:
            print("Motorista deletado com sucesso")
        else:
            print("Nenhum motorista foi deletado")

    def _doc_para_motorista(self, doc):
        corridas = []
        for corrida_dict in doc["corridas"]:
            passageiro_dict = corrida_dict["passageiro"]
            passageiro = Passageiro(passageiro_dict["nome"], passageiro_dict["documento"])
            corrida = Corrida(corrida_dict["nota"], corrida_dict["distancia"], corrida_dict["valor"], passageiro)
            corridas.append(corrida)
        motorista = Motorista(corridas, doc["nota"])
        return motorista