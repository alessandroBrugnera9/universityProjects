"""
  AO PREENCHER ESSE CABEÃ‡ALHO COM O MEU NOME E O MEU NÃšMERO USP,
  DECLARO QUE SOU A ÃšNICA PESSOA AUTORA E RESPONSÃVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÃCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÃ‡Ã•ES
  DESSE EP E, PORTANTO, NÃƒO CONSTITUEM ATO DE DESONESTIDADE ACADÃŠMICA,
  FALTA DE Ã‰TICA OU PLÃGIO.
  DECLARO TAMBÃ‰M QUE SOU A PESSOA RESPONSÃVEL POR TODAS AS CÃ“PIAS
  DESSE PROGRAMA E QUE NÃƒO DISTRIBUÃ OU FACILITEI A
  SUA DISTRIBUIÃ‡ÃƒO. ESTOU CIENTE QUE OS CASOS DE PLÃGIO E
  DESONESTIDADE ACADÃŠMICA SERÃƒO TRATADOS SEGUNDO OS CRITÃ‰RIOS
  DIVULGADOS NA PÃGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃƒO SERÃƒO CORRIGIDOS E,
  AINDA ASSIM, PODERÃƒO SER PUNIDOS POR DESONESTIDADE ACADÃŠMICA.

  Nome : Alessandro Brugnera Silva
  NUSP : 10334040
  Turma: 10
  Prof.: Alan Durhan

  ReferÃªncias: Com exceÃ§Ã£o das rotinas fornecidas no enunciado
  e em sala de aula, caso vocÃª tenha utilizado alguma referÃªncia,
  liste-as abaixo para que o seu programa nÃ£o seja considerado
  plÃ¡gio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""
# ======================================================================
#
#   FUNÃ‡Ã•ES FORNECIDAS: NÃƒO DEVEM SER MODIFICADAS
#
# ======================================================================
import random
random.seed(0)

def main():
    '''
    Esta Ã© a funÃ§Ã£o principal do seu programa. Ela contÃ©m os comandos que
    obtÃªm os parÃ¢metros necessÃ¡rios para criaÃ§Ã£o do jogo (nÃºmero de linhas,
    colunas e cores), e executa o laÃ§o principlal do jogo: ler comando,
    testar sua validade e executar comando.

    ******************************************************
    ** IMPORTANTE: ESTA FUNÃ‡ÃƒO NÃƒO DEVE SER MODIFICADA! **
    ******************************************************
    '''
    print()
    print("=================================================")
    print("             Bem-vindo ao Gemas!                 ")
    print("=================================================")
    print()

    pontos = 0
    # lÃª parÃ¢metros do jogo
    num_linhas = int(input("Digite o nÃºmero de linhas [3-10]: ")) # exemplo: 8
    num_colunas = int(input("Digite o nÃºmero de colunas [3-10]: ")) # exemplo: 8
    num_cores = int(input("Digite o nÃºmero de cores [3-26]: ")) # exemplo: 7
    # cria tabuleiro com configuraÃ§Ã£o inicial
    tabuleiro = criar (num_linhas, num_colunas)
    completar (tabuleiro, num_cores)
    num_gemas = eliminar (tabuleiro)
    while num_gemas > 0:
        deslocar (tabuleiro)
        completar (tabuleiro, num_cores)
        num_gemas = eliminar (tabuleiro)
    # laÃ§o principal do jogo
    while existem_movimentos_validos (tabuleiro): # Enquanto houver movimentos vÃ¡lidos...
        exibir (tabuleiro)
        comando = input("Digite um comando (perm, dica, sair ou ajuda): ")
        if comando == "perm":
            linha1 = int(input("Digite a linha da primeira gema: "))
            coluna1 = int(input("Digite a coluna da primeira gema: "))
            linha2 = int(input("Digite a linha da segunda gema: "))
            coluna2 = int(input("Digite a coluna da segunda gema: "))
            print ()
            valido = trocar ( linha1, coluna1, linha2, coluna2, tabuleiro)
            if valido:
                num_gemas = eliminar (tabuleiro)
                total_gemas = 0
                while num_gemas > 0:
                    # Ao destruir gemas, as gemas superiores sÃ£o deslocadas para "baixo",
                    # criando a possibilidade de que novas cadeias surjam.
                    # Devemos entÃ£o deslocar gemas e destruir cadeias enquanto houverem.
                    deslocar (tabuleiro)
                    completar (tabuleiro, num_cores)
                    total_gemas += num_gemas
                    print("Nesta rodada: %d gemas destruidas!" % num_gemas )
                    exibir (tabuleiro)
                    num_gemas = eliminar (tabuleiro)
                pontos += total_gemas
                print ()
                print ("*** VocÃª destruiu %d gemas! ***" % (total_gemas))
                print ()
            else:
                print ()
                print ("*** Movimento invÃ¡lido! ***")
                print ()
        elif comando == "dica":
            pontos -= 1
            linha, coluna = obter_dica (tabuleiro)
            print ()
            print ("*** Dica: Tente permutar a gema na linha %d e coluna %d ***" % (linha, coluna))
            print ()
        elif comando == "sair":
            print ("Fim de jogo!")
            print ("VocÃª destruiu um total de %d gemas" % (pontos))
            return
        elif comando == "ajuda":
            print("""
