#include <xc.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>


#define PWM1_DIR RA1
#define PWM2_DIR RB1


void pwm_init(void) {
    // pino correspondente ao CCP1
    TRISC1 = 1; // configura como entrada (desabilita saída)
    // pino correspondente ao CCP2
    TRISC2 = 1; // configura como entrada (desabilita saída)
    
    // configura modulo CCP
    CCP1CONbits.P1M = 0;
    // CCP2CONbits.P2M = 0; // nao tem essa config no CCP2CON
    
    CCP1CONbits.CCP1M = 0b1100;
    CCP2CONbits.CCP2M = 0b1100;
    
    int pwm_dc1 = 50; // em %
    int pwm_dc2 = 50;
    
    PR2 = 255; // maxima resolucao
    
    // pwm 1
    ANS1 = 0; // digital
    PWM1_DIR = 0; // PWM1_DIR deslocamento para frente
    
    //pwm 2
    ANS10 = 0; //digital
    PWM2_DIR = 0; // PWM2_DIR deslocamento para frente
    
    while(!TMR2IF);
    TRISC1 = 0;
    TRISC2 = 0;
}


void pwm_set(int pwm_dc1, int pwm_dc2) {
    //local variables
    static unsigned int n_1;
    static unsigned int n_2;
    static unsigned int absolute_pwm_dc1;
    static unsigned int absolute_pwm_dc2;
    
    //// n doPWM1 (n_1) e n do PWM2 (n_2)
    // calculo de acordo com a equacao do datasheet 
    // Tosc = 1/20*10^6; TMR2 presclaer = 4; Tpwm = 1/(5*10^3);
    
    // n = Duty Cycle / Tosc * TMR2 presclaer
    // + 0.5 é só pr a arredondar pro valor mais proximo
    
    absolute_pwm_dc1 = abs(pwm_dc1);
    absolute_pwm_dc2 = abs(pwm_dc2);
    
    n_1 = (int)( ( ( (abs(absolute_pwm_dc1)/100.0)*0.0002 )/( 0.0000002 ) ) + 0.5 );
    n_2 = (int)( ( ( (abs(absolute_pwm_dc2)/100.0)*0.0002 )/( 0.0000002 ) ) + 0.5 );
    
    // pwm 1
    CCPR1L = n_1 >> 2;
    CCP1CONbits.DC1B = n_1 % 4;
    //pwm 2 CCP1CONbits.DC2B nao tava fucionando
    CCPR2L = n_2 >> 2;
    DC2B1 = (n_2 % 4) >> 1;
    DC2B0 = (n_2 % 4) % 2;
    
    // atualiza de acordo com a direcao 
    // PWMn_DIR = 0 -> deslocamento para frente
    if (pwm_dc1*pwm_dc2 > 0) {
        pwm_dc1 > 0 ? PWM1_DIR, PWM2_DIR = 0 : PWM1_DIR, PWM2_DIR = 1; 
    }
    
}

int pwm_calc(int adc_value, int *pwm_dc1, int *pwm_dc2) {
    static int radius;

    if (PWM1_DIR = 0) {
        // para frente, valores positivos
        // 1) Cálculo dos pwm's pela relacao linear com o adc_value
        *pwm_dc1 = (int)((adc_value/1023.0)*100 + 0.5);
        *pwm_dc2 = 100 - *pwm_dc1;
        
        // 2) Cálculo do raio pela relacao linear com as velocidades, 
        // estas que estabelecem uma relacao linear com os pwm's

        ///Velocidades aqui embaixo (relacao linear com pwm)
        //v1 = 6*(*pwm_dc1);
        //v2 = 600 - v1;
        
        // raio positivo
        if (adc_value != 512) {
            radius = (int)(11250.0/((6*(*pwm_dc1)) - 300));
            return radius;
        } else { return 0; } // raio infinito
        
    } else {  
        // para tras, valores negativos 
        *pwm_dc1 = (int)((-adc_value/1023.0)*100 + 0.5);
        *pwm_dc2 = - 100 - *pwm_dc1;
        
        // 2) Cálculo do raio pela relacao linear com as velocidades, 
        // estas que estabelecem uma relacao linear com os pwm's

        ///Velocidades aqui embaixo (relacao linear com pwm)
        //v1 = -6*(*pwm_dc1);
        //v2 = -600 + v1;

        // raio negativo
        if (adc_value != 512) {
            radius = (int)(-11250.0/((6*(*pwm_dc1)) - 300));
            return radius;
        } else { return 0; } // raio infinito
    }
   
    
}

