def main():
    valorporhora = float(input(''))
    horastrabalhadas = float(input(''))
    
    salariobruto = valorporhora * horastrabalhadas
    
    impostorenda = 0.11 * salariobruto
    inss = 0.08 * salariobruto
    sindicato = 0.05 * salariobruto
    
    salarioliquido = salariobruto - (impostorenda + inss + sindicato)
    
    print(f"+ Salário Bruto : R$ {salariobruto:.2f}")
    print(f"- IR (11%) : R$ {impostorenda:.2f}")
    print(f"- INSS (8%) : R$ {inss:.2f}")
    print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
    print(f"= Salário Líquido : R$ {salarioliquido:.2f}")
    
    return 0
if __name__ == "__main__":
    main()
