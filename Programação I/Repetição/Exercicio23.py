def main():
    time_a = str("")
    time_b = str("")
    gols_a = int(0)
    gols_b = int(0)
    total_gols = 0
    i = 0
    bl = False
    maior_gol = int(0)
    menor_gol = int(0)
    maior_time = str("")

    time_a = str(input())

    while(time_a != ""):
        time_b = str(input())
        gols_a = int(input())
        gols_b = int(input())

        if(gols_a >= 0 and gols_b >= 0):
            print(f'{time_a} x {time_b}')
            if(gols_a > gols_b):
                print(f'Vencedor: {time_a}')
            elif(gols_a < gols_b):
                print(f'Vencedor: {time_b}')
            elif(gols_a == gols_b):
                print(f'Empate')
        total_gols += gols_a
        total_gols += gols_b
        
        i += 1
        
        if(gols_a < gols_b):
            if(gols_a < menor_gol):
                menor_gol = gols_a
        elif(gols_a > gols_b):
            if(gols_b < menor_gol):
                menor_gol = gols_b

        if(gols_a > gols_b):
            if(gols_a > maior_gol):
                maior_gol = gols_a
                maior_time = time_a
        elif(gols_a < gols_b):
            if(gols_b > maior_gol):
                maior_gol = gols_b
                maior_time = time_b
        time_a = str(input())
    print(f'Média de Gols: {total_gols / i} por jogo')
    print(f'Time que fez mais gols em um jogo: {maior_time}')
    print(f'Menor número de gols em uma partida: {menor_gol}')
    return 0
if __name__ == "__main__":
    main()
