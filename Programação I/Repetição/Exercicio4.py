def main():
    soma = 0
    cont = 0
    resposta = input("deseja inserir um valor <s/n>: ")
    while(resposta == "s"):
        n = int(input("n: "))
        soma = soma + n
        cont = cont + 1
        resposta = input("deseja inserir um valor <s/n>: ")
    print(soma/cont)
    return 0
if __name__ == "__main__":
    main()
