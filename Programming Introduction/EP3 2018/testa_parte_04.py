# -*- coding: latin-1 -*-
import os
import pickle
from ep3 import *


def run_tests():
    total_tests = 2
    test_results = 0
    print('##########################################################')
    print('# Iniciando testes: (Parte04) Busca                      #')
    print('##########################################################')

    try:
        keep_index = 0
        print('Carregando testes...', end=' ')
        f = open('data.p', 'rb')
        data = pickle.load(f)
        f.close()
        print('OK')
        # busca
        testing_now = 'busca'
        print('Iniciando testes da função {0}...'.format(testing_now))
        for i in range(2):
            print('Teste 04_{:02}...'.format(i), end=' ')
            keep_index = i
            keep_id = busca(data['test_04_{:02}D1'.format(i)], data['test_04_{:02}D2'.format(i)], data['test_04_{:02}D3'.format(i)], data['test_04_{:02}D4'.format(i)])
            keep_id2 = calcula_id(keep_id)
            assert type(keep_id) is list, 'Tipo não é lista, verifique se sua\nbusca não está retornando float ou str'
            for j in range(len(keep_id)):
                for k in range(len(keep_id[0])):
                    assert type(keep_id[j][k]) is int, 'Tipo do elemento não é int, verifique se sua\nbusca não está retornando float ou str na matriz'
            if keep_id2 != data['test_04_{:02}A2'.format(i)]:
                raise AssertionError('Falhou na comparação de resultados do test_04_{:02}'.format(i))
            print("OK")
            test_results += 1
    except IOError as e:
        print('FALHOU!')
        print('Falhou no teste da função {0}!'.format(testing_now))
        print('#####################################')
        print('Provavelmente você apagou ou moveu o')
        print("arquivo 'data.p' que deve estar na pasta")
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
        print('Para uma busca com:')
        print('Matriz: {0}'.format(data['test_04_{:02}D1'.format(keep_index)]))

        print('Transformações: {0}'.format(data['test_04_{:02}D2'.format(keep_index)]))
        print('identificador: {0}'.format(data['test_04_{:02}D3'.format(keep_index)]))
        print('max_transfs: {0}'.format(data['test_04_{:02}D4'.format(keep_index)]))
        print('################################################')
        print('Nosso resultado foi: {0}'.format(data['test_04_{:02}A1'.format(keep_index)]))
        print('O resultado obtido foi: {0}'.format(keep_id))
        print('Como era possível que duas buscas retornassem matrizes')
        print('diferentes de mesmo identificador, calculamos o')
        print('identificador de ambas e o resultado foi:')
        print('Identificador esperado: {0}'.format(data['test_04_{:02}A2'.format(keep_index)]))
        print('Seu identificador: {0}'.format(keep_id2))
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
        print('Tente consultar:\n{0}'.format(e))
        print('################################################')
    else:
        print('#############################################################')
        print('# Parabéns! Seu código passou em todos os testes da parte04 #')
        print('#############################################################')
        print(data['passedwarning'])
    finally:
        print('Resultados:')
        print('Nos testes da parte04:')
        print('Você obteve {0} acertos de um total de {1} possíveis'.format(test_results, total_tests))


if __name__ == "__main__":
    FILE_ABSOLUTE_PATH = os.path.abspath(__file__)
    TEST_DIR = os.path.dirname(FILE_ABSOLUTE_PATH)
    run_tests()
