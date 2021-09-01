"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Alessandro Brugnera Silva
  NUSP : 10334040
  Turma: 10
  Prof.: Alan

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort
"""

# ======================================================================
#
#   M A I N 
#
# ======================================================================
def main():

    print()
    print("=================================================")
    print("         Bem-vindo ao Jogo da Cobrinha!          ")
    print("=================================================")
    print()
    
    nlinhas = int(input('Número de linhas do tabuleiro : '))
    ncols   = int(input('Número de colunas do tabuleiro: '))
    x0      = int(input('Posição x inicial da cobrinha : '))
    y0      = int(input('Posição y inicial da cobrinha : '))
    t       = int(input('Tamanho da cobrinha           : '))

    # Verifica se corpo da cobrinha cabe na linha do tabuleiro,
    # considerando a posição inicial escolhida para a cabeça
    if x0 - (t - 1) < 0:
        # Não cabe
        print()
        print("A COBRINHA NÃO PODE FICAR NA POSIÇÃO INICIAL INDICADA")
        
    else:

        ''' Inicia a variável d indicando nela que t-1 partes do corpo
            da cobrinha estão inicialmente alinhadas à esquerda da cabeça.
            Exemplos:
               se t = 4, então devemos fazer d = 222
               se t = 7, então devemos fazer d = 222222
        '''
        d = 0
        i = 1
        while i <= t-1: 
            d = d * 10 + 2
            i = i + 1
        
        # Laço que controla a interação com o jogador
        direcao = 1
        while direcao != 5:
            # mostra tabuleiro com a posição atual da cobrinha
            imprime_tabuleiro(nlinhas, ncols, x0, y0, d)
            
            # lê o número do próximo movimento que será executado no jogo
            print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
            direcao = int(input("Digite o número do seu próximo movimento: "))
            
            if direcao != 5:
                # atualiza a posição atual da cobrinha
                x0, y0, d = move(nlinhas, ncols, x0, y0, d, direcao)

    print()        
    print("Tchau!")
    

# ======================================================================

def num_digitos(n):

  num=len(str(n))
  return num
 
# ======================================================================
def pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):

  xp=x0
  yp=y0
  ocupada=False
  cabeca=False


  if x==x0 and y==y0:
    ocupada=True
    cabeca=True
  while d!=0:
    if x!=xp or y!=yp:

      passo=d%10
      if passo==1:
        xp=xp+1
      if passo==2:
        xp=xp-1
      if passo==3:
        yp=yp+1
      if passo==4:
        yp=yp-1

      if x==xp and y==yp:
        ocupada=True

    d=d//10

  return (ocupada, cabeca)


# ======================================================================
def imprime_tabuleiro(nlinhas, ncols, x0, y0, d):

  x=0
  y=0
  linha1=0
  linhau=0

  while ncols+2 > linha1:
    print('#', end='')
    linha1 = linha1 + 1
  print('')

  while nlinhas > y:
    print('#', end='')
    while ncols > x:
      if pos_ocupada(nlinhas, ncols, x, y, x0, y0, d)[0] == True:
        if pos_ocupada(nlinhas, ncols, x, y, x0, y0, d)[1] == True:
          print('C', end='')
        else:
          print('*', end='')
      else:
        print('.', end='')
      x=x+1

    y=y+1
    print('#')
    x=0

  if nlinhas == y:
    while ncols+2 > linhau:
      print('#', end='')
      linhau = linhau + 1

  print('')
  print('')


# ======================================================================
def move(nlinhas, ncols, x0, y0, d, direcao):

  xp=x0
  yp=y0

  if direcao==1:
    xp=xp-1
  if direcao==2:
    xp=xp+1
  if direcao==3:
    yp=yp-1
  if direcao==4:
    yp=yp+1

  if pos_ocupada(nlinhas, ncols, xp, yp, x0, y0, d)[0]==False and xp!=ncols and xp!=-1 and yp!=nlinhas and yp!=-1:
    x0=xp
    y0=yp

    expoente=num_digitos(d)-1
    divisor=10**expoente
    if d!=0 :
      d=d%divisor
      d=10*d
      d=d+direcao

  elif xp==ncols or xp==-1 or yp==nlinhas or yp==-1:
    print()
    print('COLISÃO COM A PAREDE')
    print()
  elif pos_ocupada(nlinhas, ncols, xp, yp, x0, y0, d)[0]==True:
    print()    
    print('COLISÃO COM SI MESMA')
    print()
        
  return x0, y0, d

# ======================================================================
main()     
