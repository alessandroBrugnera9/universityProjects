/* 
 * File:             adc.h 
 * Author:           Jun Okamoto Jr.
 * Comments:         Convers�o Anal�gico-Digital
 * Revision history: 200423 - vers�o inicial
 */

// This is a guard condition so that contents of this file are not included
// more than once.  
#ifndef ADC_H
#define	ADC_H

#include <xc.h> // include processor files - each processor file is guarded.  

///
/// Inicializa canal AN0 do conversor A/D
///
extern void adc_init_0(void);

///
/// Faz a leitura do canal AN0 do conversor A/D
///
/// @return Retorna um inteiro sem sinal que corresponde a leitura do A/D 
///         justificado � direita ou � esquerda conforme a inicializa��o
///
extern unsigned int adc_read_0(void);

#endif	/* ADC_H */

