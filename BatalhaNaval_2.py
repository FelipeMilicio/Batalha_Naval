import random
import time
contador_vitorias_player = 0
contador_vitorias_bot = 0

def iniciar_batalha_naval():
    global contador_vitorias_bot, contador_vitorias_player
    def criar_tabuleiro():
        tabuleiro = []
        for i in range(10):
            linha = [' '] * 10
            tabuleiro.append(linha)
        return tabuleiro

    tabuleiro_jogador = criar_tabuleiro()
    tabuleiro_computador = criar_tabuleiro()
    tabuleiro_jogador_ataques = criar_tabuleiro()  # Para mostrar onde o jogador atacou o computador
    tabuleiro_computador_ataques = criar_tabuleiro()  # Para mostrar onde o computador atacou o jogador

    # dicionarios que definem os barcos e as suas quantidades
    tipos_barcos = {
        1: {"nome": "Destroier", "tamanho": 1},
        2: {"nome": "Submarino", "tamanho": 2},
        3: {"nome": "Contratorpedeiro", "tamanho": 3},
        4: {"nome": "Navio-Tanque", "tamanho": 4},
        5: {"nome": "Porta-Aviões", "tamanho": 5},
    }
    contadores = {
        1: 2,
        2: 2,
        3: 1,
        4: 1,
        5: 1,
    }

    # verificação de disponibilidade do espaço
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
                        matriz[i][j] = '-'
        elif orientacao == "horizontal":
            for i in range(max(0, linha1 - 1), min(10, linha1 + 2)):
                for j in range(max(0, coluna1 - 1), min(10, coluna2 + 2)):
                    if matriz[i][j] == ' ':
                        matriz[i][j] = '-'

    # def para colocar o barco
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
        print("\033[4:36m𝔹𝕒𝕥𝕒𝕝𝕙𝕒 ℕ𝕒𝕧𝕒𝕝\033[m")
        print("Na hora do ataque, o espaço será mudado para 'H' ou 'M'. A letra 'H' significa 'hit' ou 'acertou' e a letra 'M' significa 'miss' ou 'errou'.")
        print("Vamos colocar os seus barcos!")
        contadores_local = contadores.copy()  # Usar uma cópia para não alterar o original
        while any(contadores_local.values()):
            # pegar inputs do usuario e responder a algum erro
            try:
                print("\033[1:34m\nBarcos restantes:\033[m")
                for tipo, quantidade in contadores_local.items():
                    if quantidade > 0:
                        print(
                            f"{tipo} - {tipos_barcos[tipo]['nome']} (tamanho {tipos_barcos[tipo]['tamanho']}): {quantidade} restante(s)")
                escolha_tipo = int(input("\033[1:34m\nEscolha o tipo de barco (1-5): \033[m"))
                barco = tipos_barcos.get(escolha_tipo)
                if not barco:
                    print("\033[1:31m\nTipo de barco inválido\033[m")
                    time.sleep(1.5)
                    continue

                if contadores_local[escolha_tipo] <= 0:
                    print("\033[1:34m\nQuantidade deste tipo de barco esgotada\033[m")
                    time.sleep(1.5)
                    continue

                escolha_rotacao = str(input("\033[1:34mEscolha a rotação (vertical ou horizontal): \033[m")).lower()
                tamanho = barco["tamanho"]

                if escolha_rotacao == "vertical":
                    linha1 = int(input("\033[1:36mEscolha a linha inicial (1-10): \033[m")) - 1
                    coluna = int(input("\033[1:36mEscolha a coluna (1-10): \033[m")) - 1
                    if linha1 + tamanho > 10:
                        print("\033[1:31m\nO barco saiu da matriz\033[m")
                        time.sleep(1.5)
                        continue
                    linha2 = linha1 + tamanho - 1
                    if colocar_barco(tabuleiro, linha1, linha2, coluna, coluna, "vertical", tamanho):
                        contadores_local[escolha_tipo] -= 1
                        print("\033[1:34mBarco posicionado com sucesso!\033[m")  # Feedback
                        time.sleep(0.5)
                    else:
                        print("\033[1:31m\nA posição do barco está conflitando com outro já colocado\033[m")
                        time.sleep(1.5)
                        continue

                elif escolha_rotacao == "horizontal":
                    coluna1 = int(input("\033[1:36mEscolha a coluna (1-10): \033[m")) - 1
                    linha = int(input("\033[1:36mEscolha a linha inicial (1-10): \033[m")) - 1
                    if coluna1 + tamanho > 10:
                        print("O barco foi posicionado inteiramente ou parcialmente fora da matriz")
                        continue
                    coluna2 = coluna1 + tamanho - 1
                    if colocar_barco(tabuleiro, linha, linha, coluna1, coluna2, "horizontal", tamanho):
                        contadores_local[escolha_tipo] -= 1
                        print("\033[1:34mBarco posicionado com sucesso!\033[m")  # Feedback
                        time.sleep(0.5)
                    else:
                        print("\033[1:31m\nO barco foi posicionado inteiramente ou parcialmente fora da matriz\033[m")
                        time.sleep(1.5)
                        continue
                else:
                    print("\033[1:31m\nEscolha de rotação inválida\033[m")
                    time.sleep(1.5)

            except ValueError:
                print("\033[1:31m\nInserção inválida, use números inteiros\033[m")
                time.sleep(1.5)

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
                print(f"\033[1:31m\nNão foi possível posicionar o barco do tipo {tipo} após 100 tentativas.\033[m")
                # Pode ser necessário reavaliar a lógica ou reiniciar o posicionamento

    def imprimir_tabuleiro(tabuleiro):
        print("  1 2 3 4 5 6 7 8 9 10")
        for i in range(10):
            print(chr(65 + i) + " " + " ".join(tabuleiro[i]))

    def atacar(tabuleiro, tabuleiro_ataques, linha, coluna):
        if tabuleiro[linha][coluna] == 'X' or tabuleiro[linha][coluna] == 'H':
            print("\033[0:32mAcertou!\033[m")
            tabuleiro[linha][coluna] = 'H'  # H para Hit
            tabuleiro_ataques[linha][coluna] = 'H'
            return True
        else:
            print("\033[0:34mÁgua!\033[m")
            tabuleiro[linha][coluna] = 'M'  # M para Miss
            tabuleiro_ataques[linha][coluna] = 'M'
            return False

    def ataque_jogador(tabuleiro_computador, tabuleiro_jogador_ataques):
        try:
            linha = input("\033[1:36mInsira a linha para atacar (A-J): \033[m").upper()
            coluna = int(input("\033[1:36mInsira a coluna para atacar (1-10): \033[m")) - 1

            if not ('A' <= linha <= 'J' and 0 <= coluna <= 9):
                print("\033[1:31mCoordenadas inválidas.\033[m")
                time.sleep(1.5)
                return False

            linha_index = ord(linha) - ord('A')
            if tabuleiro_jogador_ataques[linha_index][coluna] in ['H', 'M']:
                print("Você já atacou aqui!")
                time.sleep(1.5)
                return False

            return atacar(tabuleiro_computador, tabuleiro_jogador_ataques, linha_index, coluna)

        except ValueError:
            print("\033[1:31mEntrada inválida. Use uma letra de A a J para a linha e um número de 1 a 10 para a coluna.\033[m")
            time.sleep(1.5)
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
        print("\033[1:34m\nSeu tabuleiro:\033[m")
        imprimir_tabuleiro(tabuleiro_jogador)
        print("\033[1:31m\nSeus ataques:\033[m")
        imprimir_tabuleiro(tabuleiro_jogador_ataques)
        
        print('\nTabuleiro do pc):')
        imprimir_tabuleiro(tabuleiro_computador)
        
        print("\033[4:36m\nSua vez de atacar!\033[m")
        ataque_jogador(tabuleiro_computador, tabuleiro_jogador_ataques)

        # Verificar vitória do jogador
        if verificar_vitoria(tabuleiro_computador):
            contador_vitorias_player += 1
            print("\033[4:35mParabéns! Você venceu o computador!\033[m")
            print("\033[0:35mJogo feito por: \nFelipe Milicio\nGiovane Holanda\nMaria L. Batistel\033[m")
            return

        # Turno do Computador
        print("\033[4:36m\nVez do computador atacar...\033[m")
        ataque_computador(tabuleiro_jogador, tabuleiro_computador_ataques)

        # Verificar vitória do computador
        if verificar_vitoria(tabuleiro_jogador):
            contador_vitorias_bot += 1
            print("\033[4:35mO computador venceu!\033[m")
            return
        
# loop de partidas
def loop_jogo():
    while True:
        iniciar_batalha_naval()
        print(f"O placar está Jogador: {contador_vitorias_player}, Computador: {contador_vitorias_bot}.")
        resposta = input("Deseja jogar novamente? (1-Sim, 2-Não): ")
        if resposta != "1":
            break

loop_jogo()
