import time

class Entity:

	def __init__(self):

		self.nome = ""
		self.idade = ""
		self.sexo = ""
		self.cpf = ""
		self.backup = []

	def cadastrar(self):

		self.nome = str(input("Informe seu nome: "))
		self.idade = str(input("Informe sua idade: "))
		self.sexo = str(input("Informe sua sexualidade: "))
		self.cpf = str(input("Informe seu CPF: "))
		self.backup = ["Nome: "+self.nome, "Idade: "+self.idade, "Sexo: "+self.sexo, "CPF: "+self.cpf]

		print("Aguarde enquanto analiso os dados...")
		time.sleep(3)

		if self.nome != "" and self.idade != "" and self.sexo != "" and self.cpf != "":
			print("Certo, seus dados foram salvos com sucesso!")

			for x in range(0,4):
				print(self.backup[x])
		else:
			print("Ocorreu um erro e não foi possível salvar os dados!")
			print("Porfavor tente realizar o cadastro novamente.")

	def editar(self):

		if self.nome == "" and self.idade == "" and self.sexo == "" and self.cpf == "":
			print("Parece que você ainda não realizou um cadastro!")
			print("Volte e realize um cadastro para poder usar essa ação.")
		else:

			print("Parece que você já realizou um cadastro, podemos editar os dados já salvos se quiser.")
			print("Você deseja atualizar os dados ou não? (Sim / Não)")

			self.confirm = str(input("Digite aqui: "))

			if self.confirm == "Sim":
				print("Vamos atualizar seus dados...")
				time.sleep(3)

				self.nome = str(input("Informe seu novo nome: "))
				self.idade = str(input("Informe sua nova idade: "))
				self.sexo = str(input("Informe sua nova sexualidade: "))
				self.cpf = str(input("Informe seu novo CPF: "))

				self.backup.clear()
				self.backup.append("Nome: "+self.nome)
				self.backup.append("Idade: "+self.idade)
				self.backup.append("Idade: "+self.sexo)
				self.backup.append("CPF: "+self.cpf)

				print("Dados atualizados! Confira logo abaixo:")

				for x in range(0,4):
					print(self.backup[x])
			else:

				print("Certo, não vamos atualizar nenhum dado seu.")