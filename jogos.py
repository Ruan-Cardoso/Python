import forca
import adivinhacao

print("escolha o seu jogo")

print("(1) forca (2) Adivinhação")
jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando advinhacao")
    adivinhacao.jogar()
