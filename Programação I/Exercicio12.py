def main():
    n = int(0)
    c = int(0)
    parte = int(0)
    d = int(0)
    u = int(0)
    
    n = int(input("digite um valor: "))
    
    c = n // 100
    parte = n // 10
    d = parte % 10
    u = n % 10
    invertido = u*100 + d*10 + c
    
    print(f'{invertido}')
    return 0
if __name__ == "__main__":
    main()
