# Útulek pro zvířata


def vytvor_utulek():
    return {}


def pridej_zvire(utulek, jmeno, druh, vek):
    utulek[jmeno] = {
        "druh": druh,
        "vek": vek
    }


def vypis_zvirata(utulek):
    for jmeno, info in utulek.items():
        print(f"{jmeno} je {info['druh']} a je jí/mu {info['vek']} let.")


def vypis_podle_druhu(utulek, druh):
    for jmeno, info in utulek.items():
        if info["druh"] == druh:
            print(f"{jmeno} je {info['druh']} a je mu {info['vek']} let.")


utulek = vytvor_utulek()
pridej_zvire(utulek, "packa", "kočka", 3)
pridej_zvire(utulek, "flíček", "pes", 5)

print("Všechna zvířata v útulku:")
vypis_zvirata(utulek)

print("Jen psi v útulku:")
vypis_podle_druhu(utulek, "pes")