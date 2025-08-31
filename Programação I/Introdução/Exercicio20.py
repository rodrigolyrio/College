def main():
    
    tamanhoarquivo = float(input(""))
    velocidadeinternet = float(input(""))
    
    velocidadembps = velocidadeinternet * 0.125
    
    tempodownloadsegundos = (tamanhoarquivo / velocidadembps)

    print(f"{tempodownloadsegundos:.2f} segundos")
    
    return 0
if __name__ == "__main__":
    main()
