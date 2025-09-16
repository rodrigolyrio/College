def main():
    flag = str ("")
    n = int(0)
    soma_pos = int(0)
    soma_neg = int(0)
    n = 0
    soma_pos = 0
    soma_neg = 0
    flag = input("deseja informar um valor? <s/n>: ")
    while (flag.upper() == "S"):
        n = int(input())
        if (n > 0):
            soma_pos += n
        elif (n < 0):
            soma_neg += n
        flag = input("deseja informar outro valor? <s/n>: ")
    print(f'{soma_pos} {soma_neg}')
    return 0
if __name__ == "__main__":
    main()
