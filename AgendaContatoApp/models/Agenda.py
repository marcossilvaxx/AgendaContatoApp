class Agenda:
    def __init__(self, proprietario, contatos=[]):
        self.proprietario = proprietario
        self.contatos = contatos

    def contarContatos(self):
        return len(self.contatos)

    def listarContatos(self):
        return self.contatos

    def incluirContato(self, contato):
        self.contatos.append(contato)
        print("Contato incluído.")

    def excluirContato(self, nome):
        for contato in self.contatos:
            if contato['pessoa']['nome'].lower() == nome.lower():
                self.contatos.remove(contato)
                print("Contato excluído.")
                break
