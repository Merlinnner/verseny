class Termek():
    def __init__(self, nev ,ar):
        self.nev = nev
        self.ar = ar

def meretek(bemenet):
    if "nagy" in bemenet:
        meret = "nagy"
        szorzo = 1.5
    elif "közepes" in bemenet:
        meret = "közepes"
        szorzo = 1.2
    elif "kicsi" in bemenet or "kis" in bemenet:
        meret = "kicsi"
        szorzo = 1.0
    else:
        meret = ""
        szorzo = 1.0
    return meret, szorzo

def extrafeltetek():
    print("Kiszolgáló: Szeretnél rá extra feltétet? Ha igen, mit?")
    extrafeltet = input("Felhasználó: ").lower()
    extra = []
    if "nem" in extrafeltet:
        return None
    else:
        if "kukorica" not in extrafeltet and "gomba" not in extrafeltet and "sonka" not in extrafeltet:
            return extrafeltetek()
        if "kukorica" in extrafeltet:
            extra.append("kukorica")
        if "gomba" in extrafeltet:
            extra.append("gomba")
        if "sonka" in extrafeltet:
            extra.append("sonka")
    return extra

def kosarform(kosar):
    rendeles = {}
    for item in kosar:
        if item.nev not in rendeles.keys():
            rendeles[item.nev] = 0
        rendeles[item.nev] += 1
    lista = []
    for item in rendeles:
        db = ""
        if rendeles[item] == 1:
            db = "egy"
        else:
            db = str(rendeles[item]) + " db"
        lista.append(f"{db} {item}")
    return ', '.join(lista)

def rendeles(bemenet):
    global kosar
    if "kukorica" in bemenet:
        meret, szorzo = meretek(bemenet)
        while meret == "":
            print("Kiszolgáló: Milyen méretű kukoricás pizzát szeretnél?")
            meret, szorzo = meretek(input("Felhasználó: ").lower())
        extra = extrafeltetek()
        if extra == None:
            kosar.append(Termek(f"{meret} kukoricás pizza",3050 * szorzo))
        else:
            kosar.append(Termek(f"{meret} kukoricás pizza +{' +'.join(extra)}",3050 * szorzo + len(extra) * 100))
    elif "sonkás" in bemenet:
        meret, szorzo = meretek(bemenet)
        while meret == "":
            print("Kiszolgáló: Milyen méretű sonkás pizzát szeretnél?")
            meret, szorzo = meretek(input("Felhasználó: ").lower())
        extra = extrafeltetek()
        if extra == None:
            kosar.append(Termek(f"{meret} sonkás pizza",3100 * szorzo))
        else:
            kosar.append(Termek(f"{meret} sonkás pizza +{' +'.join(extra)}",3100 * szorzo + len(extra) * 100))
    elif "szalámi" in bemenet:
        meret, szorzo = meretek(bemenet)
        while meret == "":
            print("Kiszolgáló: Milyen méretű szalámis pizzát szeretnél?")
            meret, szorzo = meretek(input("Felhasználó: ").lower())
        extra = extrafeltetek()
        if extra == None:
            kosar.append(Termek(f"{meret} szalámis pizza",3300 * szorzo))
        else:
            kosar.append(Termek(f"{meret} szalámis pizza +{' +'.join(extra)}",3300 * szorzo + len(extra) * 100))
    elif "víz" in bemenet or "viz" in bemenet:
        kosar.append(Termek("víz",250))
    elif "kóla" in bemenet:
        kosar.append(Termek("kóla",750))
    elif "fanta" in bemenet:
        kosar.append(Termek("fanta",650))
    elif "pizza" in bemenet:
        print("Kiszolgáló: Milyen pizzát?")
    elif "mit lehet" in bemenet:
        print("Kiszolgáló: Pizzák: Sonkás, Kukoricás, Szalámis, minegyik 3 méretben: kicsi, közepes és nagy")
        print("Kiszolgáló: Italok: víz, kóla, fanta")
        print("Kiszolgáló: Extra feltétek: sonka, kukorica, gomba")
    else:
        print("Kiszolgáló: Elnézést, ezt nem értettem.")

def Befejez():
    global kosar
    osszeg = 0
    osszegzes = ""
    for item in kosar:
        osszegzes += f"{item.nev}\t{int(item.ar)} Ft\n"
        osszeg += item.ar
    osszegzes += f"Végösszeg\t{int(osszeg)} Ft\n"
    print("Összegzés (mentve a rendeles.txt fájlba):")
    print("----------")
    print(osszegzes,end="")
    print("----------")
    with open("rendeles.txt","w",encoding="UTF-8") as file:
        file.write(osszegzes)
kosar = []
print("Kiszolgáló: Üdvözöllek a pizzériánkban! Mit szeretnél rendelni?")
rendeles(input("Felhasználó: ").lower())
while True:
    if len(kosar) > 0:
        print(f"Tehát lesz {kosarform(kosar)}. Szeretnél valami mást is?")
    bemenet = input("Felhasználó: ").lower()
    if "nem" in bemenet or "ennyi" in bemenet:
        Befejez()
        break
    else:
        rendeles(bemenet)

