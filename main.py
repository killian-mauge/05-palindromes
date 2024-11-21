"""
Module permettant de vérifier si une chaîne de caractères (mot ou phrase) est un palindrome.
Un palindrome se lit de la même manière à l'endroit et à l'envers, 
en ignorant les accents, la casse et les caractères spéciaux.
"""
import string

#### Fonction secondaire


def ispalindrome(p):
    """
    Vérifie si une chaîne de caractères est un palindrome.
    Args:
        p (str): La chaîne de caractères à vérifier.
    Returns:
        bool: True si la chaîne est un palindrome, False sinon.
    """
    #stocke les accents
    accents = "àâäéèêëîïôöùûüç"
    sans_accents = "aaaeeeeiioouuuc"
    #stocke les caractères spéciaux et l'espace
    caracteres_speciaux = string.punctuation + " "
    #remplace les caractères avec accents en caractères sans accents
    #tout en supprimant les caractères spéciaux
    transtab = str.maketrans(accents,sans_accents,caracteres_speciaux)
    p = p.lower().translate(transtab)
    pprime = p[::-1]
    return pprime == p

#### Fonction principale


def main():

    """
    Fonction principale pour tester la fonction ispalindrome 
    avec plusieurs exemples prédéfinis.

    Affiche pour chaque mot si c'est un palindrome ou non.
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
