def main():
    cf = float(input("Custo de fábrica: "))
    custo = cf + cf*28/100 + cf*45/100
    print(custo)
    return 0 
if __name__ == "__main__":
    main()
