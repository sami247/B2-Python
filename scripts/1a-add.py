#!/bin/python3
#1a-add.py - Somme de deux nombres 
#BEN EL FAHSI Sami
#15/10/2018
    
# Fonction de convertion en int et d'addition
def convertAndAdd(a, b) :
    return int(a) + int(b)

print('Écrivez deux nombres :')

# Demande des nombres à l'utilisateur
numberOne = input()
numberTwo = input()


# Affichage de la somme si les entrées sont des nombres
if numberOne.isdigit() and numberTwo.isdigit() :
    print('La somme de ces nombres : ', convertAndAdd(numberOne, numberTwo))
