from lutador import *

if __name__ == "__main__":

    popo = Boxeador('Popó')
    bambam = Boxeador('Bambam')

    popo.soco(bambam)
    print(popo)
    print(bambam)

    popo.gancho(bambam)
    print(popo)
    print(bambam)

    joao = Jujitsu('João')
    falcao = Jujitsu('Falcão')
    
    joao.chave_braco(falcao)
    print(joao)
    print(falcao)

    minotauro = Muay_Thai('Minotauro')
    marreta = Muay_Thai('Marreta')
    
    marreta.chute_alto(minotauro)
    marreta.cruzado(minotauro)

    print(marreta)
    print(minotauro)

    giovana = MMA('Giovana')
    amanda = MMA('Amanda')

    amanda.superman_punch(giovana)
    giovana.chave_braco(amanda)

    print(giovana)
    print(amanda)