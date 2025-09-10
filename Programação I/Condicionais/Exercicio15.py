def main():
    hora_inicio = int(input())
    hora_fim = int(input())
    
    if (hora_inicio > hora_fim):
        duracao = (24-hora_inicio) + hora_fim
    elif (hora_inicio < hora_fim):
        duracao = hora_fim - hora_inicio
    else:
        duracao = 24
        
    print(f'{duracao}')
    
    
    return 0
if __name__ == "__main__":
    main()
