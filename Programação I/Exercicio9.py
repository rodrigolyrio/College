def main():
  nc = int(input("Número de carros vendidos: "))
  vt = float(input("Valor total das vendas: "))
  sf = float(input("Salário Fixo: "))
  vpc = float(input("Valor por carro vendido: "))
  salario = sf + vpc*nc + vt*5/100
  print(salario)
  return 0
if __name__ == "__main__":
    main()
