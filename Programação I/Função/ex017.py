def f_fibo(n):
    i = 0
    a = 1
    print(a)
    for x in range(n-1):
        p = i + a
        print(p)
        i = a
        a = p
def main():
    q = int(input())
    f_fibo(q)
    return 0
if __name__ == "__main__":
    main()
