def main():
    soma = 0
    numerador = 1
    denominador = 1
    
    while numerador <= 99 and denominador <= 50:
        termo = numerador / denominador
        soma += termo
        numerador += 2
        denominador += 1
    
    print(soma)
        
    return 0
if __name__ == "__main__":
    main()
