from atletas import *

if __name__ == "__main__":

    corredor = Corredor("Usain Bolt", 38, 94.0)

    print(corredor)
    print(corredor.aquecer())
    print(corredor.correr())

    nadador = Nadador("Michael Phelps", 39, 90.0)

    print(nadador)
    print(nadador.aquecer())
    print(nadador.nadar())
 

    ciclista = Ciclista("Nairo Quintana", 34, 59.0)

    print(ciclista)
    print(ciclista.aquecer())
    print(ciclista.pedalar())

    triatleta = Triatleta("Fernanda Keller", 64, 56.0)

    print(triatleta)
    print(triatleta.aquecer())
    print(triatleta.realizar_maratona())
