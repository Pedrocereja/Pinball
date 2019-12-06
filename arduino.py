from pyfirmata import Arduino, util, INPUT, OUTPUT
from time import sleep

class Sensor:
	def __init__(self, pin, valor, board):
		self.pin = board.get_pin('d:{0}:i'.format(pin))
		self.valor = valor
		self.pin.enable_reporting
		sleep(0.05)
	def status(self):
		return self.pin.read()
		
#sensor = Sensor(2,500)
#while 1:
#	print(sensor.status())
#	sleep(0.05)

	
