def f_tam(n):
    tamanho = 0
    while (n > 0):
        n = n // 10
        tamanho += 1
    return tamanho
    
def f_armstrong(n):
    soma = 0
    comparar = n
    potencia = f_tam(n)
    while (n > 0):
        resto = n % 10
        soma += resto ** potencia
        n = n // 10
    return soma == comparar
    
def main():
    for i in range(1,1000000):
        if (f_armstrong(i)):
            print(i)
    
    
    return 0
if __name__ == "__main__":
    main()
