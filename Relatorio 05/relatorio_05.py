from pymongo import MongoClient
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database

    def adicionar_livro(self, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.Livros.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Livro adicionado com o id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao adicionar o livro: {e}")
            return None

    def listar_livros(self):
        try:
            livros = list(self.db.Livros.find())
            print("Lista de Livros:")
            for livro in livros:
                print(livro)
            return livros
        except Exception as e:
            print(f"Ocorreu um erro ao listar os livros: {e}")
            return None

    def buscar_livro_por_id(self, id: str):
        try:
            res = self.db.Livros.find_one({"_id": ObjectId(id)})
            if res:
                print(f"Livro encontrado: {res}")
            else:
                print("Livro não encontrado.")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o livro: {e}")
            return None

    def atualizar_livro(self, id: str, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.Livros.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            print(f"Livro atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def deletar_livro_por_id(self, id: str):
        try:
            res = self.db.Livros.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o livro: {e}")
            return None

def main():
    try:
        client = MongoClient("localhost", 27017)
        db = client["Relatorio05"]
        livro_model = LivroModel(db)

        while True:
            print("\n===== Menu Livros =====")
            print("1. Adicionar Livro")
            print("2. Listar os Livros")
            print("3. Buscar Livro por ID")
            print("4. Atualizar Livro")
            print("5. Deletar Livro por ID")
            print("6. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                ano = int(input("Digite o ano do livro: "))
                preco = float(input("Digite o preço do livro: "))
                livro_model.adicionar_livro(titulo, autor, ano, preco)
            elif escolha == "2":
                livro_model.listar_livros()
            elif escolha == "3":
                id = input("Digite o ID do livro a ser buscado: ")
                livro_model.buscar_livro_por_id(id)
            elif escolha == "4":
                id = input("Digite o ID do livro a ser atualizado: ")
                titulo = input("Digite o novo título do livro: ")
                autor = input("Digite o novo autor do livro: ")
                ano = int(input("Digite o novo ano do livro: "))
                preco = float(input("Digite o novo preço do livro: "))
                livro_model.atualizar_livro(id, titulo, autor, ano, preco)
            elif escolha == "5":
                id = input("Digite o ID do livro a ser deletado: ")
                livro_model.deletar_livro_por_id(id)
            elif escolha == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
