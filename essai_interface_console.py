from init import *
import os

def add():
    """
    option de creation
    """
    os.system("cls")
    print("rentrer les elements suivants :")
    aTables = input("nom de la table : ")
    aLhs = input("partie gauche de la dependance fonctionnelle : ")
    aRhs = input("partie droite de la dependance fonctionnelle : ")

    if aRhs.count(" ") != 0:
        print("error synthax")
        add()
    else:
        insertDep(aTables, aLhs, aRhs)
        print ("votre dependance a bien ete ajoutee")
        main_menu()

def edit():
    """
    option de modification
    """
    tableau = getAllDep()
    if len(tableau)!= 0:
        print("la table ne contient aucun element a modifier")
    else:
        print("quelle ligne voulez-vous modifier?")
        increment = 1
        for line in tableau:
            print(increment+".  Table: "+line[0]+"relation: "+line[1]+" --> "+line[2])
            increment  += 1
        
        try:
            a = input("numero de la ligne : ")
            nbre = float(a)
            if nbre >= (len(tableau) -1) or nbre <= 0:
                print("error integer")
           
           
            else:
                print("que voulez-vous modifier?")
                print("1. table")
                print("2. lhs")
                print("3. rhs")
                b = input("entrez le nbre: ")
                newnbre = float(b)
                new = input("rentrez les nouvelles donnees :")
                if newnbre == 1:
                    editTableDep(tableau[nbre -1][0],tableau[nbre -1][1],tableau[nbre -1][2],new)
                elif newnbre == 2:
                    ediLhsDep(tableau[nbre -1][0],tableau[nbre -1][1],tableau[nbre -1][2],new):
                elif newnbre == 3:
                    if new.count(" ") != 0:
                        print("error syntax")
                        edit()
                    else:
                        editRhsDep(tableau[nbre -1][0],tableau[nbre -1][1],tableau[nbre -1][2],new):
                print("votre donnee a bien ete modifiee")
                main_menu()
        except ValueError:
            print("invalid syntax, try again")
        

def delete():
    """
    option de suppression
    """
    tableau = getAllDep()
    if len(tableau)!= 0:
        print("la table ne contient aucun element a supprimer")
    else:
        print("quelle ligne voulez-vous supprimer?")
        increment = 1
        for line in tableau:
            print(increment+".  Table: "+line[0]+"relation: "+line[1]+" --> "+line[2])
            increment += 1

        try: 
            a = input("numero de la ligne : ")
            nbre = float(a)
            if nbre >= (len(tableau) -1) or nbre <= 0:
                print("error integer")
            else:
                verif = input("la suppression est definitive voulez-vous vraiment continuer?(Y/N)")
                if verif == "Y" or verif == "y":
                    removeDep(tableau[nbre -1][0],tableau[nbre -1][1],tableau[nbre -1][2])
                    print("votre dependance a bien ete supprimee")
                    main_menu()
                elif verif == "N" or verif == "n":
                    delete()
                else:
                    print("erreur synthaxe")
                    delete()
        except ValueError:
            print("invalid syntax, try again")

def analyse():
    """
    option d analyse
    """
    tableau = getAllDep()
    if len(tableau)!= 0:
        print("la table ne contient aucun element a analyser")
    else:
        print("quelle ligne voulez-vous analyser?")
        increment = 1
        for line in tableau:
            print(increment+".  Table: "+line[0]+"relation: "+line[1]+" --> "+line[2])
            increment += 1

    try:
        a = input("numero de la ligne : ")
        nbre = float(a)
        if nbre >= (len(tableau) -1) or nbre <= 0:
           print("error integer")
           
           
        else:
           print("que voulez-vous faire?")
           print("1. determiner les cles et supercles")
           print("2. determiner les consequences logiques")
           print("3. determiner la cloture d un ensemble d attributs")
           print("4. restreindre sur le schema")
           print("5. BCNF ou 3NF")
           nbre = input("entrez le nbre: ")
    except ValueError:
        print("invalid syntax, try again")

def main_menu():
    """
    fonction menu de base du programme
    """
    os.system("cls")
    print("Veuillez choisir votre fonctionnalite :")
    print("1. ajouter")
    print("2. modifier")
    print("3. supprimer")
    print("4. analyse")
    print("5. quitter")

    try:
        a = input("entrez le nombre : ")
        fonctio = float(a)

        if fonctio == 1:
            add()
        elif fonctio == 2:
            edit()
        elif fonctio == 3:
            delete()
        elif fonctio == 4:
            analyse()
        elif fonctio == 5:
            print("goodbye")
        else:
            print("invalid number, try again")
            main_menu()
    except ValueError:
        print("invalid syntax, try again")
        main_menu()

def init():
    bdd=input("inserer la base de donnee:")
    connect(bdd)
    main_menu()

init()