def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    if (a < b and a < c):
        if (b < c):
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        if (b < c):
            if (a < c):
                print(b,a,c)
            else:
                print(b,c,a)
        else:
            if (a < b):
                print(c,a,b)
            else: 
                print(c,b,a)
    return 0
if __name__ == "__main__":
    main()
