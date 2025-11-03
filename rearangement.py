from math import *

def tableau (i:int, j:int) :
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


# def tab (i:int, j:int) :
#     if (isinstance(i,int)) and (isinstance(j,int)) and (i>=0) and (j>=0) :
#         n = 5
#         if (i % 2 == 1):
#             n = 1
#         resultat = ((2**i)*(6*j - n)-1)/3
#     else :
#         resultat = "ERREUR"
#     return resultat
##########  The pitt / Grey's anatomie / chicago made / the residants #########
# for i in range (10):
#     print()
#     for j in range (10):
#         print(tableau(i,j),end="  ")

print(suivantImpaire(tableau(0,0)))
