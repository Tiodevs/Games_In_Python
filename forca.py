import random

def jogar():

    #escolhendo uma palavra aleatoria
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    #mostra quantas letras foram acertadas e deixa as restantes em "_"
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)


    enforcou = False
    acertou  = False
    erros    = 0


    while(not enforcou and not acertou):

        #pedir chute
        chute = input("Qual letra?")
        chute = chute.strip().upper()

        #confere se chute esta correto
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index +1
        #caso erre acresenta mais um erro
        else:
            erros = erros +1

        #se errar 6 vez perde
        enforcou = erros == 6

        #se nao tiver _ na palavra secre vc ganhou
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        #mensagem de vitoria e derrota
        if(acertou):
            print("voce ganhou")
        else:
            if(enforcou):
                print("voce perdeu")
    print("fim do jogo")

def imprime_mensagem_abertura():
    print("***************************")
    print("BEM VINDOS DO JOGO  DA FORCA!")
    print("****************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()