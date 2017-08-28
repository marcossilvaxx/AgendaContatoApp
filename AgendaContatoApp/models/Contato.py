import datetime

class Contato:
    def __init__(self):
        self.criacao = datetime.date.today().strftime("%d/%m/%y")
