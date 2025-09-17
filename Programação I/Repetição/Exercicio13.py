def main():
    sexo = str("")
    altura = float(0.0)
    maior = float(0.0)
    menor = float(0.0)
    med_alt_f = float(0.0)
    soma_alt_f = float(0.0)
    cont_f = int(0)
    cont_m = int(0)
    i = int(0) 
    
    i = 0
    cont_f = 0
    cont_m = 0
    soma_alt_f = 0
    
    while(i < 5):
        sexo = input("sexo: ")
        altura = float(input("altura: "))
        if (i == 0):
            maior = altura
            menor = altura
        elif (altura > maior):
            maior = altura
        elif (altura < menor):
            menor = altura
        if (sexo.upper() == "F"):
            soma_alt_f += altura
            cont_f += 1
        else:
            cont_m += 1
        i += 1
    
    med_alt_f = soma_alt_f/cont_f
    print(maior)
    print(menor)
    print(med_alt_f)
    print(cont_m)
    
    return 0
if __name__ == "__main__":
    main()
