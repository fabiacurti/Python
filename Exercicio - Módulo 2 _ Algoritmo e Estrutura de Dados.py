import random


class Dado:
    def initial(self):
        self.value = 0

    def lancar(self):
        self.value.random.randint(1, 6)

    def show(self):
        print("O valor é ", self.value)

dado1 = Dado()
dado2 = Dado()
repeat = "sim"

while repeat == "sim" or repeat == "s":
    dado1.lancar()
    dado2.lancar()
    soma = dado1.value+dado2.value
    dado1.show()
    dado2.show()
    print("A soma dos dados é ...", soma)
    if soma == 7 or soma == 9:
        print("Você é sortudo, ganhou!")
    elif soma == 2 or soma == 4 or soma == 12:
        print("Que azar , perdeu!")
    else:
        ponto = soma
        print("este é seu ponto", ponto)
while True:
    dado1.lancar()
    dado2.lancar()
    soma = dado1.value+dado2.value
    dado1.show()
    dado2.show()
    print("A soma dos dados é", soma)
    if soma == ponto:
        print("Você ganhou!")
        break
    elif soma == 7:
        print("Você tirou 7 e perdeu")
        break
    else:
        print("voce nao conseguiu o ponto , tente novamente")

repeat = input("Deseja jogar novamente? (sim/s ou não/n)")
