def f_menor(a,b,c):
    if (a < b and a < c):
        return a
    else: 
        if (b < c):
            return b
        else:
            return c
            
def f_med(a,b,c):
    m = f_menor(a,b,c)
    while(m > 0):
        if (a % m == 0 and b % m == 0 and c % m == 0):
            return m
        m = m - 1
        
def main():
    
    for i in range(4):
        a = int(input())
        b = int(input())
        c = int(input())
        print(f'MDC({a}, {b}, {c})={f_med(a,b,c)}')
        
    return 0
    
if __name__ == "__main__":
    main()
