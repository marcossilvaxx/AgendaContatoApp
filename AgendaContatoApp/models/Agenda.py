from models.Pessoa import Pessoa

class Agenda:
    def __init__(self, nome, nascimento, email):
        self.proprietario = Pessoa(nome, nascimento, email)

