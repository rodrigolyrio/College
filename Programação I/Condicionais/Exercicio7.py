def main():
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    n3 = float(input("n3: "))
    n4 = float(input("n4: "))
    media = (n1+n2+n3+n4)/4
    if (media >= 60):
        print("APROVADO")
    else:
        print("REPROVADO")
    return 0 
if __name__ == "__main__":
    main()
