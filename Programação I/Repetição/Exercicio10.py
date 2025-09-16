def main():
    soma_positivos = 0
    soma_negativos = 0
    contador_negativos = 0
    contador = 0
    
    while contador < 5:
        valor = int(input(''))
        if valor > 0:
            soma_positivos += valor
        elif valor < 0:
            soma_negativos += valor
            contador_negativos += 1
        contador += 1
    
    if contador_negativos > 0:
        media_negativos = soma_negativos / contador_negativos
    else:
        media_negativos = 0
    
    print(soma_positivos)
    print(media_negativos)
        
    
    return 0
if __name__ == "__main__":
    main()
