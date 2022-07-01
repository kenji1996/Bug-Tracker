from flask_restplus import Model
from Bug import Bug

class Projeto:

    def __init__(self, nome) -> None:
        self.nome = nome
        self.bugs = []
        self.bugs_resolvidos = []

    def adicionar_bug(self, bug : Bug) -> None:
        self.bugs.append(bug)

    def remover_bug(self, bug : Bug) -> None:
        self.bugs.remove(bug)

    def adicionar_bug_resolvido(self, bug : Bug) -> None:
        self.bugs.append(bug)

    def remover_bug_resolvido(self, bug : Bug) -> None:
        self.bugs.remove(bug)