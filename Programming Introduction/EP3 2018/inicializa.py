# ********************************************************
# *      IMPORTANTE: NÃO MODIFIQUE ESSE ARQUIVO!         *
# ********************************************************

import os
import sys
import platform
import pickle


def create_ep3(data):
    try:
        f = open('ep3.py', 'x')
        if platform.system() == 'Windows':
            f.write('# -*- coding: latin-1 -*-\n')
        f.write(data['ep3'])
        f.close()
    except IOError:
        print("FALHOU! (Arquivo ep3.py já existe)")
        return False
    else:
        print("OK")
        return True


def run_tests():
    """ Executa testes da parte 00 """
    #total_files = 32
    total_files = 64 
    files_checked = 0
    print('####################################################')
    print('# Iniciando testes: (Parte00) Teste de integridade #')
    print('####################################################')
    try:
        f = open('data.p', 'rb')
        data = pickle.load(f)
        f.close()
        # Write part
        for i in range(1, 5):  # Maybe change to 6 if test05
            print("Criando 'testa_parte_{:02}.py'...".format(i), end=' ')
            f = open('testa_parte_{:02}.py'.format(i), 'w')
            if platform.system() == 'Windows':
                f.write('# -*- coding: latin-1 -*-\n')
            f.write(data['testa_parte_{:02}.py'.format(i)])
            f.close()
            print("OK")
            files_checked += 1
        for i in range(11):
            print("Criando 'img{:02}.adler32'...".format(i), end=' ')
            f = open('img{:02}.adler32'.format(i), 'w')
            f.write(data['img{:02}.adler32'.format(i)])
            f.close()
            print("OK")
            files_checked += 1
            print("Criando 'img{:02}.pgm'...".format(i), end=' ')
            f = open('img{:02}.pgm'.format(i), 'w')
            f.write(data['img{:02}.pgm'.format(i)])
            f.close()
            print("OK")
            files_checked += 1

        print("Criando 'LEIAME.txt'...", end=' ')
        f = open('LEIAME.txt', 'w')
        f.write(data['leiame'])
        f.close()
        print("OK")
        files_checked += 1
        print("Criando 'transformações.txt'...", end=' ')
        f = open('transformações.txt', 'w')
        f.write(data['transformações.txt'])
        f.close()
        print("OK")
        files_checked += 1
        print("Criando 'duas_transformações.txt'...", end=' ')
        f = open('duas_transformações.txt', 'w')
        f.write(data['duas_transformações.txt'])
        f.close()
        print("OK")
        files_checked += 1
        print("Criando 'ep3.py'...", end=' ')
        if create_ep3(data):
            files_checked += 1
        print("Criando 'enunciado_ep3_mac2166.pdf'...", end=' ')
        f = open('enunciado_ep3_mac2166.pdf', 'wb')
        f.write(data['enunciado'])
        f.close()
        print("OK")
        files_checked += 1
        print("Criando 'ARQUIVO.txt'...", end=' ')
        f = open('ARQUIVO.txt', 'w')
        f.write(data['arquivo'])
        f.close()
        print("OK")
        files_checked += 1

        print('####################################################')
        # Read part
        print("Verificando 'enunciado_ep3_mac2166.pdf'...", end=' ')
        f = open('enunciado_ep3_mac2166.pdf', 'r')
        f.close()
        print("OK")
        files_checked += 1
        print("Verificando 'ep3.py'...", end=' ')
        f = open('ep3.py', 'r')
        f.close()
        print("OK")
        files_checked += 1
        print("Verificando 'ARQUIVO.txt'...", end=' ')
        f = open('ARQUIVO.txt', 'r')
        f.close()
        print("OK")
        files_checked += 1
        for i in range(1, 5):  # change to 6 if test05
            print("Verificando 'testa_parte_{:02}.py'...".format(i), end=' ')
            f = open('testa_parte_{:02}.py'.format(i), 'r')
            f.close()
            print("OK")
            files_checked += 1
        print("Verificando 'transformações.txt'...", end=' ')
        f = open('transformações.txt', 'r')
        f.close()
        print("OK")
        files_checked += 1
        print("Verificando 'duas_transformações.txt'...", end=' ')
        f = open('duas_transformações.txt', 'r')
        f.close()
        print("OK")
        files_checked += 1
        for i in range(11):
            print("Verificando 'img{:02}.adler32'...".format(i), end=' ')
            f = open('img{:02}.adler32'.format(i), 'r')
            f.close()
            print("OK")
            files_checked += 1
            print("Verificando 'img{:02}.pgm'...".format(i), end=' ')
            f = open('img{:02}.pgm'.format(i), 'r')
            f.close()
            print("OK")
            files_checked += 1
        print("Verificando 'LEIAME.txt'...", end=' ')
        f = open('LEIAME.txt', 'r')
        f.close()
        print("OK")
        files_checked += 1
    except PermissionError:
        print("FALHOU")
        print(data['permissionmessage'])
    except IOError as e:
        print('\n################################################')
        print("O arquivo .zip descompactado está corrompido, baixe e", end=' ')
        print("descompacte novamente")
        print("Pelo menos um problema detectado em:\n{0}".format(e))
    else:
        print('################################################')
        print("Parabéns! Seu programa passou no teste de integridade.")
        print("Em sua pasta, você agora possui todos os arquivos necessários")
        print("para execução desse EP, inclusive um chamado LEIAME.txt")
        print("com o resumo das atividades previstas para esse EP.")
        print("Você já pode começar à trabalhar na Parte 1!")
        print('################################################')
    print('Resultados:')
    print('No teste de integridade:')
    print('Você obteve {0} acertos de um total de {1} possíveis'.format(files_checked, total_files))


if __name__ == "__main__":
    FILE_ABSOLUTE_PATH = os.path.abspath(__file__)
    TEST_DIR = os.path.dirname(FILE_ABSOLUTE_PATH)
    sys.path.append(TEST_DIR)
    run_tests()
