def main():
    soma = 0
    a = 1
    b = 2
    
    while (a < 6):
        soma += -(a + a ** 2)/b
        a += 1
        b += 2
        soma += (a + a ** 2)/b
    print(soma)
    
    
    return 0
if __name__ == "__main__":
    main()
