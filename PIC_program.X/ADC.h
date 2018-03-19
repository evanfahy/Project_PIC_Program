#ifndef ADC_H
#define	ADC_H

#include "Constants.h"

//Function Declarations
void InitialiseADC(void);
unsigned short ReadADC(void);

//Variables
unsigned short adcData = 0; //combined value of ADC result registers


#endif	/* ADC_H */

