#include <stdio.h>
#include <wiringPi.h>

#define A	22
#define AA	23
#define B	24
#define BB	25

#define SW	21
#define TIME	800
void initialize(void);
void iris_control(int a, int b, int c, int d);

void iris_open(void);
void iris_close(void);

void initialize(void)
{
	pinMode(22,OUTPUT);
	pinMode(23,OUTPUT);
	pinMode(24,OUTPUT);
	pinMode(25,OUTPUT);
	pinMode(21,INPUT);	
}

void iris_control(int a, int b, int c, int d)
{
	digitalWrite(A,a);
	digitalWrite(AA,b);
	digitalWrite(B,c);
	digitalWrite(BB,d);
}

void iris_open(void)
{
	iris_control(1,0,1,0);
	delay(TIME);
	iris_control(0,1,1,0);
	delay(TIME);
	iris_control(0,1,0,1);
	delay(TIME);
	iris_control(1,0,0,1);
	
}

void iris_close(void)
{
	
	iris_control(1,0,0,1);
	delay(TIME);
	iris_control(0,1,0,1);
	delay(TIME);
	iris_control(0,1,1,0);
	delay(TIME);
	iris_control(1,0,1,0);
}
int main(void)
{	
	initialize();
	if(wiringPiSetup() == -1) return 1;
	while(1)
	{
		if(digitalRead(SW) == 0)
			iris_open();
		else
			iris_close();
	}

	return 0;
}
