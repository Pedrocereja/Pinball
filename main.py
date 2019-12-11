from pyfirmata import Arduino, util, INPUT, OUTPUT
from time import sleep
from player import *
from arduino import *
from telas import *
from testeAlinhamento import*
import pygame

#Setup
board = Arduino('/dev/ttyACM0', baudrate = 250000)
sleep(5)
it = util.Iterator(board)
it.start()
pygame.init()
pygame.mixer.music.load("SpaceCadet.mp3")
pygame.mixer.music.play(loops = -1, start = 1.2)

#Declaração de variáveis
player = Player()
sens_inicio = Sensor(4, 0, board)
sens_morte = Sensor(8, 0, board)
sens0 = Sensor(2, 10, board) #Embaixo da ponte
sens1 = Sensor(3, 15, board) #Buraco da direita
sens2 = Sensor(5, 15, board) #Buraco da esquerda
sens3 = Sensor(6, 5, board) #Ao lado do loop
sens4 = Sensor(7, 20, board) #Loop

#Desabilitação dos sensores em caso de desalinhamento
check_morte = sensorCheck(sens_morte)
check_morte.start()
check_inicio = sensorCheck(sens_inicio)
check_inicio.start()
check0 = sensorCheck(sens0)
check0.start()
check1 = sensorCheck(sens1)
check1.start()
check2 = sensorCheck(sens2)
check2.start()
check3 = sensorCheck(sens3)
check3.start()
check4 = sensorCheck(sens4)
check4.start()

#Execução do jogo
while True:
  telaInicial(sens_inicio)#Exibe tela inicial até o lançamento da bola
  telaJogo(player.vidas, player.pontuacao)
  while True:
    if (sens0.status() == 1):
      player.pontuar(sens0.valor)
    if (sens1.status() == 1):
      player.pontuar(sens1.valor)
    if (sens2.status() == 1):
      player.pontuar(sens2.valor)
    if (sens3.status() == 1):
      player.pontuar(sens3.valor)
    if (sens4.status() == 1):
      player.pontuar(sens4.valor)
    if (sens_morte.status() == 1):
      player.morrer()
      sleep(1)
      if (player.vidas == 0):
        player.__init__()
        break
      else:
        telaTransicao(player.vidas)
  telaFinal()
  
      
