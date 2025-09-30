def f_tamanho(n):
  cont = 0
  while (n > 0):
    cont = cont + 1
    n = n // 10
  return cont

def f_inverte(n):
  pot = f_tamanho(n)-1
  invertido = 0
  while (n > 0):
    resto = n % 10
    invertido = invertido + resto * 10 ** pot
    n = n // 10
    pot = pot - 1
  return invertido

def main():
  a = int(input(''))
  print(f_inverte(a))
  
  return 0
if __name__ == "__main__":
  main()
