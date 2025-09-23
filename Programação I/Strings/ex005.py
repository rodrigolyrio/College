def main():
    n = input('nome: ')
    for i in range(len(n),-1,-1):
        print(n[0:i])
    return 0
if __name__ == "__main__":
    main()
