from datetime import date

class Pessoa:
    def __init__(self, nome, nascimento, email):
        self.nome = nome
        dia, mes, ano = nascimento.split("/")
        self.nascimento = str(date(int(ano), int(mes), int(dia)))
        self.email = email
