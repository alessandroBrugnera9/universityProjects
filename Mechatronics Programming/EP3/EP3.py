from heapq import heappush, heappop
from teste3 import Node
import pdb
import sys
import math
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle('Huffman')

        extractAction = QAction('&Quit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Fechar Programa.')
        extractAction.triggered.connect(self.close_application)

        comprimir = QAction('&Comprimir', self)
        comprimir.setShortcut('Ctrl+O')
        comprimir.setStatusTip('Abrir arquivo para ser comprimido.')
        comprimir.triggered.connect(self.comprimir)

        Salvar_huf = QAction('&Salvar .huf', self)
        Salvar_huf.setShortcut('Ctrl+S')
        Salvar_huf.setStatusTip('Salvar .huf.')
        Salvar_huf.triggered.connect(self.salvar_huf)

        Descomprimir = QAction('&Descomprimir .huf', self)
        Descomprimir.setShortcut('Ctrl+D')
        Descomprimir.setStatusTip('Abrir .huf')
        Descomprimir.triggered.connect(self.descomprimir)

        Salvar_descomprimido = QAction('&Salvar Arquivo Descomprimido', self)
        Salvar_descomprimido.setShortcut('Ctrl+P')
        Salvar_descomprimido.setStatusTip('Salvar arquivo descomprimido.')
        Salvar_descomprimido.triggered.connect(self.salvar_descomp)

        self.statusBar()
        self.editor()


        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        comprmirMenu = mainMenu.addMenu('&Comprimir')
        comprmirMenu.addAction(comprimir)
        comprmirMenu.addAction(Salvar_huf)

        descomprmirMenu = mainMenu.addMenu('&Descomprimir')
        descomprmirMenu.addAction(Descomprimir)
        descomprmirMenu.addAction(Salvar_descomprimido)

        self.home()

        self.textEdit.append("Para utilizar comprimir arquivos utilizando o algoritmo de Huffman utilize o File Dialog, ou descomprimir arquivos - de Huffman; a partir dos menus acima.\n")




    def comprimir(self):
        self.txt, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        teste=open(self.txt, "r")
        try:
            if len(teste.read())>=9999:
                self.textEdit.append("O arquivo '" + self.txt.split("/")[-1] + "' tem mais de 9999 caracteres ou mais. Escolha outro arquivo.\n")
                teste.close()
                return()
        except:
            self.textEdit.append("O arquivo '" + self.txt.split("/")[-1] + "' contem caracteres irregulares. Escolha outro arquivo.\n")
            teste.close()
            return()

        teste.close()
        self.leitura=leitura(self.txt)
        self.arvore=montagem_arvore(self.leitura)[1]
        self.bst=BST(self.arvore)
        self.root=self.bst.devolveroot()
        self.cifra=self.bst.preordertraverse(self.root)
        self.tabela=criar_tabela(self.cifra)

        self.textEdit.append("O arquivo '" + self.txt.split("/")[-1] + "' foi comprimido. Escolha onde salvá-lo.\n")

    def salvar_huf(self):
        pdb.set_trace()
        try:
            if type(self.cifra) is dict:
                pass
        except:
            self.textEdit.append("Primeiro escolha um arquivo para comprimir, antes de salvá-lo.\n")    
            return()

        self.huf, _ = QFileDialog.getSaveFileName(self, 'Save File', options=QFileDialog.DontUseNativeDialog)
        gravar_arquivo(self.tabela, self.huf, self.txt, self.cifra)

        self.textEdit.append("O arquivo '" + self.huf.split("/")[-1] + "' comprimido foi salvo.`\n")

    def descomprimir(self):
        self.huf_pronto, _ = QFileDialog.getOpenFileName(self, 'Save File', options=QFileDialog.DontUseNativeDialog)
        try:
            self.leitura_huf=leitura_huf(self.huf_pronto)
            self.leitura_huf.leitura()

            self.textEdit.append("O arquivo '" + self.huf_pronto.split("/")[-1] + "' foi descomprimido. Escolha onde salvá-lo.\n")
        except:
            self.textEdit.append("O arquivo é irregular.\n")
            return()
    def salvar_descomp(self):
        try:
            if self.leitura_huf is leitura_huf:
                pass
        except:
            self.textEdit.append("Primeiro escolha um arquivo para descomprimir, antes de salvá-lo.\n")
            return()

        self.descomprimido, _ = QFileDialog.getSaveFileName(self, 'Save File', options=QFileDialog.DontUseNativeDialog)
        self.leitura_huf.grava(self.descomprimido)

        self.textEdit.append("O arquivo '" + self.descomprimido.split("/")[-1] + "' descomprimido foi salvo.\n")

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0, 100)

    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.show()


    def close_application(self):

        choice = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            print('quit application')
            sys.exit()
        else:
            pass

class Node:
    def __init__(self, car=None,freq=None,left=None,right=None):
        self.caracter = car
        self.frequencia = freq
        self.left = left
        self.right = right
    
    def __str__(self):
        if (self.caracter is None):
            return('0')
        else:
            return('1')
        
    def __lt__(self,other):
        if (self.frequencia <= other.frequencia):
            return(True)
        else:
            return(False)
            
