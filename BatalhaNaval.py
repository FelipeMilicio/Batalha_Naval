def iniciar_batalha_naval():

    matriz = []
    #gerar matriz
    for i in range(10):
        lista = [' '] * 10
        matriz.append(lista)
        valor = "x"

    #dicionarios que definem os barcos e as suas quantidades
    tipos_barcos = {
        1: {"nome": "Destroier", "tamanho": 1},
        2: {"nome": "Submarino", "tamanho": 2},
        3: {"nome": "Contratorpedeiro", "tamanho": 3},
        4: {"nome": "Navio-Tanque", "tamanho": 4},
        5: {"nome": "Porta-Aviões", "tamanho": 5},
    }
    contadores = {
        1:5,
        2:4,
        3:3,
        4:2,
        5:1,
    }
    #verificação de disponibilidade do espaço
    def verificar_disponibilidade(matriz, linha1, linha2, coluna1, coluna2, orientacao, tamanho, valor):
        if orientacao == "vertical":
            inicio = min(linha1, linha2)
            for i in range(tamanho):
                if matriz[inicio + i][coluna1] != ' ':
                    return False
        elif orientacao == "horizontal":
            inicio = min(coluna1, coluna2)
            for i in range(tamanho):
                if matriz[linha1][inicio + i] != ' ':
                    return False
        return True
    
    def marcar_area_ao_redor(matriz, linha1, linha2, coluna1, coluna2, orientacao):
        #os for são para pegar a área ao redor do barco
        for i in range(linha1 - 1, linha2 + 2):
            for j in range(coluna1 - 1, coluna2 + 2):
                #garante que não vai tentar colocar uma marcação fora da matriz
                if 0 <= i < 10 and 0 <= j < 10:
                    if matriz[i][j] == ' ':
                        matriz[i][j] = 'O'

        
    #def para colocar o barco
    def colocar_barco(matriz, linha1, linha2, coluna1, coluna2, orientacao, tamanho, valor):
        if not verificar_disponibilidade(matriz, linha1, linha2, coluna1, coluna2, orientacao, tamanho, valor):
            print("A posição do barco está conflitando com outro já colocado")
            return False

        if orientacao == "vertical":
            inicio = min(linha1, linha2)
            for i in range(tamanho):
                matriz[inicio + i][coluna1] = valor
        elif orientacao == "horizontal":
            inicio = min(coluna1, coluna2)
            for i in range(tamanho):
                matriz[linha1][inicio + i] = valor

        marcar_area_ao_redor(matriz, linha1, linha2, coluna1, coluna2, orientacao)
        return True

    print("Vamos colocar os seus barcos!")
    while any(contadores.values()):
    #pegar inputs do usuario e responder a algum erro
        try:
            print("\nBarcos restantes:")
            for tipo, quantidade in contadores.items():
                if quantidade > 0:
                    print(f"{tipo} - {tipos_barcos[tipo]['nome']} (tamanho {tipos_barcos[tipo]['tamanho']}): {quantidade} restante(s)")
            escolha_tipo = int(input("Escolha o tipo de barco (1-5): "))
            barco = tipos_barcos.get(escolha_tipo)
            if not barco:
                print("Tipo de barco inválido")
                continue
            
            if contadores[escolha_tipo] <= 0:
                print("Quantidade deste tipo de barco esgotada")
                continue
            
            escolha_rotacao = str(input("Escolha a rotação (vertical ou horizontal): ")).lower()
            tamanho = barco["tamanho"]

            if escolha_rotacao == "vertical":
                linha1 = int(input("Escolha a linha inicial (1-10): ")) - 1
                coluna = int(input("Escolha a coluna (1-10): ")) - 1
                if linha1 + tamanho > 10:
                    print("O barco saiu da matriz")
                    continue
                linha2 = linha1 + tamanho - 1
                if colocar_barco(matriz, linha1, linha2, coluna, coluna, "vertical", tamanho, valor):
                    contadores[escolha_tipo] -= 1
            
            elif escolha_rotacao == "horizontal":
                coluna1 = int(input("Escolha a coluna inicial (1-10): ")) - 1
                linha = int(input("Escolha a linha (1-10): ")) - 1
                if coluna1 + tamanho > 10:
                    print("O barco foi posicionado inteiramente ou parcialmente fora da matriz")
                    continue
                coluna2 = coluna1 + tamanho - 1
                if colocar_barco(matriz, linha, linha, coluna1, coluna2, "horizontal", tamanho, valor):
                    contadores[escolha_tipo] -= 1
            else:
                print("Escolha de rotação inválida")

        except ValueError:
            print("Inserção inválida, use números inteiros")

        for lista in matriz:
            print(lista)
    
    #sistema de ataque
    def atacar_barco(linha_ataque, coluna_ataque, acerto):
        linha_ataque = int(input("Insira a posição da linha para atacar: "))
        coluna_ataque = int(input("Insira a posição da coluna para atacar: "))
        if matriz[linha_ataque][coluna_ataque] == 'x':
            acerto == True
            if acerto == True:
                matriz[linha_ataque][coluna_ataque] = 'O'
                atacar_barco()
            else:
                return #vez do bot
            

iniciar_batalha_naval()



