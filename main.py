from pyfirmata import Arduino, util, INPUT, OUTPUT
from time import sleep
from player import *
from arduino import *
from telas import *

#Setup
board = Arduino('/dev/ttyACM0', baudrate = 250000)
sleep(5)
it = util.Iterator(board)
it.start()

#Declaração de variáveis
player = Player()
sens_inicio = Sensor(11, 10, board)
sens_morte = Sensor(2, 10, board)
sens0 = Sensor(3, 10, board)
sens1 = Sensor(4, 10, board)
sens2 = Sensor(5, 10, board)
sens3 = Sensor(6, 10, board)
sens4 = Sensor(7, 10, board)
sens5 = Sensor(8, 10, board)
sens6 = Sensor(9, 10, board)
sens7 = Sensor(10, 10, board)

#Execução do jogo
while True:
  telaInicial(sens_inicio)#Exibe tela inicial até o lançamento da bola
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
      sleep(1)
      if (player.vidas == 0):
        player.__init__()
        break
      else:
        telaTransicao(player.vidas)
  telaFinal()
  
      
