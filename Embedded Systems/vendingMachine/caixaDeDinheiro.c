//
// Created by alessandro on 20/04/2020.
//

#include "caixaDeDinheiro.h"

static float credito;

void cxd_zeraCaixa() {
    credito = 0;
}

float cxd_getCredito() {
    return credito;
}

void cxd_adicionar(float dinheiroInserido) {
    credito += dinheiroInserido;
}
