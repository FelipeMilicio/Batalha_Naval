import random

def iniciar_batalha_naval():

    def criar_tabuleiro():
        tabuleiro = []
        for i in range(10):
            linha = [' '] * 10
            tabuleiro.append(linha)
        return tabuleiro

    tabuleiro_jogador = criar_tabuleiro()
    tabuleiro_computador = criar_tabuleiro()
    tabuleiro_jogador_ataques = criar_tabuleiro() # Para mostrar onde o jogador atacou o computador
    tabuleiro_computador_ataques = criar_tabuleiro() # Para mostrar onde o computador atacou o jogador

    #dicionarios que definem os barcos e as suas quantidades
    tipos_barcos = {
        1: {"nome": "Destroier", "tamanho": 1},
        2: {"nome": "Submarino", "tamanho": 2},
        3: {"nome": "Contratorpedeiro", "tamanho": 3},
        4: {"nome": "Navio-Tanque", "tamanho": 4},
        5: {"nome": "Porta-Aviões", "tamanho": 5},
    }
    contadores = {
        1:2,
        2:2,
        3:1,
        4:1,
        5:1,
    }
    #verificação de disponibilidade do espaço
    def verificar_disponibilidade(matriz, linha1, linha2, coluna1, coluna2, orientacao, tamanho):
        if orientacao == "vertical":
            inicio = min(linha1, linha2)
            for i in range(tamanho):
                if not (0 <= inicio + i < 10 and 0 <= coluna1 < 10 and matriz[inicio + i][coluna1] == ' '):
                    return False
        elif orientacao == "horizontal":
            inicio = min(coluna1, coluna2)
            for i in range(tamanho):
                if not (0 <= linha1 < 10 and 0 <= inicio + i < 10 and matriz[linha1][inicio + i] == ' '):
                    return False
        return True
    
    def marcar_area_ao_redor(matriz, linha1, linha2, coluna1, coluna2, orientacao, tamanho):
        if orientacao == "vertical":
            for i in range(max(0, linha1 - 1), min(10, linha2 + 2)):
                for j in range(max(0, coluna1 - 1), min(10, coluna1 + 2)):
                    if matriz[i][j] == ' ':
                        matriz[i][j] = 'O'
        elif orientacao == "horizontal":
            for i in range(max(0, linha1 - 1), min(10, linha1 + 2)):
                for j in range(max(0, coluna1 - 1), min(10, coluna2 + 2)):
                    if matriz[i][j] == ' ':
                        matriz[i][j] = 'O'

        
    #def para colocar o barco
    def colocar_barco(matriz, linha1, linha2, coluna1, coluna2, orientacao, tamanho):
        if not verificar_disponibilidade(matriz, linha1, linha2, coluna1, coluna2, orientacao, tamanho):
            return False

        if orientacao == "vertical":
            inicio = min(linha1, linha2)
            for i in range(tamanho):
                matriz[inicio + i][coluna1] = 'X'
        elif orientacao == "horizontal":
            inicio = min(coluna1, coluna2)
            for i in range(tamanho):
                matriz[linha1][inicio + i] = 'X'

        marcar_area_ao_redor(matriz, linha1, linha2, coluna1, coluna2, orientacao, tamanho)
        return True

    def posicionar_barcos_jogador(tabuleiro):
        print("Vamos colocar os seus barcos!")
        contadores_local = contadores.copy() # Usar uma cópia para não alterar o original
        while any(contadores_local.values()):
        #pegar inputs do usuario e responder a algum erro
            try:
                print("\nBarcos restantes:")
                for tipo, quantidade in contadores_local.items():
                    if quantidade > 0:
                        print(f"{tipo} - {tipos_barcos[tipo]['nome']} (tamanho {tipos_barcos[tipo]['tamanho']}): {quantidade} restante(s)")
                escolha_tipo = int(input("Escolha o tipo de barco (1-5): "))
                barco = tipos_barcos.get(escolha_tipo)
                if not barco:
                    print("Tipo de barco inválido")
                    continue
                
                if contadores_local[escolha_tipo] <= 0:
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
                    if colocar_barco(tabuleiro, linha1, linha2, coluna, coluna, "vertical", tamanho):
                        contadores_local[escolha_tipo] -= 1
                        print("Barco posicionado com sucesso!")  # Feedback
                    else:
                        print("A posição do barco está conflitando com outro já colocado")
                        continue
                
                elif escolha_rotacao == "horizontal":
                    coluna1 = int(input("Escolha a coluna inicial (1-10): ")) - 1
                    linha = int(input("Escolha a linha (1-10): ")) - 1
                    if coluna1 + tamanho > 10:
                        print("O barco foi posicionado inteiramente ou parcialmente fora da matriz")
                        continue
                    coluna2 = coluna1 + tamanho - 1
                    if colocar_barco(tabuleiro, linha, linha, coluna1, coluna2, "horizontal", tamanho):
                        contadores_local[escolha_tipo] -= 1
                        print("Barco posicionado com sucesso!")  # Feedback
                    else:
                        print("A posição do barco está conflitando com outro já colocado")
                        continue
                else:
                    print("Escolha de rotação inválida")

            except ValueError:
                print("Inserção inválida, use números inteiros")

            imprimir_tabuleiro(tabuleiro)

    def posicionar_barcos_computador(tabuleiro):
        contadores_local = contadores.copy()
        while any(contadores_local.values()):
            tipo = random.choice(list(contadores_local.keys()))
            if contadores_local[tipo] <= 0:
                continue

            tamanho = tipos_barcos[tipo]["tamanho"]
            orientacoes = ["vertical", "horizontal"]
            orientacao = random.choice(orientacoes)

            tentativas = 0
            while tentativas < 100:  # Limitar tentativas para evitar loops infinitos
                if orientacao == "vertical":
                    linha1 = random.randint(0, 10 - tamanho)
                    coluna = random.randint(0, 9)
                    linha2 = linha1 + tamanho - 1
                    if colocar_barco(tabuleiro, linha1, linha2, coluna, coluna, "vertical", tamanho):
                        contadores_local[tipo] -= 1
                        break  # Barco colocado com sucesso, sair do loop
                else:
                    coluna1 = random.randint(0, 10 - tamanho)
                    linha = random.randint(0, 9)
                    coluna2 = coluna1 + tamanho - 1
                    if colocar_barco(tabuleiro, linha, linha, coluna1, coluna2, "horizontal", tamanho):
                        contadores_local[tipo] -= 1
                        break  # Barco colocado com sucesso, sair do loop
                tentativas += 1
            if tentativas == 100:
                print(f"Não foi possível posicionar o barco do tipo {tipo} após 100 tentativas.")
                # Pode ser necessário reavaliar a lógica ou reiniciar o posicionamento

    def imprimir_tabuleiro(tabuleiro):
        print("  1 2 3 4 5 6 7 8 9 10")
        for i in range(10):
            print(chr(65 + i) + " " + " ".join(tabuleiro[i]))

    def atacar(tabuleiro, tabuleiro_ataques, linha, coluna):
        if tabuleiro[linha][coluna] == 'X' or tabuleiro[linha][coluna] == 'H':
            print("Acertou!")
            tabuleiro[linha][coluna] = 'H'  # H para Hit
            tabuleiro_ataques[linha][coluna] = 'H'
            return True
        else:
            print("Água!")
            tabuleiro[linha][coluna] = 'M'  # M para Miss
            tabuleiro_ataques[linha][coluna] = 'M'
            return False

    def ataque_jogador(tabuleiro_computador, tabuleiro_jogador_ataques):
        try:
            linha = input("Insira a linha para atacar (A-J): ").upper()
            coluna = int(input("Insira a coluna para atacar (1-10): ")) - 1

            if not ('A' <= linha <= 'J' and 0 <= coluna <= 9):
                print("Coordenadas inválidas.")
                return False

            linha_index = ord(linha) - ord('A')
            return atacar(tabuleiro_computador, tabuleiro_jogador_ataques, linha_index, coluna)

        except ValueError:
            print("Entrada inválida. Use uma letra de A a J para a linha e um número de 1 a 10 para a coluna.")
            return False

    def ataque_computador(tabuleiro_jogador, tabuleiro_computador_ataques):
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        print(f"O computador ataca {chr(65 + linha)}{coluna + 1}")
        return atacar(tabuleiro_jogador, tabuleiro_computador_ataques, linha, coluna)

    def verificar_vitoria(tabuleiro):
        for linha in tabuleiro:
            if 'X' in linha:
                return False
        return True

    # Preparação do jogo
    posicionar_barcos_jogador(tabuleiro_jogador)
    posicionar_barcos_computador(tabuleiro_computador)
    
    jogo_ativo = True
    while jogo_ativo:
        # Turno do Jogador
        print("\nSeu tabuleiro:")
        imprimir_tabuleiro(tabuleiro_jogador)
        print("\nSeus ataques:")
        imprimir_tabuleiro(tabuleiro_jogador_ataques)

        print("\nSua vez de atacar!")
        ataque_jogador(tabuleiro_computador, tabuleiro_jogador_ataques)

        # Verificar vitória do jogador
        if verificar_vitoria(tabuleiro_computador):
            print("Parabéns! Você venceu o computador!")
            print("Jogo feito por: \nFelipe Milicio\nGiovane Holanda\nMaria L. Batistel")
            jogo_ativo = False
            break

        # Turno do Computador
        print("\nVez do computador atacar...")
        ataque_computador(tabuleiro_jogador, tabuleiro_computador_ataques)

        # Verificar vitória do computador
        if verificar_vitoria(tabuleiro_jogador):
            print("O computador venceu!")
            jogo_ativo = False
            break

        print("\nTabuleiro do computador (para fins de depuração - REMOVER NA VERSÃO FINAL):") #apenas para teste
        imprimir_tabuleiro(tabuleiro_computador) #apenas para teste
        print("\nAtaques do computador:")
        imprimir_tabuleiro(tabuleiro_computador_ataques)

iniciar_batalha_naval()

