# -*- coding: latin-1 -*-
import os
import pickle
from ep3 import *


def run_tests():
    total_tests = 14
    test_results = 0
    testing_now = 'data.p'
    print('######################################################')
    print('# Iniciando testes: (Parte02) Leitura e Escrita      #')
    print('######################################################')

    try:
        keep_index = 0
        print('Carregando testes...', end=' ')
        f = open('data.p', 'rb')
        data = pickle.load(f)
        f.close()
        print('OK')
        # carrega_identificador
        testing_now = 'carrega_identificador'
        print('Iniciando testes da função {0}...'.format(testing_now))
        for i in range(5):
            print('Teste 02_00_{:02}...'.format(i), end=' ')
            keep_index = i
            keep_id = carrega_identificador(data['test_02_00_{:02}D'.format(i)])
            assert type(keep_id) is int, 'Tipo não é inteiro, verifique se seu\ncarrega_identificador não está retornando float ou str'
            assert keep_id == data['test_02_00_{:02}A'.format(i)], 'Falhou na comparação de resultados do test_02_00_{:02}'.format(i)
            print("OK")
            test_results += 1
        # carrega_imagem
        testing_now = 'carrega_imagem'
        print('Iniciando testes da função {0}...'.format(testing_now))
        for i in range(5):
            print('Teste 02_01_{:02}...'.format(i), end=' ')
            keep_index = i
            keep_id = carrega_imagem(data['test_02_01_{:02}D'.format(i)])
            assert type(keep_id) is list, 'Tipo não é lista, verifique se seu\ncarrega_imagem não está retornando float ou str'
            for j in range(len(keep_id)):
                for k in range(len(keep_id[0])):
                    assert type(keep_id[j][k]) is int, 'Tipo do elemento não é int, verifique se seu\ncarrega_imagem não está retornando float ou str'
            assert keep_id == data['test_02_01_{:02}A'.format(i)], 'Falhou na comparação de resultados do test_02_01_{:02}'.format(i)
            print("OK")
            test_results += 1
        # salva_imagem
        testing_now = 'salva_imagem'
        print('Iniciando testes da função {0}...'.format(testing_now))
        for i in range(2):
            print('Teste 02_02_{:02}...'.format(i), end=' ')
            keep_index = i
            salva_imagem(data['test_02_02_{:02}D1'.format(i)], data['test_02_02_{:02}D2'.format(i)])
            keep_id = carrega_imagem(data['test_02_02_{:02}D1'.format(i)])
            assert type(keep_id) is list, 'Tipo não é lista, verifique se seu\ncarrega_imagem não está retornando float ou str'
            for j in range(len(keep_id)):
                for k in range(len(keep_id[0])):
                    assert type(keep_id[j][k]) is int, 'Tipo do elemento não é int, verifique se seu\ncarrega_imagem não está retornando float ou str'
            assert keep_id == data['test_02_02_{:02}A'.format(i)], 'Falhou na comparação de resultados do test_02_02_{:02}'.format(i)
            print("OK")
            test_results += 1
        # carrega_transformações
        testing_now = 'carrega_transformações'
        print('Iniciando testes da função {0}...'.format(testing_now))
        for i in range(2):
            print('Teste 02_03_{:02}...'.format(i), end=' ')
            keep_index = i
            keep_id = carrega_transformações(data['test_02_03_{:02}D'.format(i)])
            assert type(keep_id) is list, 'Tipo não é lista, verifique se seu\ncarrega_imagem não está retornando float ou str'
            for trans in keep_id:
                for j in range(len(trans)):
                    for k in range(len(trans[0])):
                        assert type(trans[j][k]) is int, 'Tipo do elemento não é int, verifique se seu\ncarrega_transformações não está retornando float ou str'
            assert keep_id == data['test_02_03_{:02}A'.format(i)], 'Falhou na comparação de resultados do test_02_03_{:02}'.format(i)
            print("OK")
            test_results += 1

    except IOError as e:
        print('FALHOU!')
        print('Falhou no teste da função {0}!'.format(testing_now))
        print('#####################################')
        print('Provavelmente você apagou ou moveu o')
        print("arquivo 'data.p' que deve estar na pasta")
        if testing_now == 'salva_imagem':
            print("OU sua função não conseguiu salvar/abrir no arquivo de teste: {0}".format(data['test_02_02_{:02}D1'.format(i)]))
            print("Verifique se você tem permissão de escrita na pasta e/ou ")
            print("se sua função está usando corretamente o nome do arquivo passado via parâmetro")
        print('#####################################')
        print('Em linguagem Python: {0}'.format(e))
    except NotImplementedError:
        print('FALHOU!')
        print('Falhou no teste da função {0}!'.format(testing_now))
        print(data['notimplementedmessage'])
    except AssertionError as e:
        print('FALHOU!')
        print('Falhou no teste {1} da função {0}!'.format(testing_now, keep_index))
        print('################################################')
        if testing_now == 'data.p':
            print(data['unexpectedmessage'])
            print('Tente consultar:\n{0}'.format(e))
            print('################################################')
        elif testing_now == 'carrega_identificador':
            print('Para o arquivo: {0}'.format(data['test_02_00_{:02}D'.format(keep_index)]))
            print('################################################')
            print('O resultado esperado era: {0}'.format(data['test_02_00_{:02}A'.format(keep_index)]))
            print('O resultado obtido foi: {0}'.format(keep_id))
        elif testing_now == 'carrega_imagem':
            print('Para o arquivo: {0}'.format(data['test_02_01_{:02}D'.format(keep_index)]))
            print('################################################')
            print('O resultado esperado era: {0}'.format(data['test_02_01_{:02}A'.format(keep_index)]))
            print('O resultado obtido foi: {0}'.format(keep_id))
        elif testing_now == 'salva_imagem':
            print('Para o arquivo: {0}'.format(data['test_02_02_{:02}D1'.format(keep_index)]))
            print('################################################')
            print('O resultado esperado era: {0}'.format(data['test_02_02_{:02}A'.format(keep_index)]))
            print('O resultado obtido foi: {0}'.format(keep_id))
        else:
            print('Para o arquivo: {0}'.format(data['test_02_03_{:02}D'.format(keep_index)]))
            print('################################################')
            print('O resultado esperado era: {0}'.format(data['test_02_03_{:02}A'.format(keep_index)]))
            print('O resultado obtido foi: {0}'.format(keep_id))
        print('################################################')
        print('Em linguagem Python:\n{0}'.format(e))
        print('################################################')
    except NameError as e:
        print('FALHOU!')
        print('Falhou no teste {1} da função {0}!'.format(testing_now, keep_index))
        print('################################################')
        print("Provavelmente você mexeu no arquivo 'data.p'")
        print('################################################')
        print('Em linguagem Python:\n{0}'.format(e))
        print('################################################')
    except Exception as e:
        print('FALHOU!')
        print('Falhou no teste da função função {0}!'.format(testing_now))
        print(data['unexpectedmessage'])
        if testing_now == 'carrega_transformações':
            print("3. Outra possibilidade:")
            print("Verifique se você está retornando uma matriz de matrizes")
        elif testing_now == 'salva_imagem':
            print("3. Outra possibilidade:")
            print("Verifique se há uma nova imagem salva na pasta e/ou")
            print("se o cabeçalho dessa imagem está correto conforme os")
            print("padrões especificados") 
        print('Tente consultar:\n{0}'.format(e))
        print('################################################')
    else:
        print('#############################################################')
        print('# Parabéns! Seu código passou em todos os testes da parte02 #')
        print('#############################################################')
        print(data['passedwarning'])
    finally:
        print('Resultados:')
        print('Nos testes da parte02:')
        print('Você obteve {0} acertos de um total de {1} possíveis'.format(test_results, total_tests))


if __name__ == "__main__":
    FILE_ABSOLUTE_PATH = os.path.abspath(__file__)
    TEST_DIR = os.path.dirname(FILE_ABSOLUTE_PATH)
    run_tests()
