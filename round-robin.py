""" le programme doit gerer les processus selon l'algorithme de tourniquet
class 1: processus
    args: numero,duree,arrivee
 args:
    numero,duree,arrivee,
    les processus
    liste de file d'attente
    liste ordonencement
    quantum

"""

class Processus:
    def __init__(self, numero, duree, arrivee, priorite):
        self.numero = numero
        self.duree = duree
        self.arrivee = arrivee

    def diminuer_temps(self):
        self.duree -= 1

    def __str__(self):
        return f"{self.numero}  / {self.duree} / {self.arrivee}"


p1 = Processus("P1", 5, 0, 1)
p2 = Processus("P2", 4, 0, 2)
p3 = Processus("P3", 1, 2, 3)
p4 = Processus("P4", 3, 5, 2)
p5 = Processus("P5", 0, 0, 0)
p6 = Processus("P6", 0, 0, 0)

liste_de_processus_a_traiter = []
liste_de_processus_a_traiter.append(p1)
liste_de_processus_a_traiter.append(p2)
liste_de_processus_a_traiter.append(p3)
liste_de_processus_a_traiter.append(p4)
liste_de_processus_a_traiter.append(p5)
liste_de_processus_a_traiter.append(p6)

file_1 = []
file_2 = []
file_3 = []
liste_ordonencement = []

quantum =0

while  not (p1.duree == 0 and p2.duree == 0 and p3.duree == 0 and p4.duree == 0 and p5.duree == 0 and p6.duree == 0):
    for pro in liste_de_processus_a_traiter:
        if pro.arrivee == quantum:
            file_1.append(pro)
    if len(file_1) > 0:
        if file_1[0].duree > 0:
            file_1.append(file_1[0])

            file_1[0].diminuer_temps()
            liste_ordonencement.append(file_1.pop(0))
        else:
            file_1.pop(0)
    quantum +=1

for po in liste_ordonencement:
    print(po.numero,end="-")
