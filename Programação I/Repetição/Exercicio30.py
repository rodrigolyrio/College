def main():
    sexo = input().upper()
    while (sexo != "M" and sexo != "F"):
        print("SEXO INVÁLIDO, DIGITE F OU M")
        sexo = input().upper()

    print("SEXO VÁLIDO")

    return 0

if __name__ == "__main__":
    main()
