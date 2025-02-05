/*
 * File:   Timer.c
 * Author: Evan
 *
 * Created on 05 March 2018, 19:10
 */


#include <xc.h>
#include "Timer.h"
#include "Constants.h"
#include "USART.h"

unsigned int temp_time;   //16 bit number
unsigned int time;

void Init_TMR1(void)
{
    
    T1CON = 0b00000000;
    T1CONbits.TMR1CS = 0b00;    //Timer1 clock source is instruction clock (Fosc/4)
    T1CONbits.T1CKPS = 0b01;    //Prescale value 1:2
    
    T1GCON = 0b01000000;        //bit 6 is setting timer1 gate is active high (timer1 counts when gate is high)
    
    INTCON = 0b10000000;
    
    return;
}

 unsigned int Timer1(void)
{
        TMR1ON = Disable;                 // Stop the timer
        
        temp_time = TMR1H;
        temp_time <<= 8;
        temp_time += TMR1L;
                
        TMR1L = 0x00;
        TMR1H = 0x00;
        
        return temp_time;
}
 
  unsigned int Timer1Read(void)
{        
        temp_time = TMR1H;
        temp_time <<= 8;
        temp_time += TMR1L;
        
        return temp_time;
}
  
  void TMR1Reset(void)
  {
    TMR1ON = Disable;                 // Stop the timer 
    TMR1L = 0x00;
    TMR1H = 0x00; 
  }
 