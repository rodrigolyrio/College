def f_soma(x,y,z):
    soma = x + y + z
    return soma

def main():
    a = int(0)
    b = int(0)
    c = int(0)
    
    a = int(input(''))
    b = int(input(''))
    c = int(input(''))
    
    soma = f_soma(a,b,c)
    print(soma)
    
    return 0
if __name__ == "__main__":
    main()
