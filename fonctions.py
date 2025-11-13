from math import *
import matplotlib.pyplot as plt

# ============================================================
#  Fonctions mathématiques liées à la suite de Collatz
# ============================================================

def tab(i: int, j: int):
    """
    Retourne l'entier situé à la position (i, j) du tableau de classement.
    n = 5 si i est pair, sinon n = 1
    """
    if isinstance(i, int) and isinstance(j, int) and i >= 0 and j >= 0:
        n = 5 if i % 2 == 0 else 1
        resultat = ((2 ** (i + 1)) * (6 * j + n) - 1) // 3
        return resultat
    else:
        raise ValueError("i et j doivent être des entiers positifs")


def suivantImpaire(n: int):
    """
    Calcule le nombre impair qui suit n dans la suite de Collatz.
    """
    if isinstance(n, int) and n > 0:
        if n % 2 == 1:
            m = 3 * n + 1
            while m % 2 == 0:
                m //= 2
        else:
            while n % 2 == 0:
                n //= 2
            m = n
        return m
    else:
        raise ValueError("n doit être un entier positif")


def liste(n: int):
    """
    Retourne la liste complète de la suite de Collatz commençant par n.
    """
    if isinstance(n, int) and n > 0:
        l = [n]
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            l.append(n)
        return l
    else:
        raise ValueError("n doit être un entier positif")


def listeImpaire(n: int):
    """
    Retourne la liste de tous les termes impairs de la suite de Collatz commençant par n.
    """
    if isinstance(n, int) and n > 0:
        l = [n]
        while 1 not in l:
            n = suivantImpaire(n)
            l.append(n)
        return l
    else:
        raise ValueError("n doit être un entier positif")


# ============================================================
#  Fonctions d'analyse d'ordre et de convergence
# ============================================================

def ordre(l):
    """
    Vérifie si la liste 'l' est strictement décroissante.
    """
    if isinstance(l, (list, tuple)):
        return all(l[i] > l[i + 1] for i in range(len(l) - 1))
    else:
        raise TypeError("l doit être une liste ou un tuple")


def ordreCroissant(l):
    """
    Vérifie si la liste 'l' est strictement croissante.
    """
    if isinstance(l, (list, tuple)):
        return all(l[i] < l[i + 1] for i in range(len(l) - 1))
    else:
        raise TypeError("l doit être une liste ou un tuple")


def siConvergeant(n: int):
    """
    Vérifie si l'entier impair 'n' est convergent,
    c'est-à-dire si la suite impaire de Collatz est strictement décroissante.
    """
    l = listeImpaire(n)
    return ordre(l)


def siSemiDivergeant(n: int):
    """
    Vérifie si l'entier impair 'n' est semi-divergeant,
    c'est-à-dire si la suite impaire de Collatz est strictement croissante.
    """
    l = listeImpaire(n)
    return ordreCroissant(l)


def listeConvergeants(debut=1, fin=100):
    """
    Retourne la liste des entiers impairs convergents entre 'debut' et 'fin'.
    """
    if isinstance(debut, int) and isinstance(fin, int) and debut >= 1 and debut < fin:
        i, l = debut, []
        if debut % 2 == 0:
            i += 1
        while i <= fin:
            if siConvergeant(i):
                l.append(i)
            i += 2
        return l
    else:
        raise ValueError("Les bornes doivent être des entiers positifs avec début < fin")


def listeSemiDivergeants(debut=1, fin=100):
    """
    Retourne la liste des entiers impairs semi-divergeants entre 'debut' et 'fin'.
    """
    if isinstance(debut, int) and isinstance(fin, int) and debut >= 1 and debut < fin:
        i, l = debut, []
        if debut % 2 == 0:
            i += 1
        while i <= fin:
            if siSemiDivergeant(i):
                l.append(i)
            i += 2
        return l
    else:
        raise ValueError("Les bornes doivent être des entiers positifs avec début < fin")


def convergents_intervalle(debut: int, fin: int):
    """
    Retourne la liste des entiers impairs convergents dans l'intervalle [debut, fin].
    Un entier impair est convergent si sa liste impaire est strictement décroissante.
    """
    if isinstance(debut, int) and isinstance(fin, int) and debut >= 1 and debut < fin:
        l = []
        i = debut if debut % 2 == 1 else debut + 1  # on démarre par un impair
        while i <= fin:
            if siConvergeant(i):
                l.append(i)
            i += 2
        return l
    else:
        raise ValueError("Les bornes doivent être des entiers positifs avec début < fin")


def semi_divergeants_selon_taille(debut: int, fin: int, taille: int):
    """
    Retourne les entiers impairs semi-divergeants dans [debut, fin]
    dont la longueur de leur liste impaire est égale à 'taille'.
    """
    if (isinstance(debut, int) and isinstance(fin, int)
        and isinstance(taille, int)
        and debut >= 1 and debut < fin and taille > 0):

        l = []
        i = debut if debut % 2 == 1 else debut + 1
        while i <= fin:
            if siSemiDivergeant(i):
                if len(listeImpaire(i)) == taille:
                    l.append(i)
            i += 2
        return l
    else:
        raise ValueError("Paramètres invalides : début, fin et taille doivent être des entiers positifs avec début < fin.")


def portee(l):
    """
    Retourne le plus grand élément de la liste 'l'.
    """
    if isinstance(l, (list, tuple)):
        return max(l)
    else:
        raise TypeError("l doit être une liste ou un tuple")


def longueur(l):
    """
    Retourne la longueur de la liste 'l'.
    """
    if isinstance(l, (list, tuple)):
        return len(l)
    else:
        raise TypeError("l doit être une liste ou un tuple")


# ============================================================
#  Fonctions graphiques pour visualiser les suites impaires
# ============================================================

def tracer_liste_impaire(n: int):
    """
    Trace la suite impaire de Collatz pour un entier n.
    Chaque point représente un terme impair rencontré jusqu’à 1.
    """
    l = listeImpaire(n)
    plt.figure(figsize=(7, 4))
    plt.plot(range(len(l)), l, marker='o', linestyle='-', label=f"n = {n}")
    plt.title(f"Suite impaire de Collatz pour n = {n}")
    plt.xlabel("Indice du terme (k)")
    plt.ylabel("Valeur impaire")
    plt.grid(True)
    plt.legend()
    plt.show()


def tracer_liste_impaire_coloree(n: int):
    """
    Trace la suite impaire de Collatz avec une couleur différente
    selon le type : convergente, semi-divergeante ou oscillante.
    """
    l = listeImpaire(n)
    if ordre(l):
        couleur, typ = "green", "Convergente"
    elif ordreCroissant(l):
        couleur, typ = "red", "Semi-divergeante"
    else:
        couleur, typ = "blue", "Oscillante"

    plt.figure(figsize=(7, 4))
    plt.plot(range(len(l)), l, marker='o', color=couleur, label=f"{typ} (n = {n})")
    plt.title(f"Suite impaire de Collatz pour n = {n} — {typ}")
    plt.xlabel("Indice du terme (k)")
    plt.ylabel("Valeur impaire")
    plt.grid(True)
    plt.legend()
    plt.show()


# ============================================================
#  Fin du programme
# ============================================================
# Exemple d'utilisation :
# tracer_liste_impaire_coloree(7)
# tracer_liste_impaire_coloree(9)
# print(listeConvergeants(1, 100))
# print(listeSemiDivergeants(1, 100))
