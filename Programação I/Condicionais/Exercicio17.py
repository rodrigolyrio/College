def main():
    
    sexo = input("")
    altura = float(input(""))
    
    peso_ideal = 0
    
    if sexo == 'M':
        peso_ideal = 72.7 * altura - 58
    
    if sexo == 'F':
        peso_ideal = 62.1 * altura - 44.7
    
    if peso_ideal != 0:
        print(f"{peso_ideal:.3f}")
    else:
        print("Sexo inválido. Por favor, insira M para masculino ou F para feminino.")
        
    return 0
if __name__ == "__main__":
    main()
