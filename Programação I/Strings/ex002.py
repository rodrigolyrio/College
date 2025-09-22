def main():
    p = ''
    name = input('insira seu nome: ')
    for i in range(len(name)-1,-1,-1):
        p = p + name[i].upper()
    print(p)
    
    return 0
if __name__ == "__main__":
    main()
