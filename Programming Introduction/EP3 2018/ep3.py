# -*- coding: latin-1 -*-
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

  Nome : 
  NUSP : 
  Turma: 
  Prof.: 

  ReferÃªncias: Com exceÃ§Ã£o das rotinas fornecidas no enunciado
  e em sala de aula, caso vocÃª tenha utilizado alguma referÃªncia,
  liste-as abaixo para que o seu programa nÃ£o seja considerado
  plÃ¡gio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""

# **********************************************************
# **                 INÃCIO DA PARTE 1                    **
# **********************************************************


def calcula_id(matriz):
    """ Retorna o valor de identificaÃ§Ã£o de uma matriz computada pelo
    algoritmo adler32

    A funÃ§Ã£o :func:'calcula_id' computa um identificador para uma matriz
    usando a seguinte versÃ£o adaptada do algoritmo de espalhamento Adler32:

        - A = 1 + matriz[0][0] + matriz[0][1] +...+ matriz[m-1][n-1] MOD 65521,
            onde m Ã© o nÃºmero de linhas e n Ã© o nÃºmero de colunas da matriz
        - B = (1 + matriz[0][0]) + (1 + matriz[0][0]+matriz[0][1]) + ... +
          (1 + matriz[0][0] + matriz[0][1] + ... + matriz[m-1][n-1]) MOD 65521
        - retorna B * (2**16) + A


    :param matriz: Uma matriz de inteiros
    :type matriz: <class 'list'>
    :return identificador: O identificador inteiro da matriz computado segundo
        a nossa versÃ£o adaptada do Adler32
    :rtype: <class 'int'>

    :Examples:

    >>> matriz_A = [[0,1,2], [3,4,5]]
    >>> matriz_B = [[3,4,5], [0,1,2]]
    >>> matriz_C = [[0,1], [1,0]]
    >>> matriz_D = [[1,0,2], [3,4,5]]
    >>> calcula_id(matriz_A)
    2686992
    >>> calcula_id(matriz_B)
    4456464
    >>> calcula_id(matriz_C)
    589827
    >>> calcula_id(matriz_D)
    2752528

    .. seealso::
        Consulte o enunciado para um exemplo mais detalhado.
    """
    A = 1
    B = 0

    #percorre a matriz
    for j in range(len(matriz)):
        for i in range(len(matriz[0])):
            A += matriz[j][i]
            B += A
    A = A % 65521
    B = B % 65521

    identificador=B * (2**16) + A

    return(B * (2**16) + A)



# ----------------------------------------------------------
# --                  FIM DA PARTE 1                      --
# ----------------------------------------------------------


# **********************************************************
# **                 INÃCIO DA PARTE 2                    **
# **********************************************************


def carrega_identificador(nome_arquivo):
    """ Carrega o identificador de uma imagem presente em um arquivo.

    A funÃ§Ã£o :func:'carrega_identificador' abre um arquivo de nome
    'nome_arquivo' presente na mesma pasta que o programa ep3.py, lÃª sua
    primeira linha e retorna o inteiro representando o identificador  
    presente nessa linha.

    :param nome_arquivo: String com o nome do arquivo com o identificador
    :type nome_arquivo: <class 'str'>
    :return identificador: Inteiro contendo identificador 
    :rtype: <class 'int'>

    :Example:

    >>> identificador = carrega_identificador('img01.adler32')
    >>> print(identificador)
    297286
    

    .. note::
        Embora pelas regras da disciplina vocÃª possa assumir que o arquivo
        'nome_arquivo' estÃ¡ presente na mesma pasta do programa ep3.py,
        boas prÃ¡ticas de programaÃ§Ã£o sugerem que para escrita e leitura de
        arquivos, vocÃª sempre deve verificar Ã  existÃªncia/permissÃµes.
        Com relaÃ§Ã£o ao identificador, vocÃª pode assumir que o arquivo contÃ©m
        um identificador vÃ¡lido na primeira linha.
    """
    arquivo=open(nome_arquivo, "r")
    linha=arquivo.readline()
    linha=linha.strip()

    arquivo.close()
    return(int(linha))



