import time
from entity import *

pessoa = Entity()

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
		print("")

	def switch(self, escolha):

		if self.escolha == 1:
			print("")

			print("Aguarde um instante...")
			time.sleep(3)

			pessoa.create()
			# # # # # # # #
			print("")
		elif self.escolha == 2:
			print("")

			print("Aguarde um instante...")
			time.sleep(3)

			pessoa.edit()
			# # # # # # # #
			print("")
		elif self.escolha == 3:
			print("")

			print("Aguarde um instante...")
			time.sleep(3)

			pessoa.viewer()
			# # # # # # # #
			print("")
		elif self.escolha == 4:
			print("")

			print("Aguarde um instante...")
			time.sleep(3)

			pessoa.delete()
			# # # # # # # #
			print("")
		elif self.escolha == 5:
			print("")

			print("Aguarde um instante...")
			time.sleep(3)

			pessoa.helper()
			# # # # # # # #
			print("")
		elif self.escolha == 6:
			print("")

			print("Aguarde um instante...")
			time.sleep(3)

			pessoa.exit()
			# # # # # # # #
			print("")