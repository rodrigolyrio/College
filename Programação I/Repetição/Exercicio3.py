def main():
    soma = 0 
    resposta = input("Deseja informar um valor <S/N>: ")
    while(resposta == "s"):
        n = int(input("n: "))
        soma = soma + n
        resposta = input("Deseja informar um valor <S/N>: ")
    print(soma)
    return 0 
if __name__ == "__main__":
    main()
