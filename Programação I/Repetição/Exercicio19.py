def main():
    soma = 0
    denominador = 1
    
    while denominador <= 10:
        numerador = denominador
        termo = numerador / (denominador**2)
        
        if denominador % 2 == 0:
            soma -= termo
        else:
            soma += termo
    
        denominador += 1
    
    print(soma)

    return 0
if __name__ == "__main__":
    main()
