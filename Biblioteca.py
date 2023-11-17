class Animal:
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor
    def comer(self):
        print(f'{self.nome} está comendo!')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def emitirsom(self):
        print(f'{self.nome} está miando... MIAU')

class Cachorro(Animal):
    def __int__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirsom(self):
        print(f'{self.nome} está latindo... AUAU')

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirsom(self):
        print(f'{self.nome} está ronronando... ronrom')

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirsom(self):
        print(f'{self.nome} está mugindo... MUUUUU')