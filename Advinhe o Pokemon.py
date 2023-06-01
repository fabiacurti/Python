import random

def preencher_lista_pokemon():
    lista_pokemon = ['Pikachu', 'Charizard', 'Squirtle', 'Bulbasaur', 'Jigglypuff', 'Mewtwo', 'Snorlax', 'Eevee', 'Gengar', 'Machamp','Arcanine']
    return lista_pokemon

def escolher_palavra(lista_pokemon):
    indice = random.randint(0, len(lista_pokemon) - 1)
    return indice

def embaralhar_palavra(palavra):
    letras = list(palavra)
    random.shuffle(letras)
    palavra_embaralhada = ''.join(letras)
    return palavra_embaralhada

def jogar(palavra_correta):
    tentativas = 7
    while tentativas > 0:
        print("Palavra embaralhada:", embaralhar_palavra(palavra_correta))
        print("Tentativas restantes:", tentativas)
        palpite = input("Digite seu palpite: ")
        if palpite.lower() == palavra_correta.lower():
            return True
        else:
            tentativas -= 1
            print("Palpite incorreto!")
    
    return False

def jogo_palavra_embaralhada():
    lista_pokemon = preencher_lista_pokemon()
    indice_pokemon = escolher_palavra(lista_pokemon)
    pokemon_escolhido = lista_pokemon[indice_pokemon]

    print("Jogo da Palavra Embaralhada")
    print("Adivinhe o nome do Pokémon!")
    print()

    resultado = jogar(pokemon_escolhido)

    print()
    print("O Pokémon correto era:", pokemon_escolhido)
    if resultado:
        print("Parabéns, você ganhou!")
    else:
        print("Que pena, você perdeu!")

jogo_palavra_embaralhada()
