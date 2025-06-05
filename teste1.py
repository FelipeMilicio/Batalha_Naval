import random

matriz = []
valor = 'x'
contadorDestroier = 5
contadorSubamarino = 4
contadorContratorpedeiro = 3
contadorNavioTanque = 2
contadorPortaAvioes = 1

#gerar matriz
for i in range(5):
    lista = [' '] * 10
    matriz.append(lista)


escolha_tipo = int(input('Insira o tipo de barco que irá colocar: '))
escolha_rotacao = str(input('Insira a posição da rotação do barco: '))
if escolha_rotacao.lower() == 'vertical':
        pri_pos_linha = int(input('Escolha a linha de inicio do barco: '))
        seg_pos_linha = int(input('Escolha a linha do final do barco: '))
        coluna = int(input('Escolha a coluna a colocar o barco: '))
        resultado = pri_pos_linha - seg_pos_linha
def colocar_barco_vertical(matriz, linha1, linha2, coluna, valor):
    global contadorDestroier, contadorSubamarino, contadorContratorpedeiro, contadorNavioTanque, contadorPortaAvioes
    if escolha_tipo == 1:
        if contadorDestroier > 0:
            if linha1 == linha2:
                matriz[linha1][coluna] = (valor)
                contadorDestroier -= 1
            else:
                print('Posição inadequada para o tipo de barco')
        else:
            print("Quantidade do tipo de barco esgotada")

    maior_linha = max(linha1, linha2)
    if escolha_tipo == 2:
        if contadorSubamarino > 0:
            if resultado == 1 or resultado == -1:
                    matriz[linha1][coluna] = (valor)
                    matriz[linha2][coluna] = (valor)
                    for i in range(maior_linha):
                        matriz[(maior_linha - i)][coluna] = (valor)
                        contadorSubamarino -= 1
            else:
                print('Tamanho inválido')
        else:
             print('Quantidade do tipo de barco esgotada')

    if escolha_tipo == 3:
        if contadorContratorpedeiro > 0:
            if resultado == 2 or resultado == -2:
                    matriz[linha1][coluna] = (valor)
                    matriz[linha2][coluna] = (valor)
                    for i in range(maior_linha):
                        matriz[(maior_linha - i)][coluna] = (valor)
                        contadorContratorpedeiro -= 1
            else:
                print('Tamanho inválido')
        else:
             print('Quantidade do tipo de barco esgotada')
    
    if escolha_tipo == 4:
        if contadorNavioTanque > 0:
            if resultado == 3 or resultado == -3:
                    matriz[linha1][coluna] = (valor)
                    matriz[linha2][coluna] = (valor)
                    for i in range(maior_linha):
                        matriz[(maior_linha - i)][coluna] = (valor)
                        contadorNavioTanque -= 1
            else:
                print('Tamanho inválido')
        else:
             print('Quantidade do tipo de barco esgotada')

    if escolha_tipo == 5:
        if contadorPortaAvioes > 0:
            if resultado == 4 or resultado == -4:
                    matriz[linha1][coluna] = (valor)
                    matriz[linha2][coluna] = (valor)
                    for i in range(maior_linha):
                        matriz[(maior_linha - i)][coluna] = (valor)
                        contadorPortaAvioes -= 1
            else:
                print('Tamanho inválido')
        else:
             print('Quantidade do tipo de barco esgotada')


if escolha_rotacao.lower() == 'vertical':
    colocar_barco_vertical(matriz, pri_pos_linha, seg_pos_linha, coluna, valor)

for lista in matriz:
    print(lista)

# while True:
#     escolhaVertical = int(input('Escolha a coordenada y para atacar: '))
#     escolhaHorizontal = int(input('Escolha a coordenada x para atacar: '))

#     if matriz[escolhaVertical][escolhaHorizontal] == 'x':
#         matriz[escolhaVertical][escolhaHorizontal] = 'kaboom'

#     for lista in matriz:
#         print(lista)
