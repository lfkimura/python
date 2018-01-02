import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
pontos =1000
numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))
if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas+1) :
    print("tentativa {} de {}".format(rodada,total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute< numero_secreto
    if(acertou):
        print("Voce acertou!")

        print("Você acertou e fez {} pontos!".format(pontos))
        break
    elif(maior):
        print("o numero é menor")
    elif(menor) :
        print("o numero eh maior")
    pontos_perditos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perditos
    rodada = rodada +1
print("Fim do jogo")