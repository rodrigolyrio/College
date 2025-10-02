def f_tam(n):
    tam = int(0)
    tam = 0
    while (n > 0):
        n = n // 10
        tam += 1
    return tam
    
def f_inverte(a):
    novo = int(0)
    p = int(0)
    resto = int(0)
    novo = 0
    p = f_tam(a)-1
    while (a > 0):
        resto = a % 10
        novo += resto*10**p
        a = a // 10
        p = p - 1
    return novo

def f_capicua(x):
    if (x == f_inverte(x) and x >= 10):
        return True
    return False

def f_qperfeito(x):
    y = int(0)
    y = 1
    while (y**2 <= x):
        if (y**2 == x):
            return True
        y += 1
    return False

def main():
    n = int(0)
    for n in range(1,5001):
        if (f_capicua(n) and f_qperfeito(n)):
            print(f'{n} É CAPICUA E QUADRADO PERFEITO')
        elif (f_capicua(n)):
            print(f'{n} É CAPICUA')
        elif (f_qperfeito(n)):
            print(f'{n} É QUADRADO PERFEITO')
    return 0

if __name__ == "__main__":
    main()
