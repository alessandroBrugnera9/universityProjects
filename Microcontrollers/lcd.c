/*
 * File:   lcd.c
 * Author: Jun Okamoto Jr.
 *
 * Created on April 18, 2020, 12:58 PM
 */

#include <xc.h>

# include "delay.h"

#define LCD_EN RB0    // [jo:200418] Enable
#define LCD_RW RA3    // [jo:200418] Read/Write
#define LCD_RS RA2    // [jo:200418] Register Select

//#define	LCD_STROBE	((LCD_EN = 1),(LCD_EN=0))
// [jo:091210] Como o clock � 20MHz, o LCD_STROBE original produz um pulso de 200ns
//             A especifica��o do display � > 450ns no m�nimo, assim � utilizado o
//             LCD_STROBE abaixo que produz cerca de 490ns. Rever no caso de altera��o
//             na frequencia do clock.
#define	LCD_STROBE ((LCD_EN = 1),(LCD_EN = 1),(LCD_EN = 1),(LCD_EN = 0))

void LCD_RS_SetLow(void) {LCD_RS = 0;}
void LCD_RS_SetHigh(void) {LCD_RS = 1;}
void LCD_RW_SetLow(void) {LCD_RW = 0;}
void LCD_RW_SetHigh(void) {LCD_RW = 1;}

void lcd_write_nibble (unsigned char c) {
  RC0 = (c & 0b00000001) >> 0;
  RC3 = (c & 0b00000010) >> 1;
  RC4 = (c & 0b00000100) >> 2;
  RC5 = (c & 0b00001000) >> 3;
  
  LCD_STROBE;
}

/* Escreve 1 byte no LCD em interface de 4 bits */
void lcd_write(unsigned char c) {
  lcd_write_nibble(c >> 4);
  lcd_write_nibble(c);       // envia para o LCD
  delay_us(40);
}

/* Limpa LCD e coloca cursor na 1a. posi��o da 1a. linha */
void lcd_clear(void) {
  LCD_RS_SetLow();  // � comando
  lcd_write(0x1);   // limpa o display e rotrona o cursor para posi��o 0
  delay_ms(2);      // tem que esperar pois esse comando demora
}

/* Escreve string no LCD */
void lcd_puts(const char * s) {
  LCD_RS_SetHigh();	// �  dado
  while(*s)
    lcd_write(*s++);
}

/*  Posiciona o cursor  */
void lcd_goto(unsigned char pos) {
  LCD_RS_SetLow();        // �  comando
  lcd_write(0x80 + pos);  // comando na forma 0b1eeeeeee, onde eeeeeee � o 
                          // endere�o da posi��o do cursor com 7-bits
                          //   se eeeeeee entre 0 e 40 - 1a. linha
                          //   se eeeeeee entre 64 e 104 - 2a. linha
}

/*  Liga/desliga cursor */
void lcd_cursor(int on) {
  LCD_RS_SetLow();   // � comando
  if (on) {          // se on for true - liga
    lcd_write(0x0f); //   display on, cursor on, blink on
  } else {           // se on for false - desliga
    lcd_write(0x0c); //   display on, cursor off, blink off
  }
}

/*  Escreve um caracter no display  */
void lcd_putchar(char c) {
  LCD_RS_SetHigh();  // � dado
  lcd_write(c);      // coloca caracter no display na posi��o atual do cursor
}

/* Inicializa LCD com interface de 4-bits */
void lcd_init(void) {
  // configura portas de I/O
  TRISB0 = 0;           // RB0 = ENABLE � sa�da
  ANS12 = 0;            // RB0 � digital
  TRISA3 = 0;           // RA3 = RW � sa�da
  ANS3 = 0;             // RA3 � digital
  TRISA2 = 0;           // RA2 = RS � sa�da
  ANS2 = 0;             // RA2 � digital
  TRISC & = 0b11000110; // Sa�das: RC5 = DB7, RC4 = DB6, RC3 = DB5, RC0 = DB4
  LCD_EN = 0;           // ENABLE no estado inicial
  
  LCD_RW_SetLow();      // modo de escrita
  LCD_RS_SetLow();	    // � comando
  delay_ms(15);	        // espera o display incializar
  lcd_write(0x02);      // define interface de 4-bits
  delay_ms(2);          // espera obrigat�ria
  lcd_write(0x28);      // 4 bit mode, 1/16 duty, 5x8 font
  lcd_write(0x08);      // deliga display
  lcd_write(0x0f);      // liga display, liga cursor
  lcd_write(0x06);      // entrada de dados � para a direita e cursor � auto-incrementado
}