============= Ajuda =====================
perm:  permuta gemas
dica:  solicita uma dica (perde 1 ponto)
sair:  termina o jogo
=========================================
                  """)
        else:
            print ()
            print ("*** Comando invÃ¡lido! Tente ajuda para receber uma lista de comandos vÃ¡lidos. ***")
            print ()
    print("*** Fim de Jogo: NÃ£o existem mais movimentos vÃ¡lidos! ***")
    print ("VocÃª destruiu um total de %d gemas" % (pontos))

def completar (tabuleiro, num_cores):
    ''' (matrix, int) -> None

    Preenche espaÃ§os vazios com novas gemas geradas aleatoriamente.

    As gemas sÃ£o representadas por strings 'A','B','C',..., indicando sua cor.
    '''
    alfabeto = ['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num_linhas = len (tabuleiro)
    num_colunas = len (tabuleiro[0])
    for i in range (num_linhas):
        for j in range (num_colunas):
            if tabuleiro[i][j] == ' ':
                gema = random.randrange (num_cores)
                tabuleiro[i][j] = alfabeto[gema]



# ======================================================================
#
#   FUNÃ‡Ã•ES A SEREM IMPLEMENTADAS POR VOCÃŠ
#
# ======================================================================

def criar (num_linhas, num_colunas):
    ''' (int,int) -> matrix

    Cria matriz de representaÃ§Ã£o do tabuleiro e a preenche com
    espaÃ§os vazios representados por ' '.

    Retorna a matriz criada.
    '''
    matriz = []
    vazio = " "
    parcial=[]

    for i in range(num_linhas):
        for j in range(num_colunas):
            parcial.append(vazio)
        matriz.append(parcial)
        parcial=[]

    return matriz

def exibir (tabuleiro):
    ''' (matrix) -> None

    Exibe o tabuleiro.
    '''
    print("    ", end="")
    for j in range(len(tabuleiro[0])):
        print(j, end="")
        print(" ", end="")
    print()

    print("  ", end="")
    print("+", end="")
    for j in range(len(tabuleiro[0])*2+1):
        print("-", end="")
    print("+", end="")
    print()

    for i in range(len(tabuleiro)):
        print(i, end="")
        print(" ", end="")
        print("|", end="")
        for j in range(len(tabuleiro[0])):
            print(" ", end="")
            print(tabuleiro[i][j], end="")
        print(" ", end="")
        print("|", end="")
        print()

    print("  ", end="")
    print("+", end="")
    for j in range(len(tabuleiro[0])*2+1):
        print("-", end="")
    print("+", end="")
    print()

def trocar (linha1, coluna1, linha2, coluna2, tabuleiro):
    ''' (int,int,int,int,matrix) -> Bool

    Permuta gemas das posiÃ§Ãµes (linha1, coluna1) e (linha2, coluna2) caso
    seja vÃ¡lida (isto Ã©, gemas sÃ£o adjacentes e geram cadeias), caso contrÃ¡rio
    nÃ£o altera o tabuleiro.

    Retorna `True` se permutaÃ§Ã£o Ã© vÃ¡lida e `False` caso contrÃ¡rio.
    '''

    if linha1==linha2:
        if coluna1==coluna2+1 or coluna1+1==coluna2:
            valor=tabuleiro[linha1][coluna1]
            tabuleiro[linha1][coluna1]=tabuleiro[linha1][coluna2]
            tabuleiro[linha1][coluna2]=valor
            if identificar_cadeias_horizontais(tabuleiro)!=[] or identificar_cadeias_verticais(tabuleiro)!=[]:
                return True
            else:
                valor=tabuleiro[linha1][coluna1]
                tabuleiro[linha1][coluna1]=tabuleiro[linha1][coluna2]
                tabuleiro[linha1][coluna2]=valor
                return False

    elif coluna1==coluna2:
        if linha1==linha2+1 or linha1+1==linha2:
            valor=tabuleiro[linha1][coluna1]
            tabuleiro[linha1][coluna1]=tabuleiro[linha2][coluna1]
            tabuleiro[linha2][coluna1]=valor
            if identificar_cadeias_horizontais(tabuleiro)!=[] or identificar_cadeias_verticais(tabuleiro)!=[]:
                return True
            else:
                valor=tabuleiro[linha1][coluna1]
                tabuleiro[linha1][coluna1]=tabuleiro[linha2][coluna1]
                tabuleiro[linha2][coluna1]=valor
                return False
    else:
        return False


def eliminar (tabuleiro):
    ''' (matrix) -> int

    Elimina cadeias de 3 ou mais gemas, substituindo-as por espaÃ§os (' ').

    Retorna nÃºmero de gemas eliminadas.
    '''
    num_eliminados = 0

    horizontal = identificar_cadeias_horizontais(tabuleiro)
    vertical = identificar_cadeias_verticais(tabuleiro)

    hor=len(horizontal)
    ver=len(vertical)

    for h in range(hor):
        num_eliminados+=eliminar_cadeia(tabuleiro, horizontal[h])

    for v in range(ver):
        num_eliminados+=eliminar_cadeia(tabuleiro, vertical[v])

    return num_eliminados

def identificar_cadeias_horizontais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias horizontais de 3 ou mais gemas. Cada cadeia Ã©
    representada por uma lista `[linha, coluna_i, linha, coluna_f]`, onde:

    - `linha`: o nÃºmero da linha da cadeia
    - `coluna_i`: o nÃºmero da coluna da gema mais Ã  esquerda (menor) da cadeia
    - `coluna_f`: o nÃºmero da coluna da gema mais Ã  direita (maior) da cadeia

    NÃ£o modifica o tabuleiro.
    '''
    cadeias = []
    parcial=[]
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])


    for i in range(num_linhas):
        parcial = tabuleiro[i]
        coluna_f = -1

        for j in range(num_colunas-2):
            if coluna_f<j and j+1<num_colunas and j+2<num_colunas:

                if parcial[j]==parcial[j+1]==parcial[j+2]:
                    coluna_f=j+2
                    if j+3<num_colunas:
                        if parcial[j+2]==parcial[j+3]:
                            rangee = range(num_colunas)
                            comparador=rangee[j+2:]
                            for p in comparador:
                                if parcial[j+2]==parcial[p]:
                                    coluna_f=p

                    caso=[i,j,i,coluna_f]
                    cadeias.append(caso)
                    caso=[]


    return cadeias

def identificar_cadeias_verticais (tabuleiro):
    ''' (matrix) -> list

    Retorna uma lista contendo cadeias verticais de 3 ou mais gemas. Cada cadeia Ã©
    representada por uma lista `[linha_i, coluna, linha_f, coluna]`, onde:

    - `linha_i`: o nÃºmero da linha da gemas mais superior (menor) da cadeia
    - `coluna`: o nÃºmero da coluna das gemas da cadeia
    - `linha_f`: o nÃºmero da linha mais inferior (maior) da cadeia

    NÃ£o modifica o tabuleiro.
    '''
    cadeias = []
    parcial=[]
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])

    for j in range(num_colunas):
        linha_f = -1
        for i in range(num_linhas):
            if linha_f<i and i+1<num_linhas and i+2<num_linhas:

                if tabuleiro[i][j]==tabuleiro[i+1][j]==tabuleiro[i+2][j]:
                    linha_f=i+2
                    if i+3<num_linhas:
                        if tabuleiro[i+2][j]==tabuleiro[i+3][j]:
                            rangee = range(num_linhas)
                            comparador=rangee[i+2:]
                            for p in comparador:
                                if tabuleiro[i+2][j]==tabuleiro[p][j]:
                                    linha_f=p

                    caso=[i,j,linha_f,j]
                    cadeias.append(caso)
                    caso=[]

    return cadeias

def eliminar_cadeia (tabuleiro, cadeia):
    ''' (matrix,list) -> int

    Elimina (substitui pela string espaÃ§o `" "`) as gemas compreendidas numa cadeia,
    representada por uma lista `[linha_inicio, coluna_inicio, linha_fim, coluna_fim]`,
    tal que:

    - `linha_i`: o nÃºmero da linha da gema mais superior (menor) da cadeia
    - `coluna_i`: o nÃºmero da coluna da gema mais Ã  esquerda (menor) da cadeia
    - `linha_f`: o nÃºmero da linha mais inferior (maior) da cadeia
    - `coluna_f`: o nÃºmero da coluna da gema mais Ã  direita (maior) da cadeia

    Retorna o nÃºmero de gemas eliminadas.
    '''
    num_eliminados = 0
    if cadeia[2]==cadeia[0]:
        linhas=[cadeia[2]]
    else:
        linhas=range(cadeia[2]+1)
        linhas=linhas[cadeia[0]:]

    if cadeia[3]==cadeia[1]:
        colunas=[cadeia[3]]
    else:
        colunas=range(cadeia[3]+1)
        colunas=colunas[cadeia[1]:]

    for i in linhas:
        for j in colunas:
            if tabuleiro[i][j]!=" ":
                tabuleiro[i][j]=" "
                num_eliminados+=1

    return num_eliminados

def deslocar (tabuleiro):
    ''' (matrix) -> None

    Desloca gemas para baixo deixando apenas espaÃ§os vazios sem nenhuma gema acima.
    '''
    #
    lista_de_vazios=[]
    for j in range(len(tabuleiro)):
        for i in range(len(tabuleiro[0])):
            if tabuleiro[i][j]==" ":
                lista_de_vazios.append(j)


    for d in range(len(lista_de_vazios)):
        deslocar_coluna(tabuleiro,lista_de_vazios[d])

def deslocar_coluna ( tabuleiro, i ):
    ''' (matrix, int) -> None

    Desloca as gemas na coluna i para baixo, ocupando espaÃ§os vazios.
    '''
    #
    linha=-1
    for l in range(len(tabuleiro[0])):
        if tabuleiro[l][i]==" ":
            if l!=0 and tabuleiro[l-1][i]!=" ":
                linha=l
                break

    if linha==-1:
        return

    linha=reversed(range(linha))
    for lin in linha:
        w=0
        while tabuleiro[lin-w][i]==" " :
            if lin-w==0:
                break
            w+=1
        tabuleiro[lin+1][i]=tabuleiro[lin-w][i]

    tabuleiro[0][i]=" "

def existem_movimentos_validos (tabuleiro):
    '''(matrix) -> Bool

    Retorna True se houver movimentos vÃ¡lidos, False caso contrÃ¡rio.
    '''
    linha, coluna = obter_dica (tabuleiro)

    if linha==-1:
        return False
    else:
        return True

def obter_dica (tabuleiro):
    '''(matrix) -> int,int

    Retorna a posiÃ§Ã£o (linha, coluna) de uma gema que faz parte de uma
    permutaÃ§Ã£o vÃ¡lida.

    Se nÃ£o houver permutaÃ§Ã£o vÃ¡lida, retorne -1,-1.
    '''
    linha = -1
    coluna = -1

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if j!=len(tabuleiro[0])-1: #direita
                valor=tabuleiro[i][j]
                tabuleiro[i][j]=tabuleiro[i][j+1]
                tabuleiro[i][j+1]=valor
                if identificar_cadeias_horizontais(tabuleiro)!=[] or identificar_cadeias_verticais(tabuleiro)!=[]:
                    valor=tabuleiro[i][j]
                    tabuleiro[i][j]=tabuleiro[i][j+1]
                    tabuleiro[i][j+1]=valor                   
                    return i, j

                valor=tabuleiro[i][j]
                tabuleiro[i][j]=tabuleiro[i][j+1]
                tabuleiro[i][j+1]=valor

            if i!=0: #esquerda
                valor=tabuleiro[i][j]
                tabuleiro[i][j]=tabuleiro[i-1][j]
                tabuleiro[i-1][j]=valor
                if identificar_cadeias_horizontais(tabuleiro)!=[] or identificar_cadeias_verticais(tabuleiro)!=[]:
                    valor=tabuleiro[i][j]
                    tabuleiro[i][j]=tabuleiro[i-1][j]
                    tabuleiro[i-1][j]=valor
                    return i, j

                valor=tabuleiro[i][j]
                tabuleiro[i][j]=tabuleiro[i-1][j]
                tabuleiro[i-1][j]=valor

            if i!=len(tabuleiro)-1: #abaixo
                valor=tabuleiro[i][j]
                tabuleiro[i][j]=tabuleiro[i+1][j]
                tabuleiro[i+1][j]=valor
                if identificar_cadeias_horizontais(tabuleiro)!=[] or identificar_cadeias_verticais(tabuleiro)!=[]:
                    valor=tabuleiro[i][j]
                    tabuleiro[i][j]=tabuleiro[i+1][j]
                    tabuleiro[i+1][j]=valor
                    return i, j

                valor=tabuleiro[i][j]
                tabuleiro[i][j]=tabuleiro[i+1][j]
                tabuleiro[i+1][j]=valor

            if i!=0: # a cima
                valor=tabuleiro[i][j]
                tabuleiro[i][j]=tabuleiro[i-1][j]
                tabuleiro[i-1][j]=valor
                if identificar_cadeias_horizontais(tabuleiro)!=[] or identificar_cadeias_verticais(tabuleiro)!=[]:
                    valor=tabuleiro[i][j]
                    tabuleiro[i][j]=tabuleiro[i-1][j]
                    tabuleiro[i-1][j]=valor
                    return i, j

                valor=tabuleiro[i][j]
                tabuleiro[i][j]=tabuleiro[i-1][j]
                tabuleiro[i-1][j]=valor

    return linha, coluna


main()
