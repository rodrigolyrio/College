def f_dec2bin(n):
  b = str('')
  b = ''
  while(n > 0):
      resto = n % 2
      b = str(resto) + b
      n = n // 2
  return b

def f_dec2hex(n):
    h = str('')
    h = ''
    while(n > 0):
        resto = n % 16
        if (resto < 10):
            h = str(resto) + h
        else:
            h = f_letrahex2(resto) + h
        n = n // 16
    return h

def f_letrahex2(x):
    hex = 'ABCDEF'
    return hex[x-10]

    
def main():
    
    n = int(input())
    while(n >= 0):
        bin = f_dec2bin(n)
        hex = f_dec2hex(n)
        print(f'DEC={n} BIN={bin} HEX={hex}')
        n = int(input())
    return 0 
    
if __name__ == "__main__":
    main()
