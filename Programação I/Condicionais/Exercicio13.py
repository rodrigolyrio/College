def main():
    a = float(input())
    b = float(input())
    c = float(input())
    
    if (a + b > c and a + c > b and b + c > a):
        if ((a == b and a != c) or (b == c and b != a) or (a == c and c != b)):
            print('ISÓSCELES')
        else:
            if (a == b and b == c):
                print('EQUILÁTERO')
            else:
                print('ESCALENO')
    else:
        print('NÃO É TRIÂNGULO')
    
    return 0
if __name__ == "__main__":
    main()
