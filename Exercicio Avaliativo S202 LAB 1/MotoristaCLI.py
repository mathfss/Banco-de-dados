from UML import Motorista, Passageiro, Corrida
from MotoristaDAO import MotoristaDAO, Corrida, Passageiro
class MotoristaCLI: 
    def __init__(self, MotoristaDAO):
        self.dao = MotoristaDAO

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Criar motorista")
            print("2. Ler motorista")
            print("3. Atualizar motorista")
            print("4. Deletar motorista")
            print("5. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.criar_motorista()
            elif escolha == "2":
                self.ler_motorista()
            elif escolha == "3":
                self.atualizar_motorista()
            elif escolha == "4":
                self.deletar_motorista()
            elif escolha == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")

    def criar_motorista(self):
        nota_motorista = int(input("Digite a nota do motorista: "))
        nome_passageiro = input("Digite o nome do passageiro: ")
        documento_passageiro = input("Digite o documento do passageiro: ")
        nota_corrida = int(input("Digite a nota da corrida: "))
        distancia_corrida = float(input("Digite a distância da corrida: "))
        valor_corrida = float(input("Digite o valor da corrida: "))
        
        passageiro = Passageiro(nome_passageiro, documento_passageiro)
        corrida = Corrida(nota_corrida, distancia_corrida, valor_corrida, passageiro)
        motorista = Motorista([corrida], nota_motorista)
        
        MotoristaDAO.criar_motorista(self, motorista)

    def ler_motorista(self):
        id_motorista = input("Digite o ID do motorista: ")
        motorista = MotoristaDAO.ler_motorista(id_motorista)
        if motorista:
            print("Motorista encontrado:")
            print("Nota:", motorista.nota)
            print("Corridas:")
            for corrida in motorista.corridas:
                print("  - Nota:", corrida.nota)
                print("    Distância:", corrida.distancia)
                print("    Valor:", corrida.valor)
                print("    Passageiro:")
                print("      Nome:", corrida.passageiro.nome)
                print("      Documento:", corrida.passageiro.documento)

    def atualizar_motorista(self):
        id_motorista = input("Digite o ID do motorista que deseja atualizar: ")
        nota_motorista = int(input("Digite a nova nota do motorista: "))
        nome_passageiro = input("Digite o novo nome do passageiro: ")
        documento_passageiro = input("Digite o novo documento do passageiro: ")
        nota_corrida = int(input("Digite a nova nota da corrida: "))
        distancia_corrida = float(input("Digite a nova distância da corrida: "))
        valor_corrida = float(input("Digite o novo valor da corrida: "))
        
        passageiro = Passageiro(nome_passageiro, documento_passageiro)
        corrida = Corrida(nota_corrida, distancia_corrida, valor_corrida, passageiro)
        motorista = Motorista([corrida], nota_motorista)
        
        self.dao.atualizar_motorista(id_motorista, motorista)

    def deletar_motorista(self):
        id_motorista = input("Digite o ID do motorista que deseja deletar: ")
        self.dao.deletar_motorista(id_motorista)