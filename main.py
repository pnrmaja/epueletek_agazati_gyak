import bevezetes
from epulet import Epulet
import sorozat
import epuletek

#bevezetes.feladat1()

""""
dobasok_szamok:list[int]=sorozat.veletlen_dobasok()
fej_szam:int=sorozat.fejek_szama(dobasok_szamok)
sorozat.konzol_kiir(fej_szam)
sorozat.file_kiir(fej_szam)
"""
epulet_lista:list[Epulet]=epuletek.feladat3()
epulet_db:int=epuletek.epuletek_szama(epulet_lista)
epuletek.magasabb_epuletek(epulet_lista)
epuletek.legoregebb_epulet(epulet_lista)
