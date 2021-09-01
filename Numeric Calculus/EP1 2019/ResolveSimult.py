'''
Entradas necessárias:  Inteiros: m,n e p. 
					   Matrizes: W, A
					   
Saida do algoritmo:    Matriz H
'''
###############################################################################
import numpy as np
import copy
import pdb
import time

def Resolver_simult (m, n, p, W, A):
    A_tmp = copy.deepcopy(A)
    W_tmp = copy.deepcopy(W)
    n = len(W)
    m = len(A[0])
    p = len(W[0])
	 
    def Rotgivens(W,n,m,i,j,c,s):     #Código do RotGivens fornecido pelo IME
        W[i,0:m] , W[j,0:m] = c * W[i,0:m] - s * W[j,0:m] , s * W[i,0:m] + c * W[j,0:m]
        return W
	
    
    def Triangularizar (W, A):       #Aplicar RotGivens até que W fique traiangular
        W_tmp = copy.deepcopy(W)     #E aplica RotGivens em A também
        A_tmp = copy.deepcopy(A)
        for k in range(p):
            for j in range (n-1, 0, -1):
                i = j-1
                if W_tmp[j,k] != 0:
                    a = np.float64(W_tmp[i][k])
                    b = np.float64(W_tmp[j][k])
                    c = a/(np.sqrt(a**2+b**2))    #Determinar cos
                    s = -b/(np.sqrt(a**2+b**2))   #Determinar sin
                    if j>k:
                        R = Rotgivens(W_tmp, n, p, i, j, c, s)
                        A_tmp = Rotgivens(A_tmp, n, m, i, j, c, s)
        A_novo = copy.deepcopy(A_tmp)
        return R, A_novo
    
    def ResolvSimult (m, R, A):  #Dado a matriz triangular R e o A aplicado... 
        A_tmp = copy.deepcopy(A) #...retorna a matriz H
        H_tmp = np.zeros((p,m))
        for k in range(p-1, -1, -1):
               if R[k,k] != 0:   #impedir divisão por 0
                   for j in range(m):
                       somatorio = 0
                       for u in range(k+1, p):
                          somatorio += R[k][u]*H_tmp[u][j]
                       H_tmp[k][j] = (A_tmp[k][j] - somatorio)/R[k][k] 
        H_final = copy.deepcopy(H_tmp)  
        return H_final
###############################################################################	
    R, A = Triangularizar (W_tmp, A_tmp)
    H = ResolvSimult(m, R, A)
    return H

