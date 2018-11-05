-dic.py - liste noms
#Sami BEN EL FAHSI
#15/10/2018

print('ecrivez plusieurs prenoms')

nom = input()
noms = []

while nom != 'q':
    noms.append (nom)
    nom = input()
    
print(noms)

