def main():
    idade = int(input('idade: '))
    anos = idade // 365
    resto = idade % 365
    meses = resto // 30
    dias = resto % 30
    print(anos,meses,dias)
    
    return 0
if __name__ == "__main__":
    main()
