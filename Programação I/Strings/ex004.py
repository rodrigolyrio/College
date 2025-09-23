def main():
    name = input('nome: ')
    for i in range(len(name)):
        print(name[0:i+1:1])
    return 0
if __name__ == "__main__":
    main()
