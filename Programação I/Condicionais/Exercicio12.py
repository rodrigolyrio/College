def main():
    valor1 = int(input(""))
    valor2 = int(input(""))
    valor3 = int(input(""))
    
    if (valor1 > valor2 and valor1 > valor3):
        maior = valor1
    elif (valor2 > valor1 and valor2 > valor3):
        maior = valor2
    else:
        maior = valor3
    
    print(maior)
    
    return 0
if __name__ == "__main__":
    main()
