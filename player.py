class Player:
	
	def __init__(self): #Atributos do player
		self.vidas = 3 #Número de vidas
		self.pontuacao = 0 #Pontos
		
	def pontuar(self, pontos): #Aumentar pontuação
		self.pontuacao += pontos
		#Ideias:
		#Se a pontuação exceder x tocamos uma músicas ou exibimos algo na tela
		#COCOCOCCOOMBOBREAKER
		
	def morrer(self): #Perder uma vida
		self.vidas -= 1
		if (self.vidas==0): #Caso as vidas cheguem em 0 o jogo reseta
			self.nomear()
		#Ideia: caso o player demore demais para jogar a próxima vida, o jogo reseta
			
	def nomear(self):
		print("nomear")
		#to-do: definir a função em que o player coloca seu nome no scoreboard
		#É preciso a interface gráfica da Luana&Mateus
