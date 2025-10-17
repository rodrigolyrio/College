def f_naoExiste(l,v):
    for i in range(len(v)):
        if (l == v[i]):
            return False
    return True

def f_vogais(t):

    v = str('')
    vogais = str('')

    v = 'AEIOU'
    vogais = ''

    for i in range(len(t)):
        for j in range(len(v)):
            if (t[i] == v[j]):
                if (f_naoExiste(t[i],vogais) == True):
                    vogais += t[i]
    return vogais

def f_naoEhVogal(letra,v):
    for i in range(len(v)):
        if (letra == v[i]):
            return False
    return True

def f_removeVogais(v,t):
    consoantes = str('')
    consoantes = ''
    for i in range(len(t)):
        if(f_naoEhVogal(t[i],v)):
            consoantes += t[i]

    return consoantes

def f_alteraTexto(t):
    novo = str('')
    vogais = str('')
    cons = str('')
    vogais = f_vogais(t)
    cons = f_removeVogais(vogais,t)
    return vogais+cons

def main():
    t = str('')
    t = input().upper()
    while (t != ""):
        print(f_alteraTexto(t))
        t = input().upper()
    return 0

if __name__ == "__main__":
    main()
