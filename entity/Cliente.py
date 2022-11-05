class Cliente:
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.email = ""

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email