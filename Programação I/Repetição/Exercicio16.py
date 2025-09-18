def main():
    idade = int(0)
    soma_idade = int(0)
    cont = int(0)
    media_idade = float(0.0)
    
    soma_idade = 0
    cont = 0
    
    idade = int(input("Idade: "))
    while (idade > 0):
        soma_idade += idade
        cont += 1
        idade = int(input("Idade: "))
        
    media_idade = soma_idade / cont
    print(f'{media_idade}')
    
    return 0
if __name__ == "__main__":
    main()
