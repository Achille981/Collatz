from math import *

def tab (i:int, j:int) :
    "Cette fonction retourne l'entier qui est à la position (i, j) du tableau de classement"
    if (isinstance(i,int)) and (isinstance(j,int)) and (i>=0) and (j>=0) :
        n = 1
        if (i % 2 == 0):
            n = 5
        resultat = ((2**(i+1))*(6*j + n)-1)//3
    else :
        resultat = "ERREUR"
    return resultat

def suivantImpaire (n : int):
    "Cette fonction calcule le nombre impaire qui suit 'n' d'après la suite de Collatz"
    if (isinstance(n, int)) and (n>0) :
        if (n % 2 == 1):
            m = 3*n + 1
            while (m % 2 == 0) :
                m //= 2
        else :
            while (n % 2 == 0) :
                n //= 2
            m = n
    else :
        m = "ERREUR"
    return m

def liste (n : int):
    "Cette fonction dresse la liste de tous les termes impaires de la suite de Collatz de premier terme 'n'."
    if (isinstance(n, int)):
        l = [n]
        while (1 not in l):
            n = suivantImpaire(n)
            l.append(n)
    else:
        l = "ERREUR"
    return l

def ordre (l):
    "Cette fonction vérifie si la liste 'l' est ordonné d'une manière décroissante."
    if (isinstance(l, list)) or (isinstance(l, tuple)):
        for i in range (len(l)-1):
            if (l[i]<l[i+1]):
                return False
        return True
    else :
        return None

def ordreCroissant (l):
    "Cette fonction vérifie si la liste 'l' est ordonné d'une manière croissante."
    if (isinstance(l, list)) or (isinstance(l, tuple)):
        for i in range (len(l)-1):
            if (l[i]>l[i+1]):
                return False
        return True
    else :
        return None

def siEntrant (n):
    "Cette fonction vérifie si l'entier naturel 'n' est un entrant."
    if (isinstance(n, int)):
        if (ordre(liste(n))):
            return True
        return False
    else:
        return None

def listeEntrants (debut = 1, fin = 100):
    "Cette fonction dresse la liste des entrants comprisent entre 'début' et 'fin'."
    if (isinstance(debut, int)) and (isinstance(fin, int)) and (debut >= 1) and (debut < fin):
        i, l = debut, []
        if (debut % 2 == 0):
            i += 1
        while i <= fin :
            if (siEntrant(i)):
                l.append(i)
            i += 2
    else :
        l = "ERREUR"
    return l
        

##########  The pitt / Grey's anatomie / chicago made / the residants #########
# 91 77 88 12

# print(ordre(liste(tab(0,0))))
# print()
# print(siEntrant(3))

print(listeEntrants(fin=1000))
