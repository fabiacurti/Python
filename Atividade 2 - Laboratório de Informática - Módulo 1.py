import random

class GerarMatriz:
    def main(self, coluna, linha):
        matriz = self.gerar_matriz_aleatoria(coluna, linha)  
        par, impar = self.separar_par_impar(matriz)
        print("Matriz de retorno:", matriz)
        print("Os números pares são:", par)
        print("Os números ímpares são:", impar)
    
    def gerar_matriz_aleatoria(self, num_colunas, num_linhas):  
        matriz = []
        for _ in range(num_linhas):
            linha = []
            for _ in range(num_colunas):
                elemento = random.randint(0, 100)
                linha.append(elemento)
            matriz.append(linha)
        return matriz
    
    def separar_par_impar(self, matriz):
        elementos_pares = []
        elementos_impares = []

        for linha in matriz:
            for elemento in linha:
                if elemento % 2 == 0:
                    elementos_pares.append(elemento)
                else:
                    elementos_impares.append(elemento)

        return elementos_pares, elementos_impares

objeto = GerarMatriz()

lin = int(input("Digite o número de linhas: "))
col = int(input("Digite o número de colunas: "))
objeto.main(col, lin)
