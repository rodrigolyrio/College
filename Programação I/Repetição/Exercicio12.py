def main():
    flag = str("") #variavel de controle
    n = int(0)
    soma_pos = int(0)
    soma_neg = int(0)
    cont_neg = int(0)
    media_neg = float(0.0)
    
    soma_pos = 0
    soma_neg = 0
    cont_neg = 0
    
    flag = input("deseja digitar um valor <s/n>?: ") #inicialização da variável de controle
    while (flag.upper() == "S"): 
        n = int(input("n: "))
        if (n < 0):
            soma_neg += n 
            cont_neg += 1 
        else: 
            soma_pos += n 
        
        flag = input("deseja informar um numero <s/n>?")
        
    media_neg = soma_neg/cont_neg
    print(f'{soma_pos} {media_neg}')
    return 0
if __name__ == "__main__":
    main()
