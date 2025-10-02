from random import randrange
def main():
    cont = 1

    jogada = int(input())
    print(jogada)

    if (jogada == 7 or jogada == 11):
        print("NATURAL!VOCÊ GANHOU")
        print(f"JOGADAS = {cont}")
    elif (jogada == 2 or jogada == 3 or jogada == 12):
        print("CRAPS!VOCÊ PERDEU")
        print(f"JOGADAS = {cont}")
    else:
        ponto = jogada

        jogada = int(input())
        cont += 1
        while (ponto != jogada and jogada != 7):
            print(jogada)

            jogada = int(input())
            cont += 1
        print(jogada)
        if (jogada == ponto):
            print("VOCÊ GANHOU")
            print(f"JOGADAS = {cont}")
        elif (jogada == 7):
            print("VOCÊ PERDEU")
            print(f"JOGADAS = {cont}")

    return 0

if __name__ == "__main__":
    main()
