estudantes = {
    "jose": [10, 5, 2, 3, 4],
    "pedro": [3, 6, 9, 2],
    "suzana": [8, 2, 7, 4, 3, 7, 4, 1, 2, 9, 1, 7],
    "gisela": [2, 8, 2, 10, 6, 7],
    "joao": [4, 3, 5, 7, 6]
}

# Abrir o arquivo
with open("estudantes.txt", "w") as arquivo:
    for estudante, notas in estudantes.items():
        linha = f"{estudante}: {', '.join(str(nota) for nota in notas)}\n"
        arquivo.write(linha)

# Leitura do arquivo e criação do dicionário
estudantes = {}
filtroCinco = []
medias = []
nota10 = []

with open("estudantes.txt", "r") as arquivo:
    for linha in arquivo:
        estudante, notas_str = linha.strip().split(": ")
        notas = [int(nota) for nota in notas_str.split(", ")]
        estudantes[estudante] = notas
####################### Métodos ###############################

# Método que imprime estudantes com menos de 5 notas


def menorCinco(estudantes, filtroCinco):
    for estudante, notas in estudantes.items():
        if len(notas) < 5:
            filtroCinco.append(estudante)
            print(
                f"O estudante que possui menos de 5 notas lançadas é o: {estudante}")


# Método que calcula a média de cada estudante
def calculaMedia(estudantes):
    for estudante, notas in estudantes.items():
        media = sum(notas) / len(notas)
        medias.append((estudante, media))
        print(f"Média de {estudante}: {media:.2f}")

# método que calcula as maiores notas e menores notas dos estudantes


def calcular_notas(estudantes):
    for estudante, notas in estudantes.items():
        nota_maior = max(notas)
        nota_menor = min(notas)
        print(f"Notas de {estudante}:")
        print(f"Nota maior: {nota_maior}")
        print(f"Nota menor: {nota_menor}")
        print()
# procura o estudante que tirou 10


def dezNota(estudantes):
    for estudante, notas in estudantes.items():
        if 10 in notas:
            nota10 = notas.append((estudante, notas))
            print(f"O estudante que tirou nota 10 foi: {estudante}")

#


# programa principal
calculaMedia(estudantes)
menorCinco(estudantes, filtroCinco)
calcular_notas(estudantes)
dezNota(estudantes)
