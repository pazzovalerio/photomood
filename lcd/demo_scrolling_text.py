#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Example: Scrolling text on display if the string length is major than columns in display.
# Created by Dídac García.

# Import necessary libraries for communication and display use
import drivers
from time import sleep

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

# Main body of code
try:
	print("Press CTRL + C to stop this script!")

	def long_string(display, text='', num_line=1, num_cols=16):
		""" 
		Parameters: (driver, string to print, number of line to print, number of columns of your display)
		Return: This function send to display your scrolling string.
		"""
		if len(text) > num_cols:
			display.lcd_display_string(text[:num_cols], num_line)
			sleep(1)
			for i in range(len(text) - num_cols + 1):
				text_to_print = text[i:i+num_cols]
				display.lcd_display_string(text_to_print, num_line)
				sleep(0.3)
			sleep(1)
		else:
			display.lcd_display_string(text, num_line)


	# Example of short string
	long_string(display, "Avvio in corso", 1)
	sleep(1)

	# Example of long string
	long_string(display, "PhotoBoot By Valex     |  Per assistenza ", 2)
	display.lcd_clear()
	long_string(display, "Email :", 1)
	long_string(display, "coccia.valerio@gmail.com ", 2)
	sleep(3)
	display.lcd_clear()
	long_string(display, "Telefono : ", 1)
	long_string(display, "3451238135", 2)
	sleep(3)
	display.lcd_clear()

	while True:
		# An example of infinite scrolling text
		long_string(display, "CPU : 50% ", 1)
		long_string(display, "RAM : 50% ", 2)
		sleep(4)
		display.lcd_clear()
		long_string(display, "MEMORIA : 50% ", 1)
		long_string(display, "WIFI    : 50%", 2)
		sleep(4)
		display.lcd_clear()
		long_string(display, "ID      : 00", 1)
		long_string(display, "GETTONI : 00", 2)
		sleep(4)
		display.lcd_clear()
		long_string(display, "COIN   : 00", 1)
		long_string(display, "CREDIT : 00 ", 2)
		sleep(4)
		display.lcd_clear()
except KeyboardInterrupt:
	# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
	print("Cleaning up!")
	display.lcd_clear()
