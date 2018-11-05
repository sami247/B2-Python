 ou du moins
#Sami Ben El Fahsi
#2/11/2018


import signal
from random import randint

# Vérifie si une variable est un nombre
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Demande un nombre à l'utilisateur
def Nombre() :

    demandenombre = input()

    while demandenombre != 'q' and not is_number(demandenombre) :
        print('entrer nombre !')
        demandenombre = input()

    if demandenombre == 'q':
        quitProgram()

    return float(asked)

# Permet de quitter le jeu
def exitgame(sig = False, frame = False) :
    
    print('Le nombre était ', toFind)
    exit()

    
    
signal.signal(signal.SIGINT, quitProgram)
signal.signal(signal.SIGTERM, quitProgram)


print('Trouvez un nombre entre 0 et 100 !')

# Variables
toFind    = randint(0, 100)
userGuess = askNumber()
totalTry  = 1


while nombre != toFind :
    
    if nombre > toFind :
        print('plus petit')
    else :
        print('plus grand!')
        
    nombre = askNumber()
    totalTry += 1
    
    
print('Touvé', toFind)
