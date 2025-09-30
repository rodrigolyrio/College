def f_tamanho(n):
    cont = 0
    while (n > 0):
        cont = cont + 1
        n = n // 10
    return cont

def main():
    n1 = int(input('valor: '))
    print(f_tamanho(n1))
    
    
    return 0
if __name__ == "__main__":
    main()
