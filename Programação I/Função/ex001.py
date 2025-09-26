def f_soma(x,y):
    soma = x + y
    return soma
    
def main():
    valor1 = int(0)
    valor2 = int(0)

    valor1 = int(input(''))
    valor2 = int(input(''))
    
    soma = f_soma(valor1,valor2)
    print(soma)
    
    return 0
if __name__ == "__main__":
    main()
