def main():
    a = float(input("X1: "))
    c = float(input("Y1: "))
    b = float(input("X2: "))
    d = float(input("Y2: "))
    soma = ((b-a)**2 + (c-d)**2)**(1/2)
    
    print(soma)
    return 0
    
if __name__ == "__main__":
    main()
