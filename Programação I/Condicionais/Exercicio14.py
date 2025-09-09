def main():
    litros = float(input())
    tipo = input()
    
    if (tipo == 'A'):
        valor = litros*2.9
        if (litros <= 20):
            desconto = valor*(3/100)
        else:
            desconto = valor*(5/100)
    else:
        valor = litros*3.3
        if (litros <= 20):
            desconto = valor*(4/100)
        else:
            valor = litros*3.3
            desconto = valor*(6/100)
    total = valor - desconto 
    print(f'{total:.2f}')
    
    return 0
if __name__ == "__main__":
    main()
