'''
Entradas necessárias:  Matriz A  = test_imagens.txt
                       Matriz b = test_index.txt
					   Inteiro p
Saida do algoritmo:   Print da taxa de acerto e retorna uma lista com digitos possíveis
'''
###############################################################################
import ResolveSimult as sm
import numpy as np
import copy

def Calcular_acertos(A_test, Gabarito, p):

	def Classificar(A_test): #Classificar os dígitos em uma lista de possíveis dígitos
		n = len(A_test)
		n_treino = len(A_test[0])
		if p == 5:
			Norma = np.empty((10,n_treino))
			A_tmp = copy.deepcopy(A_test)
			for dig in range(10):
				Wd = np.load("W"+str(dig)+"p5.npy")
				Wd_tmp = copy.deepcopy(Wd)
				H = sm.Resolver_simult(n_treino, n, p, Wd_tmp, A_tmp) #MMQ, via QR
				M = A_tmp - np.dot(Wd_tmp,H)
				M = M**2
				for j in range(n_treino):
					erro = Diferenca_c (M,j)
					Norma[dig][j] = erro
					
			minimo = np.argmin(Norma, axis=0)
			[Norma[minimo[i]][i] for i in range(0,Norma.shape[1])]
			b_calculado = minimo
			return  b_calculado
		
		if p == 10:
			Norma = np.empty((10,n_treino))
			A_tmp = copy.deepcopy(A_test)
			for dig in range(10):
				Wd = np.load("W"+str(dig)+"p10.npy")
				Wd_tmp = copy.deepcopy(Wd)
				H = sm.Resolver_simult(n_treino, n, p, Wd_tmp, A_tmp) #MMQ, via QR
				M = A_tmp - np.dot(Wd_tmp,H)
				M = M**2
				for j in range(n_treino):
					erro = Diferenca_c (M,j)
					Norma[dig][j] = erro #Lista com as normas Euclidianas
		
			minimo = np.argmin(Norma, axis=0)
			[Norma[minimo[i]][i] for i in range(0,Norma.shape[1])]
			b_calculado = minimo
			return  b_calculado
	
		if p == 15:
			Norma = np.empty((10,n_treino))
			A_tmp = copy.deepcopy(A_test)
			for dig in range(10):
				Wd = np.load("W"+str(dig)+"p15.npy")
				Wd_tmp = copy.deepcopy(Wd)
				H = sm.Resolver_simult(n_treino, n, p, Wd_tmp, A_tmp) #MMQ, via QR
				M = A_tmp - np.dot(Wd_tmp,H)
				M = M**2
				for j in range(n_treino):
					erro = Diferenca_c (M,j)
					Norma[dig][j] = erro #Lista com as normas Euclidianas
		
			minimo = np.argmin(Norma, axis=0)
			[Norma[minimo[i]][i] for i in range(0,Norma.shape[1])]
			b_calculado = minimo
			return  b_calculado
		
		else:
			Norma = np.empty((10,n_treino))
			A_tmp = copy.deepcopy(A_test)
			for dig in range(10):
				Wd = np.load("W"+str(dig)+"p"+str(p)+".npy")
				Wd_tmp = copy.deepcopy(Wd)
				H = sm.Resolver_simult(n_treino, n, p, Wd_tmp, A_tmp) #MMQ, via QR
				M = A_tmp - np.dot(Wd_tmp,H)
				M = M**2
				for j in range(n_treino):
					erro = Diferenca_c (M,j)
					Norma[dig][j] = erro #Lista com as normas Euclidianas
		
			minimo = np.argmin(Norma, axis=0)
			[Norma[minimo[i]][i] for i in range(0,Norma.shape[1])]
			b_calculado = minimo
			return  b_calculado
		
	def Diferenca_c(C,j):	#Calcula a norma euclidicana, dado um array C já elevado ao quadrado
		soma = sum((C[:,j]))
		c = np.sqrt(soma)
		return c
	
	def Taxa (C,G): #Calcula a taxa de acerto com um C calculado, em relação ao gabarito G
		n = len(C)
		cont = 0
		M = C - G
		for i in range(n):
			if M[i] == 0:
				cont = cont+1
		taxa = cont/n
		return taxa*100
###############################################################################
	Digito = Classificar(A_test)
	Taxa = (Digito, b)	
	print("A taxa de acertos é de: ", Taxa, "%"), 
	return Digito

A = np.loadtxt("dados_mnist/test_images.txt")
A = A/255
b = np.loadtxt("dados_mnist/test_index.txt")

p = 5
Digito_p5 = Calcular_acertos(A)

p = 10

Digito_p10 = Calcular_acertos(A)

p = 15

Digito_p15 = Calcular_acertos(A)





