import random

#importado para "jogos"
def jogar():
    print("***************************")
    print("BEM VINDOS AO JOGO DA ADIVINHÇÃO!")
    print("****************************")

    #declaranto o numero, pontose tentativas.
    pontos = 1000
    numero_de_sorteio = round(random.randrange(1, 101))
    total_de_tentatiuvas = 0
    rodadas = 1

    #painel de escolha de nivel
    print("qual nivel voce deseja?")
    print("(1)iniciante (2)medio (3)dificil")
    nivel = int(input("escolha um nivel:"))

    #declarando tentativas para cada dificuldade
    if (nivel == 1):
        total_de_tentatiuvas = 20
    elif (nivel == 2):
        total_de_tentatiuvas = 10
    else:
        if(nivel == 3):
            total_de_tentatiuvas = 5

    #enquanto tiver rodadas o while roda o jogo
    while (rodadas <= total_de_tentatiuvas):

        #painel de escolha de numero
        print("voce tem", total_de_tentatiuvas, "rodadas, essa e sua", rodadas, "tentativa")
        chute = input("digite seu numero de 1 a 100: ")

        #tranforma a str do chute em numero
        chute = int(chute)

        #para testar repido:
        if (chute == 0):
            print(f"voce acertou e fez {pontos}")
            break
        #caso o jogador escolha um numero fora da zona do chute
        if(chute < 0 or chute > 100):
            print("escolha um numero de 1 a 100!")
            continue

        #condiçoes para acertar e mostrar o quão perto está
        acertou = chute == numero_de_sorteio
        maior   = chute >  numero_de_sorteio
        menor   = chute <  numero_de_sorteio

        if (acertou):
            print(f"voce acertou e fez {pontos}")
            break
        else:
            if (maior):
                print("tente um numero menor")
                print("****************************")
            if (menor):
                print("tente um numero maior")
                print("****************************")

        #soma dos pontos perdidos
        pontos_perdidos = abs(numero_de_sorteio - chute)
        pontos = pontos - pontos_perdidos

        #adicionar 1 ponto no contador de rodadas
        rodadas = rodadas +1
    print(f"voce fez {pontos} e o numero era: ", numero_de_sorteio)

if(__name__ == "__main__"):
    jogar()