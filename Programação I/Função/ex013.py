def f_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
def main():
    ano = int(input())
    if (f_bissexto(ano)):
        print("É BISSEXTO")
    else:
        print("NÃO É BISSEXTO")
    return 0
if __name__ == "__main__":
    main()
