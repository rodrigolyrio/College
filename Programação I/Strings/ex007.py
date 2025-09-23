def main():
    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0
    cont_b = 0
    s = input('frase: ')
    for i in range(len(s)):
        if (s[i] == ' '):
            cont_b = cont_b + 1
        elif (s[i].upper() == 'A'):
            cont_a += 1
        elif (s[i].upper() == 'E'):
            cont_e += 1
        elif (s[i].upper() == 'I'):
            cont_i += 1
        elif (s[i].upper() == 'O'):
            cont_o += 1
        elif (s[i].upper() == 'U'):
            cont_u += 1
    print(f'ESPAÇOS EM BRANCO = {cont_b}')
    print(f'A = {cont_a}')
    print(f'E = {cont_e}')
    print(f'I = {cont_i}')
    print(f'O = {cont_o}')
    print(f'U = {cont_u}')
    return 0
if __name__ == "__main__":
    main()
