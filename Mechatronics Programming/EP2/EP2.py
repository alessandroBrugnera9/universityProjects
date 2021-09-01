import math

class grafo:
  def __init__(self,graph = {}):
    self.graph=graph

  def  AcrescentaVertice(self,v):
    try:
      type(self.graph[v])
    except:
      self.graph[v]={}

  def RemoveVertice(self,v):
    if self.graph[v]=={}:
      del self.graph[v]

  def AcrescentaArco(self,v1,v2):
    self.graph[v1][v2]=0
  
  def AcrescentaDistancia(self,v1,v2,dist):
    self.graph[v1][v2]=dist

  def RemoveArco(self,v1,v2):
    del self.graph[v1][v2]
    del self.graph[v2][v1]

  def  AchaMenorCaminho(self,v1,v2):
    #monta a tabela com as distancias do vertice inicial
    tabela={}
    for vertice in self.graph:
      tabela[vertice]=[]
      tabela[vertice].append(math.inf)
      tabela[vertice].append(v1)
      try:
        tabela[vertice][0]=self.graph[v1][vertice]
        tabela[vertice].append(vertice)
      except:
        pass
    tabela[v1][0]=0
    
    espaco=[v1]
    #chama a parte recursiva
    path=grafo.Algoritmo(tabela,espaco,v1)[v2]    
    return path[1:]

  def Algoritmo(self,tabela,espaco,v1):
    #proximo vertice
    dist_proximo_vertice=math.inf
    espaco.append("x")
    for vertice in self.graph:
      if vertice not in espaco and tabela[vertice][0]<dist_proximo_vertice:
        dist_proximo_vertice=tabela[vertice][0]
        espaco[-1]=vertice
        
    #menor caninho ate o novo vertice
    for v in self.graph[espaco[-1]]:
      if self.graph[espaco[-1]][v]+tabela[v][0]<tabela[espaco[-1]][0]:
        tabela[espaco[-1]]=[self.graph[espaco[-1]][v]+tabela[v][0]]
        tabela[espaco[-1]]+=tabela[v][1:]+espaco[-1]

    #novos caminhos pelo novo vertice
    for v in self.graph[espaco[-1]]:
      if self.graph[espaco[-1]][v]+tabela[espaco[-1]][0]<tabela[v][0]:
        tabela[v]=[self.graph[espaco[-1]][v]+tabela[espaco[-1]][0]]
        tabela[v]+=tabela[espaco[-1]][1:]+[v]

    #finalizacao ou continuar recursao
    if len(espaco)==len(self.graph):
      return tabela
    else:
      tabela=grafo.Algoritmo(tabela,espaco,v1)
    return tabela

  def CalculaDistancia(self,path):
    distancia=0
    for d in range(len(path)-1):
      distancia+=self.graph[path[d]][path[d+1]]
    
    return distancia

  def ImprimeGrafo(self):
    seta=" ->"
    for d in list(self.graph.keys()):
      print(str(d)+seta, end="")
      for c in list(self.graph[d].keys()):
        print(" " + str(c) + ':' + str(self.graph[d][c]), end="")
      print()

def main():
  #nome do arquivo
  while True:
    try:
      leituradoarquivo(input("Nome do arquivo com os dados(deixar a extensao): "))
      break
    except:
      print("arquivo nao escontrado")

  #respostas
  respostas=open(input("Nome do arquivo para gerar respostas(deixar a extensao): "), "w")
  
  #as distancias calculadas serao obtitdas de outro arquivo no padrao do enunciado ou feita perguntanda ponto a ponto  
  arquivo_ou_input=int(input("1 para leitura de arquivo com os caminhos  ou 0 para leitura no input: "))

  if arquivo_ou_input==1:
    pontos=distanciascalculadas(input("Nome do arquivo com as distancias para calcular: "))
    for p in pontos:
      path=grafo.AchaMenorCaminho(p[0],p[1])
      #parte do print
      print("Distancia entre " + str(p[0]) + " e " + str(p[1]) + " = " + str(grafo.CalculaDistancia(path)))
      respostas.write("Distancia entre " + str(p[0]) + " e " + str(p[1]) + " = " + str(grafo.CalculaDistancia(path))+"\n")
      print("Caminho percorrido: ", end="")
      respostas.write("Caminho percorrido: ")
      for d in path:
        if path.index(d)+1==len(path):
          print(d)
          respostas.write(d+"\n\n")
        else:
          print(d + "->", end="")
          respostas.write(d + "->")

  elif arquivo_ou_input==0:
    saida=input("Capital de saída(-1 para parar): ")
    chegada=input("Capital de chegada(-1 para parar): ")
    while saida!="-1" and chegada!="-1":
      try:
        path=grafo.AchaMenorCaminho(saida,chegada)
      except:
        print("vertice invalido.")
        saida=input("Capital de saída(-1 para parar): ")
        chegada=input("Capital de chegada(-1 para parar): ")
        continue
      print("Distancia entre " + saida + " e " + chegada + " = " + str(grafo.CalculaDistancia(path)))
      respostas.write("Distancia entre " + saida + " e " + chegada + " = " + str(grafo.CalculaDistancia(path))+"\n")
      print("Caminho percorrido: ", end="")
      respostas.write("Caminho percorrido: ")
      for d in path:
        if path.index(d)+1==len(path):
          print(d)
          respostas.write(d+"\n\n")
        else:
          print(d + "->", end="")
          respostas.write(d + "->")

      saida=input("Capital de saída(-1 para parar): ")
      chegada=input("Capital de chegada(-1 para parar): ")

  respostas.close()
      
def leituradoarquivo(arquivo):
  global grafo
  file=open(arquivo, "r")
  linhas=file.readlines()
  
  for l in linhas:
    #separacao de cada linha
    linha_atual=l.split()
    conexoes=len(linha_atual)-1
    
    #montando os grafos com os valores das linhas
    grafo.AcrescentaVertice(linha_atual[0])
    for c in range(1,conexoes+1):
      grafo.AcrescentaVertice(linha_atual[c][0])
      grafo.AcrescentaArco(linha_atual[0],linha_atual[c][0])
      grafo.AcrescentaDistancia(linha_atual[0],linha_atual[c][0],int(linha_atual[c][2:]))

  file.close()
  return
      
def distanciascalculadas(arquivo):
  file=open(arquivo, "r")
  linhas=file.readlines()
  pontos=[]
  
  for l in linhas:
    #separacao de cada linha
    l=l.split()

    del l[1] #tirar hifen
    pontos.append(l)

  file.close()
  return pontos


grafo=grafo()
main()
