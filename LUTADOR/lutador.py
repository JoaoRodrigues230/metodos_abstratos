from abc import ABC, ABCMeta, abstractmethod

class Lutador(ABC):
    nome : str
    energia : float

    def __init__(self, n:str):
        self.nome = n
        self.energia = 100.0
    
    def soco(self, oponente):
        oponente.energia -= 5.5
    
    def __str__(self):
        return f"Nome: {self.nome} | Energia: {self.energia:.2f}%"
    
class Boxeador(Lutador):
    def cruzado(self, oponente):
        oponente.energia -= 10.2
    
    def gancho(self, oponente):
        oponente.energia -= 20.0

class Jujitsu(Lutador):
    def chave_braco(self, oponente):
        oponente.energia -= 100.0

class Muay_Thai(Boxeador):
    def chute_alto(self, oponente):
        oponente.energia -= 15.4

class MMA (Muay_Thai, Jujitsu):
    def superman_punch(self, oponente):
        oponente.energia -= 53.2


