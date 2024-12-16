from epulet import Epulet


def feladat3():
    epulet_lista:list[Epulet]=[]
    with open("epulet.txt", "r",encoding='utf-8') as file:
        next(file)  
        for line in file:
            adatok:list[str]=line.split("$")
            epulet:Epulet=Epulet(adatok[0],adatok[1],adatok[2],float(adatok[3].replace(",",".")),int(adatok[4]),int(adatok[5]))
            epulet_lista.append(epulet)
    return epulet_lista

def epuletek_szama(epulet_lista:list[Epulet]):
    print("III/A, B:")
    db:int=len(epulet_lista)
    print(f"Az épöletek száma: {db}")
    return db

def magasabb_epuletek(epulet_lista:list[Epulet]):
    print("III/C:")
    m_lab:float = 3.280839895 
    db:int=0
    for x in epulet_lista:
        if x.magassag*m_lab > 555:
            db+=1
    print(f"Az 555 lábnál magasabb épületek száma: {db}.")

def legoregebb_epulet(epulet_lista:list[Epulet]):
    print("III/D:")
    legoregebb:Epulet=epulet_lista[0]
    for x in epulet_lista:
        if legoregebb.epult > x.epult:
            legoregebb=x

    print(f"A legöregebb épület országa: {legoregebb.orszag}")
