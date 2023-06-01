def contarpalavras(texto):
    caracteres = len(texto)
    palavras = texto.split()
    quantidade_palavras = len(palavras)
    return caracteres, quantidade_palavras


# Dados de Entrada
texto = input("Digite o texto: ")

# Contar caracteres e palavras
caracteres, quantidade_palavras = contarpalavras(texto)

#Main
print("Número de caracteres:", caracteres)
print("Número de palavras:", quantidade_palavras)