def carrega_imagem(nome_imagem):
    """ Carrega do arquivo 'nome_imagem' uma imagem em formato PGM do tipo P2 e
    retorna Ã  imagem em formato de matriz de pixels.

    A funÃ§Ã£o :func:'carrega_imagem' lÃª uma imagem em formato PGM do tipo P2
    presente em um arquivo na mesma pasta do programa ep3.py e retorna uma
    matriz de inteiros de tamanho N-por-M, onde N Ã© a altura da imagem, e M Ã©
    largura da imagem, ambos medidos em pixels e obtidos atravÃ©s do cabeÃ§alho
    da imagem.

    :param nome_imagem: String com o nome de imagem na mesma pasta de ep3.py
    :type nome_imagem: <class 'str'>
    :return matriz: Matriz de inteiros representando os pixels da imagem
    :rtype: <class 'list'>

    :Example:

    >>> A = carrega_imagem('imagem.pgm')
    >>> print(A)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    .. seealso::
        Vide enunciado para uma explicaÃ§Ã£o mais detalhada acerca do formato PGM
    .. note::
        VocÃª pode assumir que a imagem estÃ¡ no formato correto e que o valor
        da intensidade de cada pixel Ã© um inteiro entre 0 e 255 (inclusive).
    """
    arquivo=open(nome_imagem, "r")
    arquivo.readline()
    #informacoes inicias
    linha=arquivo.readline()
    linha=linha.strip()
    numeros=linha.split(" ")
    colunas=int(numeros[0])
    linhas=int(numeros[1])

    linha=arquivo.readline()
    linha=linha.strip()
    numeros=linha.split(" ")
    valor_maximo=int(numeros[0])

    #leitura para montar matriz
    linha_da_matriz=[]
    matriz=[]
    for linha in arquivo:
        linha=linha.strip()
        numeros=linha.split(" ")
        if len(numeros)==colunas:
            for numero in numeros:
                linha_da_matriz.append(int(numero))
            matriz.append(linha_da_matriz)
            linha_da_matriz=[]

    arquivo.close()
    return(matriz)


def salva_imagem(nome_arquivo, matriz):
    """ Cria (se nÃ£o existir) e escreve a imagem representada pela matriz no
    arquivo de nome nome_arquivo no formato PGM (tipo 2).

    A funÃ§Ã£o :func:'salva_imagem' recebe uma matriz de inteiros (0-255)
    representando uma imagem em tons de cinza e salva essa imagem no arquivo
    'nome_arquivo' no formato Portable GrayMap (PGM) do tipo P2 na mesma pasta.


    :param nome_arquivo: String contendo o nome de um arquivo (ex.'imagem.ppm')
    :param matriz: Matriz de inteiros representando uma imagem em tons de cinza
    :type nome_arquivo: <class 'str'>
    :type matriz: <class 'list'>

    :Example:

    >>> M = carrega_imagem('imagem.pgm')
    >>> print(M)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    >>> M[0][0] = 255
    >>> print(M)
    [[255, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    >>> salva_imagem('nova_imagem.pgm', M)

    .. seealso::
        Consulte o enunciado para informaÃ§Ãµes especÃ­ficas do formato PGM tipo 2
    """
    arquivo=open(nome_arquivo, "w")
    arquivo.write("P2\n")
    linhas=len(matriz)
    colunas=len(matriz[0])
    arquivo.write(str(colunas)+ " "+ str(linhas)+"\n")
    arquivo.write("255\n")
    for i in range(linhas):
        for j in range(colunas):
            arquivo.write(str(matriz[i][j])+ " ")
        arquivo.write("\n")

    arquivo.close()
    return()


