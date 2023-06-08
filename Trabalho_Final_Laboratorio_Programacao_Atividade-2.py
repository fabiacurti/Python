text = input("Digite uma palavra  ")


def repeat(text):
    letras_repetidas = set()

    for letra in text:
        if letra in letras_repetidas:
            return True            
        letras_repetidas.add(letra)
    return False

resultado = repeat(text)
print(resultado) 
