//
// Created by alessandro on 20/04/2020.
//

#include <stdio.h>
#include "comunicador.h"
#include "caixaDeDinheiro.h"
#include "string.h"
#include "estoque.h"


int com_inputSeletor() {
    int evento;
    printf("\n");
    printf("O  Que você deseja fazer (colocar o número respectivo):");
    printf("\n");
    printf("1  Para adicionar crédito.");
    printf("\n");
    printf("2  Para selecionar produto.");
    printf("\n");
    printf("3  Cancela a compra e devolve o troco.");
    printf("\n");
    printf("7  Modo de alteração de estoque.");
    printf("\n");
    printf("8  Remove produto.");
    printf("\n");
    printf("9  Desliga a máquina.");
    fflush(stdin);
    printf("\n");
    scanf("%d", &evento);

    return evento;
}

void com_inserindoDinheiro() {
    printf("Quantos reais você vai adicionar? ");
}

void com_dinheiroInserido() {//TODO: Try Catch
    float dinheiroInserido;
    fflush(stdin);
    scanf("%f", &dinheiroInserido);
    cxd_adicionar(dinheiroInserido);
    fflush(stdin);
    printf("Crédito: R$%.2f", cxd_getCredito());
}

void com_pedindo(void) {
    est_exportarEstoque();
    fflush(stdin);
    printf("Qual produto você deseja (coloque o número respectivo)? ");
}

void com_pedidoRecebido() {//TODO: Try Catch
    fflush(stdin);
    int produtoDesejado;
    scanf("%d", &produtoDesejado);

    if (est_pagamento(produtoDesejado)) {
        printf("\n");
        printf("Produto %s entregue.",
               est_getNomeProduto(produtoDesejado)); //TODO: conferir se isso com ponteiro vai dar bom
        printf("\n");
        printf("Troco: %.2f.", cxd_getCredito() - est_getPrecoProduto(produtoDesejado));
    } else {
        printf("\n");
        printf("Crédito insuficiente.");
    }
}

void com_alterandoEstoque() {
    fflush(stdin);
    est_exportarEstoque();
    fflush(stdin);
    printf("Qual slot de produto será removido (Número de 1 a 10)?\n");
}

void com_estoqueAlterado() {
    fflush(stdin);
    int slotAlterado;
    scanf("%d", &slotAlterado);

    est_alteraEstoque(slotAlterado);
}

void com_removendoProduto() {
    fflush(stdin);
    est_exportarEstoque();
    fflush(stdin);
    printf("Qual slot de produto será removido (Número de 1 a 10)?\n");
}

void com_produtoRemovido() {
    fflush(stdin);
    int slotAlterado;
    scanf("%d", &slotAlterado);


    if (est_removeEstoque(slotAlterado)) {
        printf("Slot %i vazio. ", slotAlterado);
    } else {
        printf("Slot inexistente.");
    }

}

void com_cancelamento() {
    printf("Compra cancelada.\n");
    printf("Troco: R$%.2f.\n", cxd_getCredito());
    cxd_zeraCaixa();
}
