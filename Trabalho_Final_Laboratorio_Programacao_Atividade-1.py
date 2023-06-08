import random

lin = int(input("Informe o número de linhas: "))
col = int(input("Informe o número de colunas: "))
pares = []
impares = []


def gerar_matriz(lin, col):
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            linha.append(random.randrange(0, 100))
        matriz.append(linha)
    return matriz


def pares_impares(matriz):
    for linha in matriz:
        for number in linha:
            if number % 2 == 0:
                pares.append(number)
            else:
                impares.append(number)
    return pares, impares


matriz = gerar_matriz(lin, col)
pares, impares = pares_impares(matriz)

print("Números pares:", pares)
print("Números ímpares:", impares)
