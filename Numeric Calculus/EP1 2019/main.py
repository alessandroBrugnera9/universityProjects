import Tarefa2 as t2
import numpy as np
import pdb
import time
import matplotlib.pyplot as plt
import Parte3 as p3

tempo=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
graficos=[]
for dig in range(10):
	for p in [5,10,15]:
		#pdb.set_trace()
		t=time.time()
		#Wd,grafico=t2.fatoracaoWH(np.load("dados_mnist/A%d.npy" %dig),p)
		A = np.loadtxt("dados_mnist/train_dig" + str(dig) + ".txt")
		A = A/255
		Wd,grafico=t2.fatoracaoWH(A,p)
		np.save("W" + str(dig) + "p" + str(p), Wd)

		print("W" + str(dig) + "p" + str(p)) #controle do console
		print(time.time()-t)


		#tempo[[5,10,15].index(p)][dig]=time.time()-t #dados para análise
		plt.plot(grafico[0], grafico[1])
		#graficos.append(grafico) #gera todos os graficos

np.save(np.array(tempo),"tempo") #salva matriz de tempo
#np.save(np.array(graficos),"graficos") #salva graficos

plt.xlabel('Iteracao')
plt.ylabel('Erro Quadratico')
plt.savefig("Wdig")  #salva grafico de todos digitos e iteracoes
  
for p in [5,10,15]:       #Análise de acertos
	print("Resultados para p = " + str(p) + " são: ")
	#tempo = time.time()
	A = np.loadtxt("dados_mnist/test_images.txt")
	b = np.loadtxt("dados_mnist/test_index.txt")
	Digitos, Frequencia = p3.Calcular_acertos(A, b, p)
	for j in range(10):
		print("A frequencia de acertos para o dígito "+str(j)+" é:",Frequencia[j][3],"%")
	#print("Tempo da parte 3: ", time.time() - tempo)