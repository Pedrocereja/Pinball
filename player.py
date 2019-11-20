class Player:
	
	def __init__(self): #Atributos do player
		self.vidas = 3 #Número de vidas
		self.pontuacao = 0 #Pontos
		
	def pontuar(self, pontos): #Aumentar pontuação
		self.pontuação += pontos
		#Se a pontuação exceder x tocamos uma músicas ou exibimos algo na tela
		#COCOCOCCOOMBOBREAKER
		
	def morrer(self): #Perder uma vida
		self.vidas -= 1
		if (self.vidas==0):
			self.nomear()
			self.__init__()
			
	def nomear(self):
		#to-do
