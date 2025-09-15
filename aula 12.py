# Solicita o nome do motorista
nome = input("Digite o nome do motorista: ")

# Solicita a velocidade registrada
velocidade = float(input("Digite a velocidade registrada (km/h): "))

# Define o limite de velocidade
limite = 80

# Classifica a velocidade
if velocidade <= limite:
    classificacao = "Dentro do limite"
elif 81 <= velocidade <= 100:
    classificacao = "Acima do limite (leve)"
else:
    classificacao = "Acima do limite (grave)"

# Mostra o resultado
print(f"\nMotorista: {nome}")
print(f"Velocidade registrada: {velocidade:.1f} km/h")
print(f"Classificação: {classificacao}")