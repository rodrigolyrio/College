def f_soma(x,y):
    return x + y
    
def f_sub(x,y):
    return x - y
    
def f_mult(x,y):
    return x * y
    
def f_div(x,y):
    return x / y
    
def f_pot(x,y):
    return x ** y
    
def f_raiz(x,y):
    return x ** (1/y)
    
    
def f_menu():
    print('menu de operações:\n')
    print('1 - soma')
    print('2 - subtração')
    print('3 - multiplicação')
    print('4 - divisão')
    print('5 - potência')
    print('6 - raiz\n')
    print('escolha sua opção')
    
def main():
    r = input().upper()
    if (op >= 1 and op <= 6):
        a = int(input())
        b = int(input())
        if (op == 1):
            print(f'{f_soma(a,b)}')
        if (op == 2):
            print(f'{f_sub(a,b)}')
        if (op == 3):
            print(f'{f_mult(a,b)}'}
        if (op == 4):
            print(f'{f_div(a,b)}')
        if (op == 5):
            print(f'{f_pot(a,b)}')
        if (op == 6):
            print(f'{f_raiz(a,b)}')
            
    else:
        print('OPERAÇÃO INVALIDA')
    r = input().upper()
    return 0
if __name__ == "__main__":
    main()
