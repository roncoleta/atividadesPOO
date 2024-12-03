# Classe Veiculo
class Veiculo:
    def __init__(self, placa, preco, marca, modelo):
        self.placa = placa
        self.preco = preco
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Placa: {self.placa}, Preço: R${self.preco:.2f}, Marca: {self.marca}, Modelo: {self.modelo}"

# Lista de veículos
veiculos = []

# Funções básicas
def adicionar_veiculo():
    placa = input("Placa: ")
    preco = float(input("Preço: "))
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    veiculos.append(Veiculo(placa, preco, marca, modelo))
    print("Veículo adicionado!\n")

def remover_veiculo():
    placa = input("Placa do veículo a ser removido: ")
    for veiculo in veiculos:
        if veiculo.placa == placa:
            veiculos.remove(veiculo)
            print("Veículo removido!\n")
            return
    print("Veículo não encontrado!\n")

def alterar_veiculo():
    placa = input("Placa do veículo a ser alterado: ")
    for veiculo in veiculos:
        if veiculo.placa == placa:
            veiculo.preco = float(input("Novo preço: "))
            veiculo.marca = input("Nova marca: ")
            veiculo.modelo = input("Novo modelo: ")
            print("Veículo atualizado!\n")
            return
    print("Veículo não encontrado!\n")

def listar_veiculos():
    if not veiculos:
        print("Nenhum veículo cadastrado.\n")
        return
    for veiculo in veiculos:
        print(veiculo)
    print()

# Menu
while True:
    print("1. Adicionar Veículo")
    print("2. Remover Veículo")
    print("3. Alterar Veículo")
    print("4. Listar Veículos")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_veiculo()
    elif opcao == '2':
        remover_veiculo()
    elif opcao == '3':
        alterar_veiculo()
    elif opcao == '4':
        listar_veiculos()
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")
