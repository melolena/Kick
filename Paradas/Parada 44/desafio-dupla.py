# Inicializações
numeros = []
soma = 0
# inf = infinito, menor e maior valor negativo infinito
maior = float('-inf')
menor = float('inf')
positivos = 0
negativos = 0

# Leitura dos números
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    soma += numero
    
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Cálculo da média
media = soma / 10

# Exibição dos resultados
print("Média dos elementos:", media)
print("Maior elemento:", maior)
print("Menor elemento:", menor)
print("Quantidade de elementos positivos:", positivos)
print("Quantidade de elementos negativos:", negativos)
