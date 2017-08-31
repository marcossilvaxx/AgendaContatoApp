class Agenda:
    def __init__(self, proprietario):
        self.proprietario = proprietario
        self.contatos = []
        print("Agenda criada com sucesso.")

    def contarContatos(self):
        return len(self.contatos)

    def listarContatos(self):
        return self.contatos

    def incluirContato(self, contato):
        self.contatos.append(contato)
        print("Contato incluído.")

    def excluirContato(self, nome):
        for contato in self.contatos:
            if contato.pessoa.nome == nome:
                self.contatos.remove(contato)
                break
        print("Contato excluído.")