from math import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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


# def semi_divergeants_selon_taille(debut: int, fin: int, taille: int):
#     """
#     Retourne les entiers impairs semi-divergeants dans [debut, fin]
#     dont la longueur de leur liste impaire est égale à 'taille'.
#     """
#     if (isinstance(debut, int) and isinstance(fin, int)
#         and isinstance(taille, int)
#         and debut >= 1 and debut < fin and taille > 0):

#         l = []
#         i = debut if debut % 2 == 1 else debut + 1
#         while i <= fin:
#             if siSemiDivergeant(i):
#                 if len(listeImpaire(i)) == taille:
#                     l.append(i)
#             i += 2
#         return l
#     else:
#         raise ValueError("Paramètres invalides : début, fin et taille doivent être des entiers positifs avec début < fin.")


def semi_divergeants_selon_taille(debut: int, fin: int, taille: int):
    """
    Retourne les entiers impairs semi-divergeants dans [debut, fin]
    pour lesquels les 'taille' premiers termes de leur liste impaire
    sont strictement croissants.
    """
    if (isinstance(debut, int) and isinstance(fin, int)
        and isinstance(taille, int)
        and debut >= 1 and debut < fin and taille > 0):

        l = []
        i = debut if debut % 2 == 1 else debut + 1  # commence par un impair

        while i <= fin:
            li = listeImpaire(i)

            # Vérifie que la liste a au moins 'taille' éléments
            if len(li) >= taille:
                sous_liste = li[:taille]

                # Vérifie si les 'taille' premiers termes sont strictement croissants
                if ordreCroissant(sous_liste):
                    l.append(i)

            i += 2
        return l

    else:
        raise ValueError("Paramètres invalides : début, fin et taille doivent être des entiers positifs avec début < fin.")


def semi_divergeants_selon_taille1(debut: int, fin: int, taille: int):
    """
    Recherche, pour chaque entier impair n dans [debut, fin],
    les séquences strictement croissantes de longueur 'taille'
    dans sa liste impaire de Collatz.

    Si une telle séquence existe, on garde le couple (n, premier_terme)
    où :
        - n est l'entier de départ,
        - premier_terme est le premier nombre de la séquence croissante trouvée.
    """
    if (isinstance(debut, int) and isinstance(fin, int)
        and isinstance(taille, int)
        and debut >= 1 and debut < fin and taille > 1):

        resultats = []
        i = debut if debut % 2 == 1 else debut + 1  # commence par un impair

        while i <= fin:
            li = listeImpaire(i)
            ajoute = False  # pour éviter d’ajouter plusieurs fois le même n

            for j in range(len(li) - taille + 1):
                sous_liste = li[j:j + taille]
                if ordreCroissant(sous_liste):
                    premier = sous_liste[0]
                    resultats.append((i, premier))
                    ajoute = True
                    break  # on arrête dès qu’on trouve une séquence croissante

            i += 2

        return resultats

    else:
        raise ValueError(
            "Paramètres invalides : début, fin et taille doivent être des entiers positifs avec début < fin et taille > 1."
        )



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


# =============================================================
# Fonctions pour tracer la courbe ou surface des suites
# =============================================================


def tracer_suite_1d(u, n_max, titre="Courbe de la suite"):
    """
    Trace la courbe d'une suite u(n) pour n allant de 0 à n_max.
    
    Paramètres :
        u : fonction représentant la suite (ex : lambda n: n**2)
        n_max : entier, valeur maximale de n
        titre : texte à afficher sur le graphique
    """
    n = list(range(n_max + 1))
    valeurs = [u(i) for i in n]
    
    plt.plot(n, valeurs, marker='o')
    plt.xlabel("n")
    plt.ylabel("u(n)")
    plt.title(titre)
    plt.grid(True)
    plt.show()


def tracer_suite_2d(u, n_max, m_max, titre="Surface de la suite"):
    """
    Trace la surface d'une suite u(n,m) pour n=0..n_max et m=0..m_max.

    Paramètres :
        u : fonction de deux variables (ex : lambda n, m: n**2 + m**2)
        n_max : maximum pour n
        m_max : maximum pour m
        titre : titre du graphique
    """
    n = np.arange(0, n_max + 1)
    m = np.arange(0, m_max + 1)
    N, M = np.meshgrid(n, m)
    
    U = u(N, M)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(N, M, U)
    
    ax.set_xlabel("n")
    ax.set_ylabel("m")
    ax.set_zlabel("u(n, m)")
    ax.set_title(titre)
    
    plt.show()


def tracer_suite_liste(suite, titre="Courbe d'une suite"):
    """
    Trace une suite numérique à partir d'une liste de valeurs.
    
    Paramètre :
        suite : liste de nombres [u0, u1, u2, ...]
    """
    if not suite:
        raise ValueError("La liste de valeurs est vide.")
    
    n = list(range(len(suite)))  # indices : 0, 1, 2, ...
    
    plt.plot(n, suite, marker='o')
    plt.xlabel("n")
    plt.ylabel("u(n)")
    plt.title(titre)
    plt.grid(True)
    plt.show()


def tracer_surface_depuis_points(points, f, titre="Surface 3D"):
    """
    Trace une surface ou un nuage 3D à partir d'une liste de points (x, y)
    et d'une fonction f(x, y) = z.

    Paramètres :
        points : liste de tuples (x, y)
        f : fonction de deux variables, ex : lambda x, y: x**2 + y**2
    """
    if not points:
        raise ValueError("La liste de points est vide.")

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [f(p[0], p[1]) for p in points]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_trisurf(xs, ys, zs)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z = f(x,y)")
    ax.set_title(titre)

    plt.show()


# =============================================================
# Exemples d'utilisation des fonctions graphiques
# =============================================================

# tracer_suite_1d(lambda n: n**2, 20, "Suite u(n) = n²")
# tracer_suite_2d(lambda n, m: n**2 + m**2, 20, 20,
#                "Surface de u(n,m) = n² + m²")
# points = [(3,2), (5,6), (1,4), (7,3)]
# f = lambda x, y: x**2 + y**2  # Exemple : z = x² + y²
#
# tracer_surface_depuis_points(points, f, "Surface z = x² + y²")
#
# suite = [1, 3, 5, 6]
# tracer_suite_liste(suite, "Suite u(n)")


# ============================================================
#  Fin du programme
# ============================================================
# Exemple d'utilisation :
# tracer_liste_impaire_coloree(7)
# tracer_liste_impaire_coloree(9)
# print(listeConvergeants(1, 1000))
# print(listeSemiDivergeants(1, 100))

# print(convergents_intervalle(1, 100))
# print()
# print(semi_divergeants_selon_taille(1, 1000, 20))

# n = 1
# while n != 0 :
#     n_str=input("Salut, veuillez entrer un entier pour voir sa courbe (courbe de Collatz) ou 0 pour quitter : ")
#     n = int(n_str)

#     tracer_liste_impaire(n)
# print("Bye")


debut = 1
fin = 1000
l = listeConvergeants(debut, fin)
m, im = [], []
for i in range (len(l)) :
    if (i % 2 == 0):
        m.append(l[i])
    else :
        im.append(l[i])
print(l)
print()
print()
print(m)
print()
print(im)