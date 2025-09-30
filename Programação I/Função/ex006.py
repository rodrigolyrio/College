def f_fatorial(n):
  fatorial = int(0)
  fatorial = 1
  while (n > 1):
    fatorial *= n #fatorial = fatorial * n
    n -= 1 #n = n - 1
  return fatorial

def main():
  a = int()
  a = int(input())
  while (a >= 0):
    if(a >= 0):
      print(f'Fatorial({a})={f_fatorial(a)}')
    else:
        if (a == 0):
          print(f'Fatorial({a})=1')
    a = int(input())
  
  return 0
if __name__ == "__main__":
  main()