def carrega_transforma��es(nome_arquivo):
    """Carrega transformaÃ§Ãµes de um arquivo de texto.

    A funÃ§Ã£o :func:'carrega_transformaÃ§Ãµes' recebe uma string com o nome de um
    arquivo presente na mesma pasta do programa ep3.py que contÃ©m as matrizes
    de transformaÃ§Ã£o.
    Neste arquivo:

        - A primeira linha representa o nÃºmero total de transformaÃ§Ãµes
        - Todas as outras linhas trazem ou transformaÃ§Ãµes ou comentÃ¡rios

    Uma linha comeÃ§ando com # indica um comentÃ¡rio e deve ser ignorada.
    Todas as outras linhas representam matrizes 2-por-3 de modo que a matriz
    inteira estÃ¡ representada em uma Ãºnica linhado arquivo e cada elemento da
    matriz Ã© separado por um (ou mais) espaÃ§os.
    O exemplo abaixo mostra o conteÃºdo de um possÃ­vel arquivo de transformaÃ§Ãµes

    **Exemplo de arquivo de transformaÃ§Ãµes**:
    2
    # Meu conjunto de transformaÃ§Ãµes
    # transformaÃ§Ã£o identidade
    1 0 0 0 1 0
    # espelhamento
    -1 0 0 0 -1 0


    :param nome_arquivo: String com nome de um arquivo texto contendo as
        transformaÃ§Ãµes
    :type nome_arquivo: <class 'str'>
    :return lista: Uma lista de matrizes de transformaÃ§Ã£o
    :rtype: <class 'list'>

    :Example:

    >>> transformaÃ§Ãµes = carrega_transformaÃ§Ãµes('duas_transformaÃ§Ãµes.txt')
    >>> print(transformaÃ§Ãµes)
    [[[1, 0, -20], [0, 1, -20]], [[1, 0, 0], [0, 1, 0]]]

    .. seealso::
        Veja o enunciado para maiores detalhes da estrutura desse arquivo.
    .. note::
        VocÃª pode considerar que o arquivo de transformaÃ§Ãµes sÃ³ contÃ©m os
        trÃªs tipos de linhas mencionados (nÃºmero total de transformaÃ§Ãµes,
        comentÃ¡rios e transformaÃ§Ãµes), vocÃª nÃ£o precisa tratar outros formatos.
    """
    arquivo=open(nome_arquivo, "r")
    matrizes=[]

    for linha in arquivo:
        if linha[0]!="#" and len(linha)>3:
            linha=linha.strip()
            numeros=linha.split(" ")
            linha_da_matriz=[]
            matriz=[]
            contador=0

            for  i in range(2):
                for j in range(3):
                    linha_da_matriz.append(int(numeros[contador]))
                    contador+=1
                matriz.append(linha_da_matriz)
                linha_da_matriz=[]
            matrizes.append(matriz)

    arquivo.close()
    return(matrizes)


# ----------------------------------------------------------
# --                  FIM DA PARTE 2                      --
# ----------------------------------------------------------


# **********************************************************
# **                 INÃCIO DA PARTE 3                    **
# **********************************************************

def transforma(matriz, T):
    """ Devolve uma transformaÃ§Ã£o geomÃ©trica linear da matriz.

    A funÃ§Ã£o :func:'transforma' recebe uma matriz de pixels e uma transformaÃ§Ã£o
    afim representada matricialmente e retorna a matriz transformada, **sem**
    modificar a matriz original.


    :param matriz: Matriz representando imagem em tons de cinza (0-255)
    :param transformaÃ§Ã£o: Matriz 2-por-3 representando transformaÃ§Ã£o linear
    :type matriz: <class 'list'>
    :type transformaÃ§Ã£o: <class 'list'>
    :return matriz_transformada: Matriz resultado da transformaÃ§Ã£o aplicada
        sobre todos os pontos
    :rtype: <class 'list'>

    :Example:

    >>> matriz1 = [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> translaÃ§Ã£o_diagonal_por_1_pixel = [[1, 0, 1], [0, 1, 1], [0, 0, 1]]
    >>> matriz2 = transforma(matriz1, translaÃ§Ã£o_diagonal_por_1_pixel)
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz2)
    [[6, 4, 5], [3, 1, 2]]

    .. seealso::
        Vide enunciado para maiores exemplos da aplicaÃ§Ã£o dessa transformaÃ§Ã£o

    .. note::
        VocÃª pode assumir que sÃ³ serÃ£o utilizadas transformaÃ§Ãµes inversÃ­veis
        cujos coeficientes sÃ£o inteiros.
    """
    linhas=len(matriz)
    colunas=len(matriz[0])
    transformada=[]
    linha=[]
    variavel=0

    #craiacao da matriz com valor qualquer
    for j in range(linhas):
        for i in range(colunas):
            linha.append(variavel)
        transformada.append(linha)
        linha=[]

    #transformacao
    for j in range(linhas):
        for i in range(colunas):
            #x linha
            parte1=T[0][0]*i
            parte2=T[0][1]*j
            parte3=T[0][2]
            soma=parte1+parte2+parte3
            x=soma%colunas

            #y linha
            parte1=T[1][0]*i
            parte2=T[1][1]*j
            parte3=T[1][2]
            soma=parte1+parte2+parte3
            y=soma%linhas

            #colocando valor
            transformada[y][x]=matriz[j][i]

    return(transformada)


