print("Uczę się")
print("Pythona! :)")
mojeimie = "Paulina Bugajska"
print(mojeimie)
mojamiejscowosc = "Gdańsk "
mojaulubionaksiazka = "AuthomateTheBoringStuffWithPython"
print('Kubuś Puchatek'.lower())
print(mojaulubionaksiazka.lower())
print(mojamiejscowosc.strip())
print('Kubuś Puchatek'.find('Pu'))
print('Kubuś Puchatek'.find('Bu'))

def sum(dzien, miesiac, rok):
    return dzien + miesiac + rok
print(sum(28, 6, 2023))

#print(2/0)

def change_name(imie):
    return 'Jakub'

def wymien_imie_nazwisko(imie, nazwisko):
    imie = change_name(imie)
    imie_nazwisko = imie + ' ' + nazwisko
    return imie_nazwisko.title()

wymienione_imie_nazwisko = wymien_imie_nazwisko(imie = 'paulina', nazwisko = 'bugajska')
print(wymienione_imie_nazwisko)

nowe_imie = change_name("Paulina")
print(nowe_imie)


lista_uczestnikow = ['Kamil']

def zaaktualizuj_liste_uczestnikow(ls, imie):
    ls.append(imie)
    return ls

zaaktualizuj_liste_uczestnikow(lista_uczestnikow, "Dorota")

print(lista_uczestnikow)

uczestnicy = ['Dorota', 'Kamil', 'Karolina', 'Magda', 'Paulina', 'Kamila']
lista_uczestnikow = []

for uczestnik in uczestnicy:
    zaaktualizuj_liste_uczestnikow(lista_uczestnikow, uczestnik)
print(lista_uczestnikow)

# 07_funkcje
def pole_kola(promien):
    wynik = 3.14 * (promien ** 2)
    return wynik

print(pole_kola(2))

def osoba(imie, nazwisko, tytul):
    imie_nazwisko = imie + ' ' + nazwisko
    return tytul + ' ' + imie_nazwisko.title()

print(osoba('paul', 'smith', 'mr'))


def cena_brutto(cena_netto, vat):
    cala_cena = cena_netto * (1 + vat)
    return cala_cena

print(cena_brutto(15, 23/100))

#08_print

print('ala {} kota'.format('ma'))
