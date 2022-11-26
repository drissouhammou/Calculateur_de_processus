""" le programme doit gerer les processus selon l'algorithme de tourniquet avec priorite
class 1: processus
    args:
    numero,duree,arrivee,priorite
    les processus
    liste de priorite haute
    liste de priorite moyenne
    liste de priorite bass
    liste ordonencement
    quantum
"""


class Processus:
    def __init__(self, numero, duree, arrivee, priorite):
        self.numero = numero
        self.duree = duree
        self.arrivee = arrivee
        self.priorite = priorite

    def diminuer_temps(self):
        self.duree -= 1

    def __str__(self):
        return f"{self.numero}  / {self.duree} / {self.arrivee}"


# ( numero, duree, arrivee, priorite):
p1 = Processus("P1", 2, 0, 3)
p2 = Processus("P2", 4, 0, 2)
p3 = Processus("P3", 2, 2, 1)
p4 = Processus("P4", 3, 2, 1)
p5 = Processus("P5", 2, 5, 2)
p6 = Processus("P6", 0, 0, 0)
p7 = Processus("P7", 0, 0, 0)

liste_de_processus_a_traiter = []
liste_de_processus_a_traiter.append(p1)
liste_de_processus_a_traiter.append(p2)
liste_de_processus_a_traiter.append(p3)
liste_de_processus_a_traiter.append(p4)
liste_de_processus_a_traiter.append(p5)
liste_de_processus_a_traiter.append(p6)
liste_de_processus_a_traiter.append(p7)

file_haute = []
file_moyenne = []
file_basse = []
liste_ordonencement = []

quantum = 0

while not (
        p1.duree == 0 and p2.duree == 0 and p3.duree == 0 and p4.duree == 0 and p5.duree == 0 and p6.duree == 0 and p7.duree == 0):
    for pro in liste_de_processus_a_traiter:
        if pro.arrivee == quantum:
            if pro.priorite == 1:
                file_haute.append(pro)
            elif pro.priorite == 2:
                file_moyenne.append(pro)
            elif pro.priorite == 3:
                file_basse.append(pro)

    if len(file_haute) > 0:
        if file_haute[0].duree > 0:
            file_haute.append(file_haute[0])

            file_haute[0].diminuer_temps()
            liste_ordonencement.append(file_haute.pop(0))
        else:
            file_haute.pop(0)
    elif len(file_moyenne) > 0:
        if file_moyenne[0].duree > 0:

            file_moyenne.append(file_moyenne[0])

            file_moyenne[0].diminuer_temps()
            liste_ordonencement.append(file_moyenne.pop(0))
        else:
            file_moyenne.pop(0)
    elif len(file_basse) > 0:
        if file_basse[0].duree > 0:
            file_basse.append(file_basse[0])

            file_basse[0].diminuer_temps()
            liste_ordonencement.append(file_basse.pop(0))
        else:
            file_basse.pop(0)

    quantum += 1

for po in liste_ordonencement:
    print(po.numero, end="-")