# ----------------------------------------------------------
# --                  FIM DA PARTE 3                      --
# ----------------------------------------------------------


# **********************************************************
# **                 INÃCIO DA PARTE 4                    **
# **********************************************************


def busca(matriz, transforma��es, identifica��o, max_transfs):
    """ Busca imagem com identificaÃ§Ã£o dada usando no mÃ¡ximo um conjunto de
    max_transfs transformaÃ§Ãµes.

    A funÃ§Ã£o :func:'busca' recebe uma matriz representando uma imagem
    monocromÃ¡tica, uma lista de transformaÃ§Ãµes possÃ­veis, um identificador
    correspondente Ã  dispersÃ£o criptogrÃ¡fica da imagem original e o valor do
    nÃºmero mÃ¡ximo de transformaÃ§Ãµes em sequencia Ã  serem realizadas sobre Ã 
    matriz nessa busca e devolve:

        - A matriz da imagem original (caso encontrada) OU
        - None (caso contrÃ¡rio)

    :param matriz: Uma matriz de inteiros representando uma imagem
    :transformaÃ§Ãµes: Uma lista de matrizes de transformaÃ§Ã£o
    :identificaÃ§Ã£o: Uma string com o identificador da imagem original
    :max_transfs: NÃºmero mÃ¡ximo de sequencias de transformaÃ§Ãµes Ã  testar
    :type matriz: <class 'list'>
    :type transformaÃ§Ãµes: <class 'list'>
    :type identificaÃ§Ã£o: <class 'int'>
    :type max_transfs: <class 'int'>
    :return resultado: Matriz com imagem restaurada ou None se ela nÃ£o for
        encontrada.
    :rtype: <class 'list'> OU <class 'NoneType'>

    :Example:

    >>> original = [[1,2,3], [4,5,6], [7,8,9]]
    >>> identificador = calcula_id(imagem)
    >>> print(identificador)
    11403310
    >>> nova = transforma(imagem, [[1,0,1], [0,1,0]]) # Aplica desloc em eixo x
    >>> print(nova)
    [[3, 1, 2], [6, 4, 5], [9, 7, 8]]
    >>> nova2 = transforma(nova, [[1,0,1], [0,1,1]]) # Aplica Desloc x+1 e y+1
    >>> print(nova2)
    [[8, 9, 7], [2, 3, 1], [5, 6, 4]]
    >>> transfs = [[[1,0,-1], [0,1,0]], [[1,0,-1],[0,1,-1]], [[1,0,1],[0,1,1]]]
    >>> resultado = busca(nova2, transfs, identificador, 2)
    >>> print(resultado)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> resultado2 = busca(nova2, transfs, identificador, 1)
    >>> print(resultado2)
    None
    """

    if calcula_id(matriz)==identifica��o:
        return(matriz)
    elif max_transfs==0:
        return(None)
    for T in transforma��es:
        matriz_transformada=transforma(matriz, T)
        matriz_recebida=busca(matriz_transformada, transforma��es, identifica��o, max_transfs-1)
        if matriz_recebida!=None:
            return(matriz_recebida)
    return(None)


# ----------------------------------------------------------
# --                  FIM DA PARTE 4                      --
# ----------------------------------------------------------


# **********************************************************
# **                 INÃCIO DA PARTE 5                    **
# **********************************************************

