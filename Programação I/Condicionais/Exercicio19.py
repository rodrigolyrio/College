def main():

    idade_homem1 = int(input(""))
    idade_homem2 = int(input(""))
    idade_mulher1 = int(input(""))
    idade_mulher2 = int(input(""))
    
    if idade_homem1 > idade_homem2:
        homem_mais_velho = idade_homem1
        homem_mais_novo = idade_homem2
    else:
        homem_mais_velho = idade_homem2
        homem_mais_novo = idade_homem1
    
    if idade_mulher1 > idade_mulher2:
        mulher_mais_velha = idade_mulher1
        mulher_mais_nova = idade_mulher2
    else:
        mulher_mais_velha = idade_mulher2
        mulher_mais_nova = idade_mulher1
    
    soma_idades = homem_mais_velho + mulher_mais_nova
    produto_idades = homem_mais_novo * mulher_mais_velha
    
    print(f"{soma_idades} {produto_idades}")
    
    return 0
if __name__ == "__main__":
    main()
