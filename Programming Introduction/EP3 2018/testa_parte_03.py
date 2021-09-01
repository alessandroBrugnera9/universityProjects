# -*- coding: latin-1 -*-
import os
import pickle
from ep3 import transforma


def run_tests():
    total_tests = 5
    test_results = 0
    print('##########################################################')
    print('# Iniciando testes: (Parte03) Transforma��es geom�tricas #')
    print('##########################################################')

    try:
        keep_index = 0
        print('Carregando testes...', end=' ')
        f = open('data.p', 'rb')
        data = pickle.load(f)
        f.close()
        print('OK')
        # carrega_identificador
        testing_now = 'transforma'
        print('Iniciando testes da fun��o {0}...'.format(testing_now))
        for i in range(5):
            print('Teste 03_{:02}...'.format(i), end=' ')
            keep_index = i
            keep_id = transforma(data['test_03_{:02}D1'.format(i)], data['test_03_{:02}D2'.format(i)])
            assert type(keep_id) is list, 'Tipo n�o � lista, verifique se seu\ncarrega_imagem n�o est� retornando float ou str'
            for j in range(len(keep_id)):
                for k in range(len(keep_id[0])):
                    assert type(keep_id[j][k]) is int, 'Tipo do elemento n�o � int, verifique se seu\ntransforma n�o est� retornando float ou str'
            assert keep_id == data['test_03_{:02}A'.format(i)], 'Falhou na compara��o de resultados do test_03_{:02}'.format(i)
            print("OK")
            test_results += 1
    except IOError as e:
        print('FALHOU!')
        print('Falhou no teste da fun��o {0}!'.format(testing_now))
        print('#####################################')
        print('Provavelmente voc� apagou ou moveu o')
        print("arquivo 'data.p' que deve estar na pasta")
        print('#####################################')
        print('Em linguagem Python: {0}'.format(e))
    except NotImplementedError:
        print('FALHOU!')
        print('Falhou no teste da fun��o {0}!'.format(testing_now))
        print(data['notimplementedmessage'])
    except AssertionError as e:
        print('FALHOU!')
        print('Falhou no teste {1} da fun��o {0}!'.format(testing_now, keep_index))
        print('################################################')
        print('Para o matriz M0: {0}'.format(data['test_03_{:02}D1'.format(keep_index)]))
        print('Com transforma��es: {0}'.format(data['test_03_{:02}D2'.format(keep_index)]))
        print('################################################')
        print('O resultado esperado era: {0}'.format(data['test_03_{:02}A'.format(keep_index)]))
        print('O resultado obtido foi: {0}'.format(keep_id))
        print('################################################')
        print('Em linguagem Python:\n{0}'.format(e))
        print('################################################')
    except NameError as e:
        print('FALHOU!')
        print('Falhou no teste {1} da fun��o {0}!'.format(testing_now, keep_index))
        print('################################################')
        print("Provavelmente voc� mexeu no arquivo 'data.p'")
        print('################################################')
        print('Em linguagem Python:\n{0}'.format(e))
        print('################################################')
    except Exception as e:
        print('FALHOU!')
        print('Falhou no teste da fun��o fun��o {0}!'.format(testing_now))
        print(data['unexpectedmessage'])
        print('Tente consultar:\n{0}'.format(e))
        print('################################################')
    else:
        print('#############################################################')
        print('# Parab�ns! Seu c�digo passou em todos os testes da parte03 #')
        print('#############################################################')
        print(data['passedwarning'])
    finally:
        print('Resultados:')
        print('Nos testes da parte03:')
        print('Voc� obteve {0} acertos de um total de {1} poss�veis'.format(test_results, total_tests))


if __name__ == "__main__":
    FILE_ABSOLUTE_PATH = os.path.abspath(__file__)
    TEST_DIR = os.path.dirname(FILE_ABSOLUTE_PATH)
    run_tests()