def main():
    """ Aqui vocÃª deve implementar Ã  interface de comunicaÃ§Ã£o com o usuÃ¡rio

    Sua interface deve (necessariamente nessa ordem):
        1. Escrever uma mensagem de identificaÃ§Ã£o do autor e descriÃ§Ã£o do programa.
        2. Solicitar ao usuÃ¡rio que digite o nome do arquivo da imagem transformada.
        3. Solicitar ao usuÃ¡rio que digite o nome do arquivo contendo o identificador.
        4. Solicitar ao usuÃ¡rio que digite o nome do o arquivo com as transformaÃ§Ãµes.
        5. Solicitar ao usuÃ¡rio que digite o nome do arquivo no qual serÃ¡ salva a imagem restaurada (se encontrada).
        6. Informar se a busca foi exitosa ou nÃ£o.

    :Example:

    >>> $ python3 ep3.py
    *****************************
    *** Programa desfaz vÃ­rus ***
    *****************************

    Autor: Denis MauÃ¡
    NUSP: 3730790

    Entre com o nome do arquivo contendo imagem transformada: img00.pgm
    Entre com o nome do arquivo contendo o identificador da imagem original: img00.adler
    Entre com o nome do arquivo contendo as transformaÃ§Ãµes disponÃ­veis: transformaÃ§Ãµes00.txt
    Entre com o nome do arquivo onde a imagem original deve ser salva: resultado00.pgm
    Entre com o nÃºmero mÃ¡ximo de transformaÃ§Ãµes: 2

    Tentando restaurar imagem 'img00.pgm'... Falhou!

    NÃ£o foi possÃ­vel encontrar uma imagem com o identificador 870647247 utilizando uma sequÃªncia de no mÃ¡ximo 2 transformaÃ§Ãµes em 'transformaÃ§Ãµes00.txt'!

    VocÃª pode tentar aumentar o nÃºmero mÃ¡ximo de transformaÃ§Ãµes ou mudar o arquivo de transformaÃ§Ãµes.

    >>> $ python3 ep3.py
    *****************************
    *** Programa desfaz vÃ­rus ***
    *****************************

    Autor: Denis MauÃ¡
    NUSP: 3730790

    Entre com o nome do arquivo contendo imagem transformada: img01.pgm
    Entre com o nome do arquivo contendo o identificador da imagem original: img01.adler
    Entre com o nome do arquivo contendo as transformaÃ§Ãµes disponÃ­veis: transformaÃ§Ãµes.txt
    Entre com o nome do arquivo onde a imagem original deve ser salva: resultado01.pgm
    Entre com o nÃºmero mÃ¡ximo de transformaÃ§Ãµes: 6

    Tentando restaurar imagem 'img01.pgm'... Pronto!

    Imagem com o identificador 870647247 salva em 'resultado01.pgm'!

    .. seealso::
        Consulte o enunciado para mais exemplos.
    """

    print(" **************************************\n *** Programa d e s f a z v � r u s *** \n **************************************\n")

    print("Autor: ")
    print("NUSP: ")

    nome_imagem_transformada=input("Digite o nome do arquivo com a imagem transformada: ")
    nome_identificador=input("Digite o nome do arquivo com o identificador original: ")
    nome_transformacoes=input("Digite o nome do arquivo com as transforma��es: ")
    nome_restaurado=input("Digite o nome do arquivo com a imagem restaurada, caso seja poss�vel: ")
    max_transfs=int(input("Digite o n�mero m�ximo de transforma��es: "))

    matriz=carrega_imagem(nome_imagem_transformada)
    identificador=carrega_identificador(nome_identificador)
    transforma��es=carrega_transforma��es(nome_transformacoes)

    print("Tentando restaurar a imagem...")

    restaurada=busca(matriz, transforma��es, identificador, max_transfs)

    if restaurada!=None:
        salva_imagem(nome_restaurado,restaurada)
        print("A imagem com o identificador "+ str(identificador)+ " foi salva no arquivo: " + nome_restaurado + ".")
    else:
        salva_imagem(nome_restaurado, matriz)
        print("N�o foi poss�vel restaurar a imagem.")
        print("Tente outras transforma��es ou aumente o n�mero de transforma��es.")



# ----------------------------------------------------------
# --                  FIM DA PARTE 4                      --
# ----------------------------------------------------------


# ******************************************************
# **  IMPORTANTE: NÃƒO MODIFIQUE AS PRÃ“XIMAS LINHAS!   **
# ******************************************************
if __name__ == "__main__":
    main()
