import time

class Messages:

	def __init__(self):

		self.n_help = 6
		self.escolha = 0

	def introduction(self):

		print("Programa baseado como funciona um cadastro em qualquer tipo de sistema/programa")
		time.sleep(3)

		print("Para mais ajuda digite o número "+ str(self.n_help) +" e aperte 'Enter' para ver como tudo funciona")

		print("Aguarde...")
		time.sleep(5)

	def switch(self, escolha):

		if self.escolha == 1:
			print("Escolheu 1")
		elif self.escolha == 2:
				print("Escolheu 2")
		elif self.escolha == 3:
				print("Escolheu 3")
		elif self.escolha == 4:
				print("Escolheu 4")
		elif self.escolha == 5:
				print("Escolheu 5")