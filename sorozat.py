import random

def veletlen_dobasok():
    dobasok = [random.choice([0, 1]) for _ in range(7)]

    dobasok_kifejezes = ["FEJ" if dobas == 1 else "ÍRÁS" for dobas in dobasok]


    print("-".join(dobasok_kifejezes))

    fejek_szama = dobasok.count(1)

    return fejek_szama


def konzol_kiir(fejek_szama):
    print(f"A fejek száma: {fejek_szama}.")

