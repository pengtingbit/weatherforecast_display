import math
import time

import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,1,1)),
            (LCD.UP,     'Up'    , (1,1,1)),
            (LCD.DOWN,   'Down'  , (1,1,1)),
            (LCD.RIGHT,  'Right' , (1,1,1)) )

def strcmp(str1,str2):
	if(str1 == str2):
		return 0
	if(str1 > str2):
		return 1
	if(str1 < str2):
		return -1

def load_result_file():
	file = open('result.txt','r')
	lcd.message(file.read())

while True:
	# Loop through each button and check if it is pressed.
	for button in buttons:
		if lcd.is_pressed(button[0]):
			# Button is pressed, change the message and backlight.
			lcd.clear()
			#lcd.message('Hello world!')#TBD
			if (strcmp(button[1], 'Select') == 0):
				#lcd.message('Hello')
				load_result_file()
				lcd.set_color(1.0, 1.0, 1.0)
			elif (strcmp(button[1], 'Left') == 0):
				#turn off light
				lcd.set_color(0.0, 0.0, 0.0)
