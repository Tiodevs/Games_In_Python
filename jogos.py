import forca
import adivinhacao

def escolhe_jogo():
    print("***************************")
    print("BEM VINDOS ESCOLHA SEU JOGO!")
    print("****************************")

    print("(1)jogo forca (2)jodo da adivinhação")

    jogo = int(input("escolha um jogo: "))

    if (jogo == 1):
        print("jogo da forca")
        forca.jogar()
    elif (jogo == 2):
        print("jogo da adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
