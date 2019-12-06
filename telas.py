from time import sleep

def telaInicial(sens_inicio):
  while (sens_inicio.status() == 0):
    print("Telainicial")
  #Plotar gráficos da tela inicial

def telaJogo():
  print("Tela jogo")
  sleep(1)
  
def telaTransicao(vidas):
  print("Tela transição")
  
def telaFinal():
  print("Tela final")
