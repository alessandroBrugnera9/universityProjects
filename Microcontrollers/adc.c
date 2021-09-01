#include <xc.h>
#include <stdio.h>
#include "delay.h"


void adc_init_0(void) {
    /// Inicializa canal AN0 do conversor A/D
    TRISA0 = 1; //entrada
    ANS0 = 1; // anal�gico
    
    ADCS1 = 1; // FOSC/32 pois T precisa ser <= 1,6ns
    
    VCFG1 = 0; //VSS = 0V
    VCFG0 = 0; //VDD = 5V
    
    ADCON0bits.CHS = 0; // Mux no AN0
    
    ADFM = 1; //justificado � direita
    
    ADON = 1; //liga coversor
    
    delay_ms(10); // > tempo de aquisi��o
}

unsigned int adc_read_0(void) {
    /// Faz a leitura do canal AN0 do conversor A/D
    /// @return Retorna um inteiro sem sinal que corresponde a leitura do A/D 
    ///justificado � direita ou � esquerda conforme a inicializa��o
    
    GO = 1;
    
    while(GO); //conversao
    
    unsigned int ADC_result = (unsigned int)(ADRESH*256.0 + ADRESL);
    
    return ADC_result; 
}