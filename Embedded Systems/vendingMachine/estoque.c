//
// Created by alessandro on 20/04/2020.
//

#include <stdio.h>
#include <stdbool.h>
#include "estoque.h"
#include "string.h"
#include "caixaDeDinheiro.h"


struct produto {
    char nome[30];
    float preco;
    int quantidade;
};

static struct produto produtos[NUMS_SLOTSPRODUTOS];


void est_inicializaEstoque(void) {
    for (int i = 0; i < NUMS_SLOTSPRODUTOS; i++) { //ver se existe no estoque
        produtos[i].quantidade = -1;
        produtos[i].preco = 0.0;
    }


    //Já liga com isso
    strncpy(produtos[0].nome, "Suco de Laranja", 29);
    produtos[0].nome[29] = 0;
    produtos[0].preco = 1.00;
    produtos[0].quantidade = 3;

    strncpy(produtos[1].nome, "Suco de Maça", 29);
    produtos[1].preco = 2.00;
    produtos[1].quantidade = 3;
}

void est_exportarEstoque() { //TODO: tentar printar isso pelo comunicador
    fflush(stdin);
    for (int i = 0; i < NUMS_SLOTSPRODUTOS; i++) {
        if (produtos[i].quantidade > -1) {
            fflush(stdin);
            printf("Produto %i : ", i+1);
            printf("%i ", produtos[i].quantidade);
            printf("%s", produtos[i].nome);
            printf(": R$%.2f.\n", produtos[i].preco);
        }
    }

}

int est_pagamento(int produtoDesejado) {
    if (cxd_getCredito() >= produtos[produtoDesejado].preco) {
        return true;
    } else {
        return false;
    }
}

char* est_getNomeProduto(int produtoDesejado) {
    return  produtos[produtoDesejado].nome;
}

float est_getPrecoProduto(int produtoDesejado) {
    return  produtos[produtoDesejado].preco;
}

void est_alteraEstoque(int slotAlterado) {
    printf("Nome do Produto no slot %i: ", slotAlterado);
    fflush(stdin);
    scanf("%s", produtos[slotAlterado].nome);
    printf("Quantidade do Produto %s: ", produtos[slotAlterado].nome);
    fflush(stdin);
    scanf("%d", &produtos[slotAlterado].quantidade);
    printf("Preço do Produto %s: ", produtos[slotAlterado].nome);
    fflush(stdin);
    scanf("%f", &produtos[slotAlterado].preco);
    printf("\n");

    printf("Produto no slot %i : ", slotAlterado);
    printf("%i ", produtos[slotAlterado].quantidade);
    printf("%s", produtos[slotAlterado].nome);
    printf(": R$%.2f.\n", produtos[slotAlterado].preco);
    printf("\n");
}

int est_removeEstoque(int slotAlterado) {
    strncpy(produtos[slotAlterado].nome, "", 29);
    produtos[slotAlterado].nome[29] = 0;
    produtos[slotAlterado].quantidade = -1;
    produtos[slotAlterado].preco = 0.0;

    return true;
}


