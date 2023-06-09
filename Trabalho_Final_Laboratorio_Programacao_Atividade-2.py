text = input("Digite uma palavra  ")


def repeat(text):
    letras_repetidas = set()

    for letra in text:
        if letra in letras_repetidas:
            return True
        letras_repetidas.add(letra)
    return False


resultado = repeat(text)
##teste
testeTrue= repeat("fabia")
testeFalse=repeat("aeiou")

print("A palavra que voce escolheu retornou ", resultado)
##retorno do teste 
print("o teste false resultou em : ", testeFalse)
print("o teste true resultou em : ", testeTrue)
