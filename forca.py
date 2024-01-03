
#find retorna o index de um array

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for simbulo in palavra_secreta]
                             # list Comprehension


    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        tentativas = 6

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            tentativas = tentativas - erros
            print("Vôce errou seu número de tentativas é {}".format(tentativas))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("voçê ganhou ")
    else:
        print("voçê perdeu!!")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()