def main():
    a = float(input())
    b = float(input())
    c = float(input())
    
    delta = b**2 - 4*a*c
    
    if (delta > 0):
        x1 = (-b + delta**(1/2))/(2*a)
        x2 = (-b - delta**(1/2))/(2*a)
        print(f'{x1:.1f} {x2:.1f}')
    elif (delta == 0):
        x1 = -b/(2*a)
        print(f'{x1:.1f}')
    else:
        print('Não possui raiz')
    return 0
if __name__ == "__main__":
    main()
