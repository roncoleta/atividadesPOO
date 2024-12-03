# Inicializar a lista de salários
salarios = []

# Entrada de dados
print("Digite os salários dos trabalhadores (ou 0 para encerrar):")
while True:
    salario = float(input("Salário: "))
    if salario == 0:
        break
    salarios.append(salario)

#a)Calcular a média dos salários
if salarios: 
    media_salarios = sum(salarios) / len(salarios)
    print(f"Média dos salários: R${media_salarios:.2f}")
else:
    print("Nenhum salário foi informado.")

#b)Determinar o maior salário
if salarios:
    maior_salario = max(salarios)
    print(f"Maior salário: R${maior_salario:.2f}")

#c)Contar salários menores que R$850,00
salarios_menores_850 = len([s for s in salarios if s < 850.00])
print(f"Quantidade de salários menores que R$850,00: {salarios_menores_850}")
