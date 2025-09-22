def main():
    s1 = input('texto1: ')
    s2 = input('texto2: ')
    if(len(s1) == len(s2)):
        print('MESMO TAMANHO')
        if(s1 == s2):
            print('CONTEÚDO IGUAL')
        else:
            print('CONTEÚDO DIFERENTE')
    else:
        print('TAMANHO DIFERENTE')
        print('CONTEÚDO DIFERENTE')
    
    return 0
if __name__ == "__main__":
    main()
