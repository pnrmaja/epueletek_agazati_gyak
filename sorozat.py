import random

def veletlen_dobasok():
    print("II/A, B, C:")
    dobasok_szamok:list[int] = []
    dobasok_szoveg:list[str]= []
    
    

    for _ in range(7):
        dobas:int = random.randint(0,1)
        dobasok_szamok.append(dobas)        
    
    
    for dobas in dobasok_szamok:
        if dobas == 0:
            dobasok_szoveg.append("ÍRÁS")
        else:
            dobasok_szoveg.append("FEJ")

    print("-".join(dobasok_szoveg))
    return dobasok_szamok


def fejek_szama(dobasok_szamok:int):
     
    return dobasok_szamok.count(1)

    

def konzol_kiir(fej_szam:int):
    print("II/D, E:")
    
    
    print(f"A fejek száma: {fej_szam}.")

def file_kiir(fej_szam:int):
    print("II/F:")
    with open("fejek.txt", 'w',encoding='utf-8') as file:
        file.write(f"A fejek száma: {fej_szam}. ")






