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

def liste (n):
    "Cette fonction dresse la liste complète de la suite de Collatz de premier terme 'n'."
    if (isinstance(n, int)) and (n>0):
        l=[n]
        while (n!=1):
            if (n%2 == 0):
                n//=2
            else:
                n = 3*n +1
            l.append(n)
    else:
        l = "ERREUR"
    return l

def listeImpaire (n : int):
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
        i = 0
        while i < (len(l) - 1):
            if (l[i]<l[i+1]):
                return False
            i += 1
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

def siConvergeant (n):
    "Cette fonction vérifie si l'entier naturel 'n' converge vers 1."
    if (isinstance(n, int)):
        if (ordre(liste(n))):
            return True
        return False
    else:
        return None

def siSemiDivergeant (n):
    "Cette fonction vérifie si l'entier naturel 'n' diverge."
    if (isinstance(n, int)):
        if (ordreCroissant(liste(n))):
            return True
        return False
    else:
        return False

def listeConvergeants (debut = 1, fin = 100):
    "Cette fonction dresse la liste des entiers convergeants comprisent entre 'début' et 'fin'."
    if (isinstance(debut, int)) and (isinstance(fin, int)) and (debut >= 1) and (debut < fin):
        i, l = debut, []
        if (debut % 2 == 0):
            i += 1
        while i <= fin :
            if (siConvergeant(i)):
                l.append(i)
            i += 2
    else :
        l = "ERREUR"
    return l

def listeSemiDivergeants (debut = 1, fin = 100):
    "Cette fonction dresse la liste des semi-divergeants comprisent entre 'debut' et 'fin."
    if (isinstance(debut, int)) and (isinstance(fin, int)) and (debut >= 1) and (debut < fin):
        i, l = debut, []
        if (debut % 2 == 0):
            i += 1
        while i <= fin :
            if (siSemiDivergeant(i)):
                l.append(i)
            i += 2
    else :
        l = "ERREUR"
    return l

def portee (l):
    "Cette fonction retourne le nombre le plus grand de la liste 'l'."
    if (isinstance(l, list)) or (isinstance(l, tuple)):
        return max(l)
    else :
        return "ERREUR"

def longueur (l):
    "Cette fonction retourne la longueur de la liste 'l'."
    if (isinstance(l, list)) or (isinstance(l, tuple)):
        return len(l)
    else :
        return "ERREUR"

##########  The pitt / Grey's anatomie / chicago made / the residants #########
# 91 77 88 12

