# Inicializar listas para armazenar os dados
nomes = []
sexos = []
salarios = []

# Entrada de dados
print("Digite os dados dos trabalhadores (ou deixe o nome vazio para encerrar):")
while True:
    nome = input("Nome: ").strip()
    if nome == "":
        break
    sexo = input("Sexo (M/F): ").strip().upper()
    salario = float(input("Salário: "))
    
    # Armazenar os dados
    nomes.append(nome)
    sexos.append(sexo)
    salarios.append(salario)

#a)Calcular e visualizar a média dos salários das mulheres
salarios_mulheres = [salarios[i] for i in range(len(sexos)) if sexos[i] == 'F']
if salarios_mulheres: 
    media_salarios_mulheres = sum(salarios_mulheres) / len(salarios_mulheres)
    print(f"Média dos salários das mulheres: R${media_salarios_mulheres:.2f}")
else:
    print("Não há mulheres cadastradas na empresa.")

#b)Determinar o menor salário e visualizar os dados do trabalhador
if salarios:
    menor_salario = min(salarios)
    indice_menor = salarios.index(menor_salario)
    print("\nTrabalhador com o menor salário:")
    print(f"Nome: {nomes[indice_menor]}")
    print(f"Sexo: {sexos[indice_menor]}")
    print(f"Salário: R${menor_salario:.2f}")
else:
    print("Não há trabalhadores cadastrados na empresa.")

#c)Contar os homens que ganham mais de R$1.500,00
homens_maiores_1500 = len([salarios[i] for i in range(len(sexos)) if sexos[i] == 'M' and salarios[i] > 1500])
print(f"\nQuantidade de homens que ganham mais de R$1.500,00: {homens_maiores_1500}")
