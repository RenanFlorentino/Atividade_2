class HashTable:
	def __init__(self, size):
		# Tamanho da tabela no primeiro nível
		self.size = size

		# Primeiro nível: um vetor de 10 ponteiros para tabelas do segundo nível
		self.level1 = [None] * self.size

	def first_level_hash(self, key):
		# Função hash do primeiro nível
		return hash(key) % self.size

	def second_level_hash(self, key):
		# Função hash do segundo nível
		return hash(key) % (self.size // 10)

	def insert(self, key, value):
		# Calcula o índice no primeiro nível
		index1 = self.first_level_hash(key)

		# Se o ponteiro do primeiro nível for None, cria a tabela do segundo nível
		if self.level1[index1] is None:
			self.level1[index1] = [[] for _ in range(self.size // 10)]

		# Calcula o índice no segundo nível
		index2 = self.second_level_hash(key)

		# Insere o par chave-valor na lista correspondente no segundo nível
		self.level1[index1][index2].append((key, value))

	def get(self, key):
		# Calcula o índice no primeiro nível
		index1 = self.first_level_hash(key)

		# Verifica se a tabela do segundo nível existe
		if self.level1[index1] is not None:
			# Calcula o índice no segundo nível
			index2 = self.second_level_hash(key)

			# Procura a chave no segundo nível
			for k, v in self.level1[index1][index2]:
				if k == key:
					return v

		# Se a chave não for encontrada
		return None

# Exemplo de uso:
table = HashTable(10)
table.insert("chave1", "valor1")
table.insert("chave2", "valor2")

print(table.get("chave1"))  # Saída: "valor1"
print(table.get("chave2"))  # Saída: "valor2"
print(table.get("chave3"))  # Saída: None (chave não encontrada)
