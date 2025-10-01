def f_maisProximo(x,a):
    if (a - x**2 < (x+1)**2 - a):
        return x
    else:
        return x + 1
        
def f_procuraRaizProx(a):
    n = 1
    while(n**2 < a):
        n = n + 1
    n = f_maisProximo(n-1,a)
    return n**2
    
def f_calculaRaizNewton(a):
    x2 = f_procuraRaizProx(a)
    x = x2**(1/2)
    if (x != 0):
        raiz = (a+x2)/(2*x)
        return raiz
    return 0
    
def main():
    a = 0
    while (a >= 0):
        a = int(input())
        if(a >= 0):
            raiz = f_calculaRaizNewton(a)
            print(f'N={a:.4f} RAIZ={raiz:.6f}')
    return 0

if __name__ == "__main__":
    main()
