-save.py
# Sami BEN EL FAHSI 
# 11/11/18
# Script permettant de sauvegarder un dossier predefini dans une archive et le déplace

import shutil
import os
import gzip
import sys
from time import sleep
import signal




# fonctions


def createArchive(archiveName, toArchiveDirectory, dataDirectory):
    shutil.make_archive(archiveName, "gztar")
    shutil.move(archiveName + ".tar.gz", dataDirectory)



# signaux d'arret 



def checkSignal(sig, frame):
    sys.stderr.write("Erreur : Archivage interompu")
    return exit()




# fonction de comparaison




def checkSpace(archive, dest):
    sizeArchive = os.path.getsize(archive + ".tar.gz")
    sizeDest = shutil.disk_usage(dest)

    if sizeDest.free > sizeArchive:
        return True
    else:
        return False

signal.signal(signal.SIGINT, checkSignal)
signal.signal(signal.SIGTERM, checkSignal)

# variables


toArchiveDirectory = "D:/Github/B2-Python"
archiveName = os.path.expanduser("~/B2-Pyton")
dataDirectory = os.path.expanduser("~/Data/")



# on verifie les droits utilisateurs sur la destination


if os.access(toArchiveDirectory, os.R_OK and os.W_OK):

    # on verifie les droits utilisateurs sur la destination


    if os.access(dataDirectory, os.R_OK and os.W_OK):



        # crée un dossier au chemin en parametre si il n'existe pas


        if not os.path.isdir(dataDirectory):
            os.makedirs(dataDirectory)



        # on verifie si une archive a deja etait faite et on compare les deux


        shutil.make_archive(archiveName, "gztar", toArchiveDirectory)
        



        # on vérifie l'espace sur la cible (user/)



        if checkSpace(archiveName, "~/"):

            if os.path.exists(dataDirectory + archiveName + ".tar.gz"):
                with gzip.open(dataDirectory + archiveName + ".tar.gz") as file:
                    oldArchive = file.read()

                with gzip.open(archiveName + ".tar.gz") as file:
                    newArchive = file.read()

                if oldArchive != newArchive:
                    os.remove(dataDirectory + archiveName + ".tar.gz")
                    createArchive(archiveName, toArchiveDirectory, dataDirectory)
                    sys.stdout.write("Complete : Archive mise a jour")

                else:
                    sys.stderr.write("Erreur : L'archive existe deja")

            else:
                createArchive(archiveName, toArchiveDirectory, dataDirectory)
                sys.stdout.write("Complete : L'archive a ete cree")

        else:
            sys.stderr.write("Erreur : pas assez de place disponible dans le dossier de destination")
    else:
        sys.stderr.write("Erreur : vous n'avez pas les droits sur le fichier de destination")

else:
    sys.stderr.write("Erreur : vous n'avez pas les droits sur le fichier a archiver")-save.py
# Sami BEN EL FAHSI 
# 11/11/18
# Script permettant de sauvegarder un dossier predefini dans une archive et le déplace

import shutil
import os
import gzip
import sys
from time import sleep
import signal




# fonctions


def createArchive(archiveName, toArchiveDirectory, dataDirectory):
    shutil.make_archive(archiveName, "gztar")
    shutil.move(archiveName + ".tar.gz", dataDirectory)



# signaux d'arret 



def checkSignal(sig, frame):
    sys.stderr.write("Erreur : Archivage interompu")
    return exit()




# fonction de comparaison




def checkSpace(archive, dest):
    sizeArchive = os.path.getsize(archive + ".tar.gz")
    sizeDest = shutil.disk_usage(dest)

    if sizeDest.free > sizeArchive:
        return True
    else:
        return False

signal.signal(signal.SIGINT, checkSignal)
signal.signal(signal.SIGTERM, checkSignal)

# variables


toArchiveDirectory = "D:/Github/B2-Python"
archiveName = os.path.expanduser("~/B2-Pyton")
dataDirectory = os.path.expanduser("~/Data/")



# on verifie les droits utilisateurs sur la destination


