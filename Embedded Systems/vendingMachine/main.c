#include <stdio.h>
#include <stdbool.h>
#include "definicoes.h"
#include "estoque.h"
#include "caixaDeDinheiro.h"
#include "comunicador.h"

int acaoMatrizTransicaoEstados[NUM_ESTADOS][NUM_EVENTOS];
int proximoEstadoMatrizTransicaoEstados[NUM_ESTADOS][NUM_EVENTOS];

void iniciaMaquinaEstados(void) {
    int i;
    int j;

    for (i = 0; i < NUM_ESTADOS; i++) {
        for (j = 0; j < NUM_EVENTOS; j++) {
            acaoMatrizTransicaoEstados[i][j] = NENHUMA_ACAO;
            proximoEstadoMatrizTransicaoEstados[i][j] = i;
        }
    }

    proximoEstadoMatrizTransicaoEstados[IDLE][INSERIRDINHEIRO] = INSERINDO;
    acaoMatrizTransicaoEstados[IDLE][INSERIRDINHEIRO] = A01;

    proximoEstadoMatrizTransicaoEstados[INSERINDO][DINHEIROINSERIDO] = IDLE;
    acaoMatrizTransicaoEstados[INSERINDO][DINHEIROINSERIDO] = A02;


    proximoEstadoMatrizTransicaoEstados[IDLE][PEDIR] = PEDINDO;
    acaoMatrizTransicaoEstados[IDLE][PEDIR] = A03;

    proximoEstadoMatrizTransicaoEstados[PEDINDO][PEDIDOSUCESSO] = IDLE;
    acaoMatrizTransicaoEstados[PEDINDO][PEDIDOSUCESSO] = A04;


    proximoEstadoMatrizTransicaoEstados[IDLE][CANCELAR] = CANCELANDO;
    acaoMatrizTransicaoEstados[IDLE][CANCELAR] = A09;


    proximoEstadoMatrizTransicaoEstados[IDLE][ALTERARESTOQUE] = ALTERANDOESTOQUE;
    acaoMatrizTransicaoEstados[IDLE][ALTERARESTOQUE] = A05;

    proximoEstadoMatrizTransicaoEstados[ALTERANDOESTOQUE][ESTOQUEALTERADO] = IDLE;
    acaoMatrizTransicaoEstados[ALTERANDOESTOQUE][ESTOQUEALTERADO] = A06;


    proximoEstadoMatrizTransicaoEstados[IDLE][REMOVERPRODUTO] = REMOVENDOPRODUTO;
    acaoMatrizTransicaoEstados[IDLE][REMOVERPRODUTO] = A07;

    proximoEstadoMatrizTransicaoEstados[REMOVENDOPRODUTO][PRODUTOREMOVIDO] = IDLE;
    acaoMatrizTransicaoEstados[REMOVENDOPRODUTO][PRODUTOREMOVIDO] = A08;


}

void iniciaSistema(void) {
    iniciaMaquinaEstados();
    est_inicializaEstoque();
    cxd_zeraCaixa();
    printf("Vending Machine ligada!\n");
}


int executaAcao(int codigoAcao) {
    int eventoInterno = NENHUM_EVENTO;

    if (codigoAcao == NENHUMA_ACAO) {
        return NENHUM_EVENTO;
    }

    switch (codigoAcao) {
        break;
        case A01:
            com_inserindoDinheiro();
            eventoInterno = DINHEIROINSERIDO;
            break;

        case A02:
            com_dinheiroInserido();
            break;

        case A03:
            com_pedindo();
            eventoInterno = PEDIDOSUCESSO;
            break;

        case A04:
            com_pedidoRecebido();
            break;

        case A05:
            com_alterandoEstoque();
            eventoInterno = ESTOQUEALTERADO;
            break;

        case A06:
            com_estoqueAlterado();
            break;

        case A07:
            com_removendoProduto();
            eventoInterno = PRODUTOREMOVIDO;
            break;

        case A08:
            com_produtoRemovido();
            break;

        case A09:
            com_cancelamento();
            break;

        default:
            printf("Ação não identificada.");
            break;
    }

    return eventoInterno;
}

int obterEvento() {
    //TODO: recebe input
    int teclaRecebida = com_inputSeletor();

    switch (teclaRecebida) {
        case PEDINDO:
            return PEDINDO;
            break;
        case INSERINDO:
            return INSERINDO;
            break;
        case CANCELANDO:
            return CANCELANDO;
            break;
        case ALTERANDOESTOQUE:
            return ALTERANDOESTOQUE;
            break;
        case REMOVENDOPRODUTO:
            return REMOVENDOPRODUTO;
            break;
        default:
            printf("Comando desconhecido."); //TODO:avaliar se eh gambiarra
            break;
    }



    return NENHUM_EVENTO;
}

int obterProximoEstado(int estado, int evento) {
    return proximoEstadoMatrizTransicaoEstados[estado][evento];
}

int obterAcao(int estado, int evento) {
    return acaoMatrizTransicaoEstados[estado][evento];
}

int main(void) {

    int codigoEvento;
    int codigoAcao;
    int estado;
    int eventoInterno;

    estado = IDLE;
    eventoInterno = NENHUM_EVENTO;

    iniciaSistema();

//    loop de maquina de estados:
    while (true) {
        if (eventoInterno == NENHUM_EVENTO) {
            codigoEvento = obterEvento();
        } else {
            codigoEvento = eventoInterno;
        }
        if (codigoEvento != NENHUM_EVENTO) {
            codigoAcao = obterAcao(estado, codigoEvento);
            estado = obterProximoEstado(estado, codigoEvento);
            eventoInterno = executaAcao(codigoAcao);
//            printf("\nEstado: %d Evento: %d Acao: %d\n", estado, codigoEvento, codigoAcao);


        }
    }

}