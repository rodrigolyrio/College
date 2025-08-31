def main():
    #declaração de variáveis
    area = float(0.0)
    
    #entrada de dados
    area = float(input())
    
    #processamento
    litros = area/6
    
    if (litros % 18 == 0):
        latas = litros//18
    else:
        latas = litros//18 + 1
        
    if (litros % 3.6 == 0):
        galoes = litros//3.6
    else:
        galoes = litros//3.6 + 1
        
    v_lat = latas*80
    v_gal = galoes*25
    
    print(f'Você utilizará {latas:.0f}) de 18L. Valor = {v_lat:.2f}')
    print(f'Você utilizará {galoes:.0f} de 3.6L. Valor = {v_gal:.2f}')
    return 0
    
if __name__ == "__main__":
    main()
