def main():
    anos = int(input("anos: "))
    meses = int(input("meses: "))
    dias = int(input("dias: "))
    idade = ((anos*365) + (meses*30) + dias)
    print(idade)
    return 0
if __name__ == "__main__":
    main()
