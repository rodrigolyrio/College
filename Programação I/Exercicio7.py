def main():
    salario = float(input("Salario: "))
    reajuste = float(input("Reajuste: "))
    novo = salario + salario*reajuste/100
    print(novo)
    
    return 0
    
if __name__ == "__main__":
    main()
