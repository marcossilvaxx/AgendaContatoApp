import datetime

class Contato:
    def __init__(self, pessoa, telefones=[]):
        self.criacao = str(datetime.date.today().strftime("%d/%m/%y"))
        self.pessoa = pessoa
        self.telefones = telefones

    def listarTelefones(self):
        return self.telefones