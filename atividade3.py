#classes
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
#Método para exibir as informações
    def exibir_detalhes(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"


class Calcado(Produto):
    def __init__(self, nome, preco, tamanho, material):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        self.material = material
#Método para exibir as informações
    def exibir_detalhes(self):
        detalhes_base = super().exibir_detalhes()
        return f"{detalhes_base}, Tamanho: {self.tamanho}, Material: {self.material}"


class Roupa(Produto):
    def __init__(self, nome, preco, tamanho, tecido):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        self.tecido = tecido
#Método para exibir as informações
    def exibir_detalhes(self):
        detalhes_base = super().exibir_detalhes()
        return f"{detalhes_base}, Tamanho: {self.tamanho}, Tecido: {self.tecido}"

#Corpo do código
sapato = Calcado("Sapato Social", 150.0, 42, "Couro")
camisa = Roupa("Camisa Polo", 80.0, "M", "Algodão")

#Exibição dos resultados
print(sapato.exibir_detalhes())
print(camisa.exibir_detalhes())
