def f_remvog(s):
    novo = str()
    for i in range(len(s)):
        if (s[i]).upper() != 'A' and (s[i]).upper() != 'E' and (s[i]).upper() != 'I' and (s[i]).upper() != 'O' and (s[i]).upper() != 'U':
            novo += s[i]
    return novo
        
def main():
    s = input()
    while s != '':
        print(f_remvog(s))
        s = input()

    return 0
if __name__ == "__main__":
    main()
