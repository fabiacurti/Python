
    # lista de conectores à serem retirados
conectores = ["e", "do", "da", "dos", "das", "de", "di", "du"]


def digiteNome(nome):
    palavras = nome.split()
    iniciais = ""
    # percorrer lista de palavras
    for palavra in palavras:
        if palavra.lower() not in conectores:
            iniciais += palavra[0].upper()

    return iniciais


# Main
nome_completo = input("Digite o nome completo: ")

iniciais = digiteNome(nome_completo)

print("As iniciais do nome são:", iniciais)
