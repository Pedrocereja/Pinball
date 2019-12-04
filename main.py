from pyfirmata import Arduino, util, INPUT, OUTPUT
from time import sleep
from player import Player
from arduino import Sensor
import telas

#Setup
board = Arduino('/dev/ttyACM0', baudrate = 250000)
sleep(5)
it = util.Iterator(board)
it.start()

#Declaração de variáveis
player = Player()
sens_inicio = Sensor(pin, valor)
sens_morte = Sensor(pin, valor)
sens0 = Sensor(pin, valor)
sens1 = Sensor(pin, valor)
sens2 = Sensor(pin, valor)
sens3 = Sensor(pin, valor)
sens4 = Sensor(pin, valor)
sens5 = Sensor(pin, valor)
sens6 = Sensor(pin, valor)
sens7 = Sensor(pin, valor)

#Execução do jogo
while True:
  telaInicial()#Exibe tela inicial até o lançamento da bola
  telaJogo()
  while True:
    if (sens0.status() == 1):
      player.pontuar(sens0.valor)
      telaJogo()
    if (sens1.status() == 1):
      player.pontuar(sens1.valor)
      telaJogo()
    if (sens2.status() == 1):
      player.pontuar(sens2.valor)
      telaJogo()
    if (sens3.status() == 1):
      player.pontuar(sens3.valor)
      telaJogo()
    if (sens4.status() == 1):
      player.pontuar(sens4.valor)
      telaJogo()
    if (sens5.status() == 1):
      player.pontuar(sens5.valor)
      telaJogo()
    if (sens6.status() == 1):
      player.pontuar(sens6.valor)
      telaJogo()
    if (sens7.status() == 1):
      player.pontuar(sens7.valor)
      telaJogo()
    if (sens_morte.status() == 1):
      player.morrer()
      if (player.vidas == 0):
        break
      else:
        telaTransicao(self.vidas)
  telaFinal()
  
      
