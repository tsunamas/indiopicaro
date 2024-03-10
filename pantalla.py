# pantalla.py>
from DFRobot_RGBLCD1602 import *
from string_utils import *

class Pantalla:
	def __init__(self):
		print('pantalla init')
		self.lcd = DFRobot_RGBLCD1602(rgb_addr=0x60,col= 16,row = 2)
		numRows = 2
		numCols = 16
		
	def showNormalMessage(self, message):
		self.lcd.clear()
		self.lcd.set_cursor(0,0)
		length = len(message)
		if length < 17:
			self.lcd.print_out(message)
		elif length >16:
			self.lcd.print_out(message[0:16])
			self.lcd.set_cursor(0,1)
			self.lcd.print_out(message[16:32])
	
	def showSectionedMessage(self, message_up, message_down):
		self.lcd.clear()
		self.showMessageUp(message_up)
		self.showMessageDown(message_down)
		
	def showMessageUp(self, message):
		self.lcd.print_out(message)
		
	def showMessageDown(self, message):
		self.lcd.set_cursor(0,1)
		self.lcd.print_out(message)

	def setColor(self, r, g, b):
		self.lcd.set_RGB(r, g, b)
		
	def clear():
		self.lcd.clear()
