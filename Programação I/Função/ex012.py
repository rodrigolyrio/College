def f_limpaCPF(cpf):
    novo = str('')
    for i in range(len(cpf)):
        if (cpf[i] != '.'):
            novo += cpf[i]
    return novo

def f_dv(cpf,peso):
    total = 0
    for i in range(len(cpf)):
        total += int(cpf[i]) * peso
        peso -= 1
    resto = total % 11
    if (resto < 2):
        return '0'
    else:
        return str(11-resto)

def f_testaCPF(cpf):
    dv = cpf[12:]
    cpf = f_limpaCPF(cpf[:11])
    dv1 = f_dv(cpf,10)
    cpf = cpf + dv1
    dv2 = f_dv(cpf,11)
    testeDV = dv1+dv2
    if (dv == testeDV):
        return True
    else:
        return False

def main():
    cpf = str('')
    cpf = input()

    if (f_testaCPF(cpf)):
        print('CPF VÁLIDO')
    else:
        print('CPF INVÁLIDO')

    return 0

if __name__ == "__main__":
    main()
