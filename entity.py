import time

class Entity:

	def __init__(self):

		self.nome = ""
		self.idade = ""
		self.sexo = ""
		self.cpf = ""
		self.backup = []

	def create(self):

		self.nome = str(input("Informe seu nome: "))
		self.idade = str(input("Informe sua idade: "))
		self.sexo = str(input("Informe sua sexualidade: "))
		self.cpf = str(input("Informe seu CPF: "))
		self.backup = ["Nome: "+self.nome, "Idade: "+self.idade, "Sexo: "+self.sexo, "CPF: "+self.cpf]

		print("Aguarde enquanto analiso os dados...")
		time.sleep(3)

		if self.nome != "" and self.idade != "" and self.sexo != "" and self.cpf != "":
			print("\nCerto, seus dados foram salvos com sucesso!\n")

			for x in range(0,4):
				print(self.backup[x])
		else:
			print("Ocorreu um erro e não foi possível salvar os dados!")
			print("Porfavor tente realizar o cadastro novamente.")

	def edit(self):

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

	def viewer(self):

		if self.nome == "" and self.idade == "" and self.sexo == "" and self.cpf == "":

			print("Parece que você está tentando visualizar uma ficha de cadastro que ainda não foi criada.")
			print("Realize um cadastro e tente usar essa funcão novamente.")

		else:

			print("Listando ficha de cadastro atual:")

			for x in range(0,4):
				print(self.backup[x])

	def delete(self):

		if self.nome == "" and self.idade == "" and self.sexo == "" and self.cpf == "":

			print("Pelo visto você está tentando apagar um cadastro que ainda não existe...")
			print("Realize um cadastro primeiro e depois tente usar essa ação.")

		else:

			print("Estamos prestes a deletar todos os dados que foram cadastrados.\nTem certeza que deseja apagar os dados?")

			self.confirm = str(input("Digite aqui (Sim / Não): "))

			if self.confirm == "Sim":

				print("Deletando dados...")
				time.sleep(3)
				
				self.nome = ""
				self.idade = ""
				self.sexo = ""
				self.cpf = ""
				self.backup.clear()

				print("Todos os dados cadastrados foram deletados com sucesso!")

			else:

				print("Não irei deletar nada então, seus dados ainda estão salvos!")

	def helper(self):

		print("- Lançando o básico sobre o programa:")
		print("O programa não terá nenhuma atualização ou modificação, é apenas uma base de de como funciona o cadastro de uma pessoa em uma empresa ou departaento.")
		print("O código-fonte estará disponível no Github do criador (JoaoGabriel588), e pode ser analisado para fins de confiança sobre a inserção de dados como CPF.")
		print("")
		print("O programa funciona a base de escolhas numéricas e das palavras Sim e Não (somente nesse formato), então tenha um bom proveito e acompanhe os trabalhos do criador no Github.")
		print("Qualquer report ou erro comunique ao email: joao.silva588@aluno.ce.gov.br - Github: JoaoGabriel588")
		print("Todos os direitos reservados ao Criador do sistema - JGBS")

	def exit(self):

		print("Finalizando programa....")
		time.sleep(3)