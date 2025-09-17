def main():
    palavra = input("")
    
    contador = 0
    
    while contador < len(palavra):
        letra = palavra[contador]
        print(letra)
        contador += 1
    
    return 0
if __name__ == "__main__":
    main()
