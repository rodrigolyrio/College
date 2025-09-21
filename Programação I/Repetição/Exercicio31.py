def main():
    resposta = input().upper()
    while (resposta != "S" and resposta !="N"):
        print("RESPOSTA INCORRETA, DIGITE S OU N")
        resposta = input().upper()

    print("RESPOSTA CORRETA")

    return 0

if __name__ == "__main__":
    main()
