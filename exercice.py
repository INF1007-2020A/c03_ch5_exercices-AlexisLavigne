#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    mon_nombre = float(input("Entrez un nombre : "))
    if mon_nombre < 0:
        mon_nombre = -mon_nombre
    return mon_nombre




def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    return [prefixe+suffixes for prefixe in prefixes]



def prime_integer_summation() -> int:
    nombrePremier = 0
    nombre = 2
    sommes = 0
    while (nombrePremier < 100):
        for i in range(1, nombre + 1):
            if (nombre % i == 0 and i != 1 and i != nombre):
                break
            elif (i == nombre):
                nombrePremier += 1
                sommes += nombre
        nombre += 1
    return sommes

def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
