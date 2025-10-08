def f_checknum(n):
    soma = 0
    for i in range(len(n)):
        soma += int(n[i])** len(n)
    return soma
    
def main():
    s = 1
    n = str()
    while (len(n) <= 6):
        n = str(s)
        if str(f_checknum(n)) == n:
            print(n)
        s += 1
if __name__ == "__main__":
    main()
