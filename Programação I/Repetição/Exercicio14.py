def main():
    pkwh = float(0.0)
    cons = int(0)
    qkwh = float(0.0)
    tipo = str ('')
    total = float (0.0)
    maior = float(0.0)
    menor = float(0.0)
    totalR = float(0.0)
    totalC = float(0.0)
    totalI = float(0.0)
    somakwh = float(0.0)
    cont_cons = int(0)
    media = float(0.0)
    
    totalR = 0
    totalC = 0
    totalI = 0
    somakwh = 0
    cont_cons = 0
    
    pkwh = float(input("valor do kwh: "))
    cons = int(input("digite o codigo consumido: "))
    while (cons != 0):
        qkwh = float(input("Consumo: "))
        tipo = input("tipo: ")
        
        total = pkwh*qkwh
        print(f'{cons} {total}')
        if (cont_cons == 0):
            maior = qkwh
            menor = qkwh
        elif (qkwh > maior):
            maior = qkwh
        elif (qkwh < menor):
            menor = qkwh
            
        if (tipo.upper() == "R"):
            totalR += qkwh
        elif (tipo.upper() == "C"):
            totalC += qkwh
        elif (tipo.upper() == "I"):
            totalI += qkwh
            
        somakwh += qkwh
        cont_cons += 1
        cons = int(input("digite o valor consumido: "))
        
    media = somakwh / cont_cons
    
    print(f'{maior}')
    print(f'{menor}')
    print(f'{totalR}')
    print(f'{totalC}')
    print(f'{totalI}')
    print(f'{media}')
    return 0
if __name__ == "__main__":
    main()
