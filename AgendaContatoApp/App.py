from AgendaContatoApp.models.Agenda import *
from AgendaContatoApp.models.Pessoa import *
from AgendaContatoApp.models.Contato import *
from AgendaContatoApp.models.Telefone import *
import json
from collections import namedtuple

def main():
    def criarAgenda():
        nome = str(input("Informe o nome do proprietário:\n"))
        nascimento = str(input("Informe o nascimento do proprietário:\n"))
        email = str(input("Informe o email do proprietário:\n"))

        p = Pessoa(nome, nascimento, email)

        a = Agenda(p)

        a.proprietario.nascimento = str(a.proprietario.nascimento)
        a.proprietario = a.proprietario.__dict__

        aJson = json.dumps(a.__dict__)

        arquivoJson = open("agenda.json", "w")
        arquivoJson.write(aJson)

    def incluirNovoContato():
        pass

    try:
        arquivoJson = open("agenda.json", "r")
        agendaJson = json.load(arquivoJson, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        print(agendaJson.proprietario.nome)
        print("Agenda aberta.")
    except FileNotFoundError:
        criarAgenda()

if __name__ == '__main__':
    main()