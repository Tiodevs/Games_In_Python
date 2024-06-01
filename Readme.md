# Projeto da faculdade para colocar em pratica o que estou aprendendo sobre Python
## É uma junção de dois jogos para Terminal

Assim que o codigo é executado aparece um menu onde você pode escolher entre duas alternativas:

[+] 1 - jogo da forca.                                                                     
[+] 2 - jogo de adivinhação.

Depois da escolha começa os respectivos jogos...

## Para fazer isso eu tive que fazer uma logica em tres etapas:

1 - Importar os dois jogos em arquivos .py separados

2 - Fazer um imput e tranformar em int

3 - Executar o jogo de acordo com o input usando if e elif


``` Python
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
```
