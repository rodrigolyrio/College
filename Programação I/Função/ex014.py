def f_criaForca(segredo):
    n = ''
    for i in range(len(segredo)):
        n += ' '
    return n
    
    
def f_testaLetra(forca,segredo,letra):
    n = ''
    for i in range(len(segredo)):
        if (letra == segredo[i]):
            n += letra
        else:
            n += forca[i]
    return n
    
def f_print(f):
    n = ''
    for i in range(len(f)):
        n += f[i]+' '
    print(f'{n}')
    
def f_ganhou(segredo,forca):
    if (segredo == forca):
        return True
    else:
        return False
        
def f_verifica(letra,segredo):
    for i in range(len(segredo)):
        if (letra == segredo[i]):
            return True
    return False
    
def main():
    erradas = ''
    jogadas = 0
    erros = 0
    segredo = input().upper()
    forca = f_criaForca(segredo)
    while (erros < 6 and f_ganhou(segredo, forca) == False):
        jogadas += 1
        f_print(forca)
        print(f'{erradas}')
        letra = input().upper()
        forca = f_testaLetra(forca,segredo,letra)
        if (f_verifica(letra,segredo) == False):
            erradas += letra
            erros += 1
    if (f_ganhou(segredo, forca)):
        f_print(forca)
        print(f'Parabéns, você ganhou com {jogadas} jogadas')
    else:
        f_print(forca)
        print(f'{erradas}')
        print(f'Que pena, você não acertou a palavra {segredo}')
        
    return 0
if __name__ == "__main__":
    main()
