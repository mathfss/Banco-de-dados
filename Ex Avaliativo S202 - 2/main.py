import sys
from teacher_crud import TeacherCRUD, Database

class TeacherCLI:
    def __init__(self):
        self.db = Database("bolt://localhost:7687", "mathfs", "12345")
        self.crud = TeacherCRUD(self.db)

    def criar_professor(self):
        nome = input("Digite o nome do professor: ")
        ano_nasc = int(input("Digite o ano de nascimento do professor: "))
        cpf = input("Digite o CPF do professor: ")
        self.crud.create(nome, ano_nasc, cpf)
        print(f"Professor {nome} criado com sucesso!")

    def ler_professor(self):
        nome = input("Digite o nome do professor para buscar: ")
        professor = self.crud.read(nome)
        if professor:
            print(f"Professor encontrado: {professor}")
        else:
            print("Professor não encontrado.")

    def atualizar_professor(self):
        nome = input("Digite o nome do professor para atualizar: ")
        novo_cpf = input("Digite o novo CPF: ")
        self.crud.update(nome, novo_cpf)
        print(f"Professor {nome} atualizado com sucesso!")

    def deletar_professor(self):
        nome = input("Digite o nome do professor para deletar: ")
        self.crud.delete(nome)
        print(f"Professor {nome} deletado com sucesso!")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Criar Professor")
            print("2. Ler Professor")
            print("3. Atualizar Professor")
            print("4. Deletar Professor")
            print("5. Sair")
            escolha = input("Digite sua escolha: ")

            if escolha == '1':
                self.criar_professor()
            elif escolha == '2':
                self.ler_professor()
            elif escolha == '3':
                self.atualizar_professor()
            elif escolha == '4':
                self.deletar_professor()
            elif escolha == '5':
                self.db.close()
                sys.exit()
            else:
                print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    cli = TeacherCLI()
    cli.run()