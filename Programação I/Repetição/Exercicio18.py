def main():
    
    soma = 0
    numerador1 = 37
    numerador2 = 38
    denominador = 1
    
    while denominador <= 37:
        termo = (numerador1 * numerador2) / denominador
        soma += termo
        numerador1 -= 1
        numerador2 -= 1
        denominador += 1
    
    print(soma)
    
    return 0
if __name__ == "__main__":
    main()
