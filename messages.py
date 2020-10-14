import time

class Messages:

	def __init__(self):

		self.cont = 6
		self.n_help = 5
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


			# # # # # # # #
			print("")
		elif self.escolha == 2:
			print("Escolheu 2")


			# # # # # # # #
			print("")
		elif self.escolha == 3:
			print("Escolheu 3")


			# # # # # # # #
			print("")
		elif self.escolha == 4:
			print("Escolheu 4")


			# # # # # # # #
			print("")
		elif self.escolha == 5:
			print("Escolheu 5")


			# # # # # # # #
			print("")
		elif self.escolha == 6:
			print("Escolheu 6")


			# # # # # # # #
			print("")