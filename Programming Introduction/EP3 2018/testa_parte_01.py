# -*- coding: latin-1 -*-
import os
import pickle
from ep3 import calcula_id


def run_tests():
    total_tests = 5
    test_results = 0
    print('######################################################')
    print('# Iniciando testes: (Parte01) Teste do identificador #')
    print('######################################################')

    try:
        keep_index = 0
        keep_id = 0
        print('Carregando testes...', end=' ')
        f = open('data.p', 'rb')
        data = pickle.load(f)
        f.close()
        print('OK')
        for i in range(5):
            print('Teste 01_{:02}...'.format(i), end=' ')
            keep_index = i
            keep_id = calcula_id(data['test_01_{:02}D'.format(i)])
            assert type(keep_id) is int, 'Tipo não é inteiro, verifique se seu calcula_id\nnão está retornando float ou str'
            assert keep_id == data['test_01_{:02}A'.format(i)], 'Falhou na comparação de resultados do test_01_{:02}'.format(i)
            print("OK")
            test_results += 1
    except IOError as e:
        print('FALHOU!')
        print('Falhou no teste da função calcula_id!')
        print('#####################################')
        print('Provavelmente você apagou ou moveu o')
        print("arquivo 'data.p' que deve estar na pasta")
        print('#####################################')
        print('Em linguagem Python: {0}'.format(e))
    except NotImplementedError:
        print('FALHOU!')
        print('Falhou no teste da função calcula_id!')
        print(data['notimplementedmessage'])
    except AssertionError as e:
        print('FALHOU!')
        print('Falhou no teste {0} da função calcula_id!'.format(keep_index))
        print('################################################')
        print('Para à matriz: {0}'.format(data['test_01_{:02}D'.format(keep_index)]))
        print('################################################')
        print('O resultado esperado era: {0}'.format(data['test_01_{:02}A'.format(keep_index)]))
        print('O resultado obtido foi: {0}'.format(keep_id))
        print('################################################')
        print('Em linguagem Python:\n{0}'.format(e))
        print('################################################')
    except NameError as e:
        print('FALHOU!')
        print('Falhou no teste {0} da função calcula_id!'.format(keep_index))
        print('################################################')
        print("Provavelmente você mexeu no arquivo 'data.p'")
        print('################################################')
        print('Em linguagem Python:\n{0}'.format(e))
        print('################################################')
    except Exception as e:
        print('FALHOU!')
        print('Falhou no teste da função calcula_id!')
        print(data['unexpectedmessage'])
        print('Tente consultar:\n{0}'.format(e))
        print('################################################')
    else:
        print('#############################################################')
        print('# Parabéns! Seu código passou em todos os testes da parte01 #')
        print('#############################################################')
        print(data['passedwarning'])
    finally:
        print('Resultados:')
        print('Nos testes da parte01:')
        print('Você obteve {0} acertos de um total de {1} possíveis'.format(test_results, total_tests))


if __name__ == "__main__":
    FILE_ABSOLUTE_PATH = os.path.abspath(__file__)
    TEST_DIR = os.path.dirname(FILE_ABSOLUTE_PATH)
    run_tests()
