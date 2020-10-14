import time
from messages import *

msg = Messages()

msg.introduction()

while msg.escolha != msg.cont:

	print("- - - - MENU DE CADASTRO - - - -")

	print("1 - Criar cadastro")
	print("2 - Editar cadastro")
	print("3 - Visualizar cadastro salvo")
	print("4 - Deletar cadastro salvo")
	print("5 - Ajuda com o programa")
	print("6 - Sair do programa")

	msg.escolha = int(input("Escolha um valor: "))
	
	msg.switch(msg.escolha)

input("Aperte enter para fechar")
