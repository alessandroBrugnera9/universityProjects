import numpy as np
import math
import ResolveSimult as sm
import copy
import pdb
import time

def fatoracaoWH(A,p):
	n=len(A)
	m=len(A[0])
	epsilon=1E-5
	its=100
	erro1=1
	contador=0
	erro2=-1
	A=np.array(A)
	grafico=[[],[]]

	W=np.random.randint(100, size=(n,p))/10 # criando matriz de entradas (floats) positivas aleatórias
	#W = np.array([[0.6, 0], [0, 1], [0.8, 0]])
	while (abs(erro1-erro2)>epsilon and contador<100): #itera para achar as matrizes
		#print(contador)
		#print(W)
		if contador>0: #erro anterior para entrar no proximo loop
			erro2=diferenca2(copy.deepcopy(A),W,H)
			pass
		for j in range(p): #normaliza cada coluna
			W=normaColuna(W,j)

		#pdb.set_trace()
		
		H=sm.Resolver_simult(m,n, p, W, copy.deepcopy(A))
		#print("tempo para resolver o 1o MMQ", tempo - time.time())
		
		for i in range(len(H)): #muda valores de H para 0, se a entrada for negativa
			for j in range(len(H[0])):
				if H[i][j]<0:
					H[i][j]=0
				else:
					pass

		W=np.array([])
		#pdb.set_trace()
		#tempo2 = time.time()
		W=sm.Resolver_simult(n, m, p, copy.deepcopy(H.transpose()), copy.deepcopy(A).transpose()).transpose()
		#print("tempo para resolver o 2o MMQ", tempo2 - time.time())
		
		#pdb.set_trace()
		for i in range(len(W)): #muda valores de W para 0, se a entrada for negativa
			for j in range(len(W[0])):
				if W[i][j]<0:
					W[i][j]=0
				else:
					pass


		erro1=diferenca2(copy.deepcopy(A),W,H) #novo erro para entrar no proximo loop
		grafico[0].append(contador+1)
		grafico[1].append(erro1)
		contador+=1

	return(W,grafico) #retorno W e H depois de iterar


def diferenca(A,W,H):  #calcula a diferenca quadratica entre A-W*H
	M=np.dot(W,H)
	n=len(A)
	m=len(A[0])
	error=0
	for i in range(n):
		for j in range(m):
			error+=(A[i][j]-M[i][j])**2

	return(error)

def diferenca2(A,W,H):  #calcula a diferenca quadratica entre A-W*H
	M=np.dot(W,H)
	error=0
	E = (A - M)**2
	error = E.sum()
	return(error)



def normaColuna(W,j):
	s=0
	n=len(W)
	for i in range(n):
		s+=W[i][j]**2
	s=math.sqrt(s)
	for i in range(n):
		W[i][j]=W[i][j]/s

	return(W)


































































