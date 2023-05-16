import random

class GerarMatriz:
    # Método Geral
    def metodo_geral(self):
        lin = int(input("Digite o número de linhas: "))
        col = int(input("Digite o número de colunas: "))
        matriz = self.gerar_matriz_aleatoria(lin, col)
        print(matriz)
        percentual_par, percentual_impar = self.gerar_percentual(matriz)
        print("A porcentagem de números pares é de", percentual_par, "% e, de números ímpares é de", percentual_impar, "%.")

    # Método que recebe os valores e cria uma matriz
    def gerar_matriz_aleatoria(self, linhas, colunas):
        matriz = []
        for _ in range(linhas):
            linha = []
            for _ in range(colunas):
                elemento = random.randint(0, 100)
                linha.append(elemento)
            matriz.append(linha)
        return matriz

    # Gerar percentual de pares e ímpares
    def gerar_percentual(self, matriz):
        numero_elementos = 0
        contador_par = 0
        contador_impar = 0

        for linha in matriz:
            for elemento in linha:
                numero_elementos += 1
                if elemento % 2 == 0:
                    contador_par += 1
                else:
                    contador_impar += 1

        percen_par = (contador_par / numero_elementos) * 100
        percen_impar = (contador_impar / numero_elementos) * 100
        return percen_par, percen_impar

# Criar uma instância da classe
objeto = GerarMatriz()

# Chamar o método
objeto.metodo_geral()
