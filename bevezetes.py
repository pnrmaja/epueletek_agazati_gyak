def feladat1():
    print("I/A:")
    jatek_neve:str  = input("Kérem adja meg a játékos nevét: ")
    szerepkor :str = input("Kérem adja meg a játékos szerepkörét (varázsló/harcos/egyéb): ")

    if szerepkor.lower() == "varázsló":
        elet = 2
    elif szerepkor.lower() == "harcos":
        elet = 10
    else:
        elet = 8
        
    print("I/B:")
    print(f"\nÜdvözlünk {jatek_neve}, {elet} életed van!")