import random

def jogar():
    print("bem vindo ao jogo do mane")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos  = 1000

    print("qual nivel de dificuldade", numero_secreto )
    print("(1) facil (2) Médio (3) Difícil  ")
    nivel = int(input("Defina o nível"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for  rodada in range(1, total_de_tentativas + 1) :
        # interpolacao de string
        print("tentativa {} de {}".format(rodada,total_de_tentativas) )
        chute_srt = input("digite um número")
        chute = int(chute_srt)
        if(chute < 1 or chute > 100):
            print("Somente números de 1 a 100")
            continue
        acertou = numero_secreto == chute
        errou_para_maior = chute > numero_secreto
        errou_para_menor = chute < numero_secreto



        if (acertou):
            print("voce acertou e fez {} pontos!".format(pontos))
            pontos_ganhos = chute
            pontos = pontos + pontos_ganhos
            break
        else:
            if   (errou_para_maior):
                print("voce errou, número maior que numreo secreto")
            elif (errou_para_menor):
                print("voce errou, número menor que numreo secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        # total_de_tentativas = total_de_tentativas - 1
        rodada = rodada + 1

    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()
