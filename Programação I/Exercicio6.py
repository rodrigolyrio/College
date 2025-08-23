def main():
  total = int(input("Total de eleitores: "))
  brancos = int(input("Votos em Brancos: "))
  nulos = int(input("Votos nulos: "))
  validos = int(input("votos validos: "))
  pb = brancos * 100 / total
  pn = nulos * 100 / total
  pv = validos * 100 / total
  print(f"BRANCOS={pb:.1f}%")
  print(f"NULOS={pn:.1f}%")
  print(f"VALIDOS={pv:.1f}%")
  return 0
if __name__ == "__main__":
  main()