class BST:
    def __init__(self,root=None):
        self.root = root
        
    def devolveroot(self):
        return self.root
    
    def preordertraverse(self,p, cifra=""):
        if(p is not None):
            if (p.caracter is not None):
                cifra+="1"
                binario=bin(ord(p.caracter))[2:]
                for i in range(8-len(binario)):
                    binario="0"+binario
                cifra+=binario
                cifra+=""


            else:
                cifra+="0"
                cifra=self.preordertraverse(p.left, cifra)
                cifra=self.preordertraverse(p.right, cifra)
        return(cifra)

class leitura_huf:
    """docstring for leitura_huf"""
    def __init__(self, arquivo_huf):
        self.arquivo_huf = arquivo_huf

    def leitura(self):
        string=""
        file=open(self.arquivo_huf,"rb")
        caracteres_dif=int(file.read(3).decode("utf-8"))
        caracteres=int(file.read(4).decode("utf-8"))

        bits=""
        bytes_=file.read()
        for byte in bytes_:
            bits+='{:08b}'.format(byte) 

        tabela, posicao=criar_tabela(bits, caracteres_dif)
        aumento=8-len(bits[:posicao+8])%8 #tirar zeros

        #leitura
        bits=bits[posicao+8+aumento:]
        parcial=""
        contador=0
        keys=list(tabela.keys())
        valores=list(tabela.values())

        while len(string)<caracteres:
            parcial+=bits[contador]
            if parcial in valores:
                string+=keys[valores.index(parcial)]
                parcial=""
            contador+=1

        file.close()
        self.string=string
        self.tabela=tabela
        return()

    def grava(self, arquivo_txt):
        file=open(arquivo_txt, "w")
        file.write(self.string)
        file.close()

        return()



def criar_tabela(cifra, caracteres_dif=math.inf):
    tabela={}
    contador=0
    contador_de_i=0
    ultimo_i=0
    bits_cifra=len(cifra)

    while len(tabela)<caracteres_dif:
        #percorre cada bit
        for bit in cifra[:bits_cifra-8]:
            if len(tabela)>=caracteres_dif:
                break
            #primeiro caracter
            if bit=="1" and contador_de_i==0:
                tabela[chr(int(cifra[contador+1:contador+9],2))]=cifra[:contador]
                ultimo_i=contador
                ultimo=cifra[:contador]
                contador_de_i+=1
                contador+=1
                continue

            #caracter qualquer
            elif bit=="1" and contador-ultimo_i>8:
                proximo=ultimo

                #tira ultimo zero e o resto
                acha_0=len(proximo)-1
                while proximo[acha_0]!="0":
                    acha_0-=1
                proximo=proximo[:acha_0]
                proximo+="1"

                #ve se precisa adicionar 0
                if contador-ultimo_i-8>1:
                    zeros=""
                    for a in range(contador-ultimo_i-9):
                        zeros+="0"
                    proximo+=zeros

                #adiciona na tabela
                tabela[chr(int(cifra[contador+1:contador+9],2))]=proximo

                #informacoes para o proximo
                ultimo=proximo
                contador_de_i+=1
                ultimo_i=contador

            contador+=1
        if caracteres_dif!=math.inf:
            return(tabela,contador)
        else:
            return(tabela)
    #quando le arquivo
    return(tabela,contador)


def leitura(arquivo):
    caracteres={}

    #contar caracteres
    file=open(arquivo, "r")
    for line in file:
        for letra in line:
            if letra not in caracteres:
                caracteres[letra]=0
            caracteres[letra]+=1

    return(caracteres)

def montagem_arvore(caracteres):
    nodos={}
    fila=[]

    #Criação dos nodos e das tuples para a fila de prioridades
    for c in caracteres:
        nodos[c]=Node(c, caracteres[c])
        heappush(fila,(nodos[c].frequencia, nodos[c]))

    contador=0
    while len(fila) is not 1: # ate a lista ficar vazia
        left = heappop(fila)
        right = heappop(fila)
        heappush(fila,(left[0]+right[0], Node(None, left[0]+right[0], left[1], right[1])))                             
        contador+=1

    arvore=heappop(fila)

    return(arvore)

def gravar_arquivo(tabela, arquivo, txt,linear):
    file=open(arquivo, "wb")
    arquivo_txt=open(txt, "r")
    bits=""
    caracteres=0

    #primeiros 3 bytes
    string=str(len(tabela))
    while len(string)<3:
        string="0"+string

    for c in string:
        file.write(bytes([int(ord(c))]))

    #outros 4 bytes

    #contagem de caracteres
    for line in arquivo_txt:
        for letra in line:
            bits+=tabela[letra]
            caracteres+=1

    str_caracteres=str(caracteres)
    while len(str_caracteres)<4:
        str_caracteres="0"+str_caracteres

    for c in str_caracteres:
        file.write(bytes([int(ord(c))]))

    #dicionario em pre ordem
    linear_zerado=completa_byte(linear)
    #pega cada byte da string
    for index in range(0, len(linear_zerado),8):
        file.write(bytes([int(linear_zerado[index:index+8],2)]))

    #transcreve o texto
    bits_zerado=completa_byte(bits)
    for index in range(0, len(bits_zerado),8):
        file.write(bytes([int(bits_zerado[index:index+8],2)]))

    file.close()
    arquivo_txt.close()
    return()

def completa_byte(bits):
    zeros_extras = 8 - len(bits) % 8
    for i in range(zeros_extras):
        bits += "0"

    return(bits)


def main():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
