def main():
    n_turma = int(0) #Número de turmas
    id_turma = str("") #Identificação da turma
    qtd_alunos = int(0) #Quantidade de alunos
    mat_aluno = str("") #Matrícula do aluno
    freq_aluno = str("") #Frequência do aluno (A ou P)
    ausencia = 0 #Controle das ausências
    presenca = 0 #Controle das presenças
    o = 0 #Quantidade da repetição geral das turmas
    perc_20 = 0 #Cálculo da ausencia maior que 20%
    b = True #Valor Booleano para definir a maior e menor ausência inicial
    
    maior_ausencia = str("") #Turma com a maior ausência
    maior_perc = int(0) #Maior porcentagem de ausência(Numérico)
    menor_ausencia = str("") #Turma co ma menor ausência
    menor_perc = int(0) #Porcentagem da menor ausência
    #Entrada de dados
    n_turma = int(input()) #Solicitando o número de turmas
    while(o != n_turma): #Repetição até alcançar o número de turmas
    
        i = 0 #Controle da quantidade de alunos
        ausencia = 0 #Controle das ausências
        presenca = 0 #Controle das presenças
        id_turma = str(input()) #Solicitando a identificação da turma
        qtd_alunos = int(input()) #Solicitando a quantidade de alunos
        while(i != qtd_alunos): #Repetição solicitando os dados dos alunos
            mat_aluno = str(input()) #Matricula do aluno
            freq_aluno = str(input()) #frequência do aluno
            #Coletando a quantidade de ausência e presença na repetição
            if(freq_aluno.upper() == "A"):
                ausencia += 1
            elif(freq_aluno.upper() == "P"):
                presenca += 1
            i += 1 #Controle da quantidade de repetições do aluno
        perc_ausencia = ((100 / qtd_alunos ) * ausencia) #Calculo da porcentagem de ausência

        if(perc_ausencia > 20): 
            perc_20 += 1
            #Valor Booleano para definir a maior e menor ausência/turma
        if(b == True):
            maior_ausencia = id_turma
            maior_perc = perc_ausencia
            menor_ausencia = id_turma
            menor_perc = perc_ausencia
            b = False
        if(b == False):
            if(maior_perc < perc_ausencia): #Novas definições de maior e menor porcentagem/turma
                maior_perc = perc_ausencia
                maior_ausencia = id_turma
            elif(menor_perc > perc_ausencia):
                menor_perc = perc_ausencia
                menor_ausencia = id_turma
                
        print(f'TURMA={id_turma} AUSENCIA={perc_ausencia:.2f} %')
        o += 1
    print(f'TURMA COM MAIOR % DE AUSENCIA={maior_ausencia} AUSENCIA={maior_perc:.2f} %')
    print(f'TURMA COM MENOR % DE AUSENCIA={menor_ausencia} AUSENCIA={menor_perc:.2f} %')
    print(f'{perc_20} TURMAS COM % DE AUSENCIA SUPERIOR A 20%')
    
    
    return 0
if __name__ == "__main__":
    main()
