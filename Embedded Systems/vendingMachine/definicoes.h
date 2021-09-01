//
// Created by alessandro on 20/04/2020.
//

#ifndef VENDINGMACHINE_DEFINICOES_H
#define VENDINGMACHINE_DEFINICOES_H

#define NUM_ESTADOS 5
#define NUM_EVENTOS 10

#define NENHUM_EVENTO -1
#define INSERIRDINHEIRO 1
#define DINHEIROINSERIDO 4
#define PEDIR 2
#define PEDIDOSUCESSO 5
#define CANCELAR 3
#define ALTERARESTOQUE 7
#define ESTOQUEALTERADO 9
#define REMOVERPRODUTO 8
#define PRODUTOREMOVIDO 10


#define NENHUMA_ACAO -1
#define A01 1
#define A02 2
#define A03 3
#define A04 4
#define A05 5
#define A06 6
#define A07 7
#define A08 8
#define A09 9


#define IDLE 0
#define PEDINDO 1
#define INSERINDO 2
#define CANCELANDO 3
#define ALTERANDOESTOQUE 4
#define REMOVENDOPRODUTO 5

#endif //VENDINGMACHINE_DEFINICOES_H
