"""
Ce module sert a utiliser la reacine carré de la bibliothèque
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Test si les nombres sont premiers
    Args:
        p: valeur entiere positive
    Returns: le booléen prem
    """
    # votre code ici
    prem=True
    if p in (0,1):
        prem=False
    for i in range (1,p):
        if p%i==0 and i!=1:
            prem=False
    return prem

#### Fonction principale


def main():
    """
    Appelle la isprime 99 fois, de 0 à 99
    Et affiche les nombres premiers 
    Args:
        None
    Returns: 
        None
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
