from AgendaContatoApp.models.Agenda import *
from AgendaContatoApp.models.Pessoa import *
from AgendaContatoApp.models.Contato import *
from AgendaContatoApp.models.Telefone import *
import json
from collections import namedtuple

def main():
    def para_dict(obj):
        # Se for um objeto, transforma num dict
        if hasattr(obj, '__dict__'):
            obj = obj.__dict__

        # Se for um dict, lê chaves e valores; converte valores
        if isinstance(obj, dict):
            return {k: para_dict(v) for k, v in obj.items()}
        # Se for uma lista ou tupla, lê elementos; também converte
        elif isinstance(obj, list) or isinstance(obj, tuple):
            return [para_dict(e) for e in obj]
        # Se for qualquer outra coisa, usa sem conversão
        else:
            return obj

    def criarAgenda():
        nome = str(input("Informe o nome do proprietário:\n"))
        nascimento = str(input("Informe o nascimento do proprietário:\n"))
        email = str(input("Informe o email do proprietário:\n"))

        p = Pessoa(nome, nascimento, email)

        a = Agenda(p)

        aJson = json.dumps(para_dict(a))

        arquivoJson = open("agenda.json", "w")
        arquivoJson.write(aJson)

    def incluirNovoContato():
        nome = str(input("Informe o nome do contato:\n"))
        nascimento = str(input("Informe o nascimento do contato:\n"))
        email = str(input("Informe o email do contato:\n"))

        pergT = int(input("Quantos telefones o contato tem?\n"))
        telefones = []

        for i in range(1, pergT+1):
            numero = str(input("Informe o número do Telefone %i:\n" % i))
            ddd = str(input("Informe o ddd do Telefone %i:\n" % i))
            codigo = str(input("Informe o codigo do Telefone %i:\n" % i))

            t = Telefone(numero, ddd, codigo)
            telefones.append(t)

        p = Pessoa(nome, nascimento, email)
        c = Contato(p, telefones)

        arquivoJson = open("agenda.json", "r")
        agendaJson = json.load(arquivoJson)
        arquivoJson.close()

        agendaJson = Agenda(agendaJson['proprietario'], agendaJson['contatos'])

        agendaJson.incluirContato(c)

        aJson = json.dumps(para_dict(agendaJson))

        arquivoJson = open("agenda.json", "w")
        arquivoJson.write(aJson)

    def listarTodosOsContatos():
        arquivoJson = open("agenda.json", "r")
        agendaJson = json.load(arquivoJson)
        arquivoJson.close()

        agendaJson = Agenda(agendaJson['proprietario'], agendaJson['contatos'])

        for contato in agendaJson.listarContatos():
            print(contato)

    def removerContato():
        arquivoJson = open("agenda.json", "r")
        agendaJson = json.load(arquivoJson)
        arquivoJson.close()

        agendaJson = Agenda(agendaJson['proprietario'], agendaJson['contatos'])

        nomeC = str(input("Informe o nome do contato que você quer remover:\n"))

        agendaJson.excluirContato(nomeC)

        aJson = json.dumps(para_dict(agendaJson))

        arquivoJson = open("agenda.json", "w")
        arquivoJson.write(aJson)

    def buscarContatoPorNome():
        arquivoJson = open("agenda.json", "r")
        agendaJson = json.load(arquivoJson)
        arquivoJson.close()

        agendaJson = Agenda(agendaJson['proprietario'], agendaJson['contatos'])

        nomeC = str(input("Informe o nome do contato que você quer buscar:\n"))

        contatoEncontrado = False

        for contato in agendaJson.listarContatos():
            if contato['pessoa']['nome'].lower() == nomeC.lower():
                contatoEncontrado = True
                print("========Contato encontrado========\nNome: {}\nData de nascimento: {}\nEmail: {}\nTelefones: {}"
                      .format(contato['pessoa']['nome'], contato['pessoa']['nascimento'], contato['pessoa']['email'], contato['telefones']))

        if contatoEncontrado == False:
            print("Contato não encontrado.")

    def contarQtdContatos():
        arquivoJson = open("agenda.json", "r")
        agendaJson = json.load(arquivoJson)
        arquivoJson.close()

        agendaJson = Agenda(agendaJson['proprietario'], agendaJson['contatos'])

        print("A quantidade de contatos é:", agendaJson.contarContatos())

    try:
        arquivoJson = open("agenda.json", "r")
        print("Agenda aberta.")

    except FileNotFoundError:
        criarAgenda()


if __name__ == '__main__':
    main()