

#Fiz algumas anotações, espero que não se importe...

from abc import ABC, abstractmethod

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Produto(ABC): # Esse (ABC) acho que faz a  mesma coisa que o @, agora, tranformando essa classe em ABSTRATO!
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return {
            "modelo": self.modelo,
            "cor": self.cor,
            "preco": self.preco,
            "categoria_id": self.categoria.id,
            "categoria_nome": self.categoria.nome
        }

    @abstractmethod # Entendi esse @ agora, ele esta tranformando o cadatrar em abstrato!
    def cadastrar(self):
        pass

class Desktop(Produto): #Produto é a classe mãe de Desktop, Desktop ta herdando da classe Produto.
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte 

    def getPotenciaDaFonte(self): #Duvida!! Não entendi direito o que extamente faz o get
        return self._potenciaDaFonte

    def setPotenciaDaFonte(self, potencia): #Duvida!! Não entendi direito o que extamente faz o set 
        self._potenciaDaFonte = potencia

    def getInformacoes(self):
        info = super().getInformacoes()
        info["potenciaDaFonte"] = self._potenciaDaFonte
        return info

    def cadastrar(self):
        print(f"Desktop '{self.modelo}' cadastrado com sucesso.")

class Notebook(Produto): #Em relação a herança, Produto faz a mesma coisa que faz no desktop. Ela é a Mãe de Notebook! 
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria 

    def getTempoDeBateria(self): # Talvez entendi? não sei direito ainda o que o get faz.
        return self.__tempoDeBateria

    def setTempoDeBateria(self, tempo):
        self.__tempoDeBateria = tempo

    def getInformacoes(self):
        info = super().getInformacoes()
        info["tempoDeBateria"] = self.__tempoDeBateria
        return info

    def cadastrar(self):
        print(f"Notebook '{self.modelo}' cadastrado com sucesso.")