if os.access(toArchiveDirectory, os.R_OK and os.W_OK):

    # on verifie les droits utilisateurs sur la destination


    if os.access(dataDirectory, os.R_OK and os.W_OK):



        # crée un dossier au chemin en parametre si il n'existe pas


        if not os.path.isdir(dataDirectory):
            os.makedirs(dataDirectory)



        # on verifie si une archive a deja etait faite et on compare les deux


        shutil.make_archive(archiveName, "gztar", toArchiveDirectory)
        



        # on vérifie l'espace sur la cible (user/)



        if checkSpace(archiveName, "~/"):

            if os.path.exists(dataDirectory + archiveName + ".tar.gz"):
                with gzip.open(dataDirectory + archiveName + ".tar.gz") as file:
                    oldArchive = file.read()

                with gzip.open(archiveName + ".tar.gz") as file:
                    newArchive = file.read()

                if oldArchive != newArchive:
                    os.remove(dataDirectory + archiveName + ".tar.gz")
                    createArchive(archiveName, toArchiveDirectory, dataDirectory)
                    sys.stdout.write("Complete : Archive mise a jour")

                else:
                    sys.stderr.write("Erreur : L'archive existe deja")

            else:
                createArchive(archiveName, toArchiveDirectory, dataDirectory)
                sys.stdout.write("Complete : L'archive a ete cree")

        else:
            sys.stderr.write("Erreur : pas assez de place disponible dans le dossier de destination")
    else:
        sys.stderr.write("Erreur : vous n'avez pas les droits sur le fichier de destination")

else:
    sys.stderr.write("Erreur : vous n'avez pas les droits sur le fichier a archiver")-save.py
# Sami BEN EL FAHSI 
# 11/11/18
# Script permettant de sauvegarder un dossier predefini dans une archive et le déplace

import shutil
import os
import gzip
import sys
from time import sleep
import signal




# fonctions


def createArchive(archiveName, toArchiveDirectory, dataDirectory):
    shutil.make_archive(archiveName, "gztar")
    shutil.move(archiveName + ".tar.gz", dataDirectory)



# signaux d'arret 



def checkSignal(sig, frame):
    sys.stderr.write("Erreur : Archivage interompu")
    return exit()




# fonction de comparaison




def checkSpace(archive, dest):
    sizeArchive = os.path.getsize(archive + ".tar.gz")
    sizeDest = shutil.disk_usage(dest)

    if sizeDest.free > sizeArchive:
        return True
    else:
        return False

signal.signal(signal.SIGINT, checkSignal)
signal.signal(signal.SIGTERM, checkSignal)

# variables


toArchiveDirectory = "D:/Github/B2-Python"
archiveName = os.path.expanduser("~/B2-Pyton")
dataDirectory = os.path.expanduser("~/Data/")



# on verifie les droits utilisateurs sur la destination


if os.access(toArchiveDirectory, os.R_OK and os.W_OK):

    # on verifie les droits utilisateurs sur la destination


    if os.access(dataDirectory, os.R_OK and os.W_OK):



        # crée un dossier au chemin en parametre si il n'existe pas


        if not os.path.isdir(dataDirectory):
            os.makedirs(dataDirectory)



        # on verifie si une archive a deja etait faite et on compare les deux


        shutil.make_archive(archiveName, "gztar", toArchiveDirectory)
        



        # on vérifie l'espace sur la cible (user/)



        if checkSpace(archiveName, "~/"):

            if os.path.exists(dataDirectory + archiveName + ".tar.gz"):
                with gzip.open(dataDirectory + archiveName + ".tar.gz") as file:
                    oldArchive = file.read()

                with gzip.open(archiveName + ".tar.gz") as file:
                    newArchive = file.read()

                if oldArchive != newArchive:
                    os.remove(dataDirectory + archiveName + ".tar.gz")
                    createArchive(archiveName, toArchiveDirectory, dataDirectory)
                    sys.stdout.write("Complete : Archive mise a jour")

                else:
                    sys.stderr.write("Erreur : L'archive existe deja")

            else:
                createArchive(archiveName, toArchiveDirectory, dataDirectory)
                sys.stdout.write("Complete : L'archive a ete cree")

        else:
            sys.stderr.write("Erreur : pas assez de place disponible dans le dossier de destination")
    else:
        sys.stderr.write("Erreur : vous n'avez pas les droits sur le fichier de destination")

else:
    sys.stderr.write("Erreur : vous n'avez pas les droits sur le fichier a archiver")
