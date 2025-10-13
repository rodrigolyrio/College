def f_naoExiste(letra,repetidas):
    for i in range(len(repetidas)):
        if (letra == repetidas[i]):
            return False
    return True
    
def f_repetidas(p):
    repetidas = ''
    for i in range(len(p)):
        cont = 0
        letra = p[i]
        for j in range(i+1, len(p)):
            if (letra == p[j]):
                cont += 1
        if (cont > 0):
            if (f_naoExiste(letra,repetidas)):
                repetidas += letra
    return repetidas
    
    
def f_contaRepetidas(repetidas, palavra):
    print(palavra)
    if (len(repetidas) > 0):
        for i in range(len(repetidas)):
            cont = 0
            for j in range(len(palavra)):
                if (repetidas[i] == palavra[j]):
                    cont += 1
            print(f'{repetidas[i]}={cont}')
    else:
        print('NÃO EXISTEM LETRAS REPETIDAS')
        
def main():
    palavra = input()
    while (palavra != ''):
        repetidas = f_repetidas(palavra)
        f_contaRepetidas(repetidas, palavra)
        palavra = input()
    return 0
    
if __name__ == "__main__":
    main()
