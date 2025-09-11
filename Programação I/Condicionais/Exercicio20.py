def main():
    
    opcao = int(input(""))
    valor1 = int(input(""))
    valor2 = int(input(""))
    
    resultado = 0
    
    if opcao == 1:
        resultado = valor1 + valor2
    elif opcao == 2:
        resultado = valor1 - valor2
    elif opcao == 3:
        resultado = valor1 * valor2
    elif opcao == 4:
        resultado = valor1 / valor2
    elif opcao == 5:
        resultado = valor1 ** valor2
    elif opcao == 6:
        resultado = valor1 ** (1 / valor2)
    else:
        print("OPERACAO INVALIDA")
    
    if opcao >= 1 and opcao <= 6:
        print(resultado)
        
    return 0
if __name__ == "__main__":
    main()
