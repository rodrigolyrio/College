def main():
    i = 0
    soma = 0
    while (i < 5):
        n = int(input("valor: "))
        soma = soma + n
        i = i + 1
    print(soma/i)
    soma = 0
    return 0
if __name__ == "__main__":
    main()
