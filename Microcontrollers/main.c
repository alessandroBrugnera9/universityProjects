/*
 * File:   main.c
 * Author: Jun Okamoto Jr.
 *
 * Created on April 18, 2020, 12:58 PM
 */


// PIC16F886 Configuration Bit Settings

// 'C' source line config statements

// CONFIG1
#pragma config FOSC = EC        // Oscillator Selection bits (EC: I/O function on RA6/OSC2/CLKOUT pin, CLKIN on RA7/OSC1/CLKIN)
#pragma config WDTE = OFF       // Watchdog Timer Enable bit (WDT disabled and can be enabled by SWDTEN bit of the WDTCON register)
#pragma config PWRTE = OFF      // Power-up Timer Enable bit (PWRT disabled)
#pragma config MCLRE = ON       // RE3/MCLR pin function select bit (RE3/MCLR pin function is MCLR)
#pragma config CP = OFF         // Code Protection bit (Program memory code protection is disabled)
#pragma config CPD = OFF        // Data Code Protection bit (Data memory code protection is disabled)
#pragma config BOREN = ON       // Brown Out Reset Selection bits (BOR enabled)
#pragma config IESO = ON        // Internal External Switchover bit (Internal/External Switchover mode is enabled)
#pragma config FCMEN = ON       // Fail-Safe Clock Monitor Enabled bit (Fail-Safe Clock Monitor is enabled)
#pragma config LVP = OFF        // Low Voltage Programming Enable bit (RB3 pin has digital I/O, HV on MCLR must be used for programming)

// CONFIG2
#pragma config BOR4V = BOR40V   // Brown-out Reset Selection bit (Brown-out Reset set to 4.0V)
#pragma config WRT = OFF        // Flash Program Memory Self Write Enable bits (Write protection off)

// #pragma config statements should precede project file includes.
// Use project enums instead of #define for ON and OFF.

#include <xc.h>
#include <stdio.h>
#include <stdlib.h>
#include "always.h"
#include "delay.h"
#include "io.h"
#include "lcd.h"
#include "adc.h"
#include "debug.h"
#include "pwm.h"

#define PWM1_DIR RA1
#define PWM2_DIR RB1

//Variaveis Globais
volatile unsigned int ADC_result;
volatile int pwm_dc1;
volatile int pwm_dc2;
volatile int *pointer_pwm_dc1 = &pwm_dc1;
volatile int *pointer_pwm_dc2 = &pwm_dc2;


void interrupt isr(void) {
    // Função para tratamento de interrupções
    // local variables -> static
    // global variables -> volatile
    
    // Tratamento da interrupção do Timer 0
    if (T0IE && T0IF) {
        // Interrupção do Timer 0 aqui
        ADC_result = adc_read_0(); // valor guardado no ADC
        TMR0 = (0xff - 98 ) ; // valor inicial do Timer 0     
        T0IF = 0; // limpa flag de interrupção
    }
    // a cada ciclo, se detectou que chave foi pressionada inverte o sentido dos pwm's
    if (TMR2IE && TMR2IF) {
       if (io_sw_pressed()) // exemplo de uso de detecção de chave pressionada
           pwm_dc1 = -pwm_dc1;
           pwm_dc2 = -pwm_dc2;
    }

  
    // Tratamento da interrupção do Port B
    // quando chave é pressionada 
    if (RBIE && RBIF) {

      //char portB = PORTB; // leitura do port B limpa interrupção

      io_sw_read(PORTB);      // Necessário para usar a chave
      //debug_led_toggle(1);    // exemplo de uso do LED de debug

      RBIF = 0; // limpa o flag de interrupção para poder atender nova
    }    
}


void t0_init(void) {
    // Inicialização do Timer 0 aqui
    
    T0CS = 0; // clock interno FOSC/4
    PSA = 0; // prescalar p/timer0

    OPTION_REGbits.T0CS = 0; // usa clock interno FOSC /4
    OPTION_REGbits.PSA = 0; // prescaler é para o Timer 0 e não para o WDT
    OPTION_REGbits.PS = 7 ; // ajusta o Prescaler do Timer 0 (divide por 256)
    TMR0 = (0xff - 98 ) ; // valor inicial do Timer 0
    
    // Interrupções
    T0IE = 1; // habilita a interrupção do Timer 0
    
}

void tmr2_init(void) {
    // incicialização do Timer2 aqui
    
    TMR2IF = 0; // limpa flag de interrupcao
    T2CONbits.T2CKPS = 1; // prescaler = 4
    TMR2ON = 1; // liga timer
    
    TMR2IE = 1; // habilita a interrupção do timer 2
    
}
 
void main(void) {
    // Programa Principal
    
    //variáveis locais
    int R; // raio da curva
    char message[9];     
    
    // Inicializações
    
    adc_init_0();        // inicializa conversor A/D
    t0_init();           // inicializa Timer 0
    io_init();         // inicializa chave, LED e Buzzer
    lcd_init();          // inicializa LCD
    //debug_init();        // inicializa LEDs para debug
    PEIE = 1;            // interrupcoes perifericas
    ei();                // macro do XC8, equivale a GIE = 1, habilita interrupções
    tmr2_init();          // inicializa timer 2 
    pwm_init();          // inicializa pwm's
    
    
    // configuracao inciais
    lcd_cursor(0);
    
    while (1) {
        //lcd_puts("888888"); // todo lcd_puts ele só ta printando o primeiro caracter
        R = pwm_calc(ADC_result, pointer_pwm_dc1, pointer_pwm_dc2);
        pwm_set(pwm_dc1, pwm_dc2); 
        
        // Mostrar info no LCD
        if (R == 0) {
            lcd_putchar(0xf3);
        } else {
            sprintf(message, "%d", R);
            lcd_puts(message);

            lcd_puts(" [mm]");
        }
        
        lcd_goto(64); // 2a linha
        lcd_puts("PWM1:"); 
        sprintf(message, "%d", pwm_dc1);
        lcd_puts(message);
        
        lcd_puts("PWM2:");
        sprintf(message, "%d", pwm_dc2);
        lcd_puts(message); 
        
        lcd_puts("[%]");
        
        delay_ms(200);
    }
    
}
