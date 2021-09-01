//
// Created by alessandro on 20/04/2020.
//

#ifndef VENDINGMACHINE_COMUNICADOR_H
#define VENDINGMACHINE_COMUNICADOR_H

extern int com_inputSeletor();

extern void com_inserindoDinheiro();
extern void com_dinheiroInserido();

extern void com_pedindo();
extern void com_pedidoRecebido();

extern void com_alterandoEstoque();
extern void com_estoqueAlterado();

extern void com_removendoProduto();
extern void com_produtoRemovido();

extern void com_cancelamento();
#endif //VENDINGMACHINE_COMUNICADOR_H
