def main():

    nickname = str("")
    soma = int(0)
    soma_pontos = int(0)

    soma_pontos = 0
    cont = 0

    nickname = input("")
    while(nickname != ""):
        soma = 0
        for i in range(0, 10, 1):
            pontuacao_fases = input("")
            if(pontuacao_fases == "A1"):
                soma += 5
            elif(pontuacao_fases == "A2"):
                soma += 7
            elif(pontuacao_fases == "A3"):
                soma += 10
            elif(pontuacao_fases == "E1"):
                soma -= 2
            elif(pontuacao_fases == "E2"):
                soma -= 5
            elif(pontuacao_fases == "E3"):
                soma = 0
            if(soma < 0):
                soma = 0
            
        print(f'{nickname} {soma} pontos')
        
        soma_pontos += soma
        
        if (cont == 0):
            nick_maior = nickname
            soma_maior = soma
        elif (soma > soma_maior):
            nick_maior = nickname
            soma_maior = soma
        cont += 1 
        nickname = input("")
    print(f'Média de pontos = {soma_pontos/cont:.2f} por jogo')
    print(f'Vencedor {nick_maior} com {soma_maior} pontos')
    
    return 0
if __name__ == "__main__":
    main()
