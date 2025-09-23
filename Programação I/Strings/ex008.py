def main():
    f1 = input('texto: ')
    f2 = ''
    for i in range(len(f1)):
        if (f1[i] != ' '):
            f2 += f1[i]
    print(f2)
    
    if (f2 == f2[::-1]):
        print('É PALÍNDROMO')
    else: 
        print('NÃO É PALÍNDROMO')
    return 0
if __name__ == "__main__":
    main()
