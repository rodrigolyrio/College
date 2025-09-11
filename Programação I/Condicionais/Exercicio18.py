def main():
    
    quantidade_atual = int(input(""))
    quantidade_maxima = int(input(""))
    quantidade_minima = int(input(""))
    
    quantidade_media = (quantidade_maxima + quantidade_minima) / 2
    
    if quantidade_atual >= quantidade_media:
        print("NÃO EFETUAR COMPRA")
    else:
        print("EFETUAR COMPRA")
    
    
    return 0
if __name__ == "__main__":
    main()
