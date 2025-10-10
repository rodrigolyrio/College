def f_menor_letra(palavra):
    menor = palavra[0]
    for letra in palavra:
        if(letra<menor):
            menor = letra
    return menor
    
    
def main():
    palavra = input().upper()
    while(palavra != ''):
        letra_menor = f_menor_letra(palavra)
        print(f'{letra_menor}')
        palavra = input().upper()
        
        
    return 0
if __name__ == "__main__":
    main()
