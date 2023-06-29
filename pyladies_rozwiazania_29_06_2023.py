# Zamien liste imion na liste nazwisk

list_of_names = ['Paul', 'Jake', 'Carl', 'Loona']
list_of_surnames = ['Smith', 'Brad', 'Pitt', 'John']

def change_names_to_surnames(old_list, new_list):
    ostatni_element = len(old_list)
    for name in range(ostatni_element):
        old_list[name] = new_list[name]
    return old_list

print(change_names_to_surnames(list_of_names, list_of_surnames))


# Operacje na plikach

plik_z_lista_imion = open('lista_imion.txt')
# lista_imion = []

# for linia in plik_z_lista_imion:
#     lista_imion.append(linia.replace('\n', ''))


# list comprehension

lista_imion = [linia_nazwiska.replace('\n','') for linia_nazwiska in plik_z_lista_imion]
print(lista_imion)

def wczytaj_do_listy_ze_sciezki(sciezka):
    plik_lista = open(sciezka)
    lista = [linia.replace('\n', '') for linia in plik_lista]
    return lista

wczytana_lista_imion = wczytaj_do_listy_ze_sciezki('lista_imion.txt')
wczytana_lista_nazwisk = wczytaj_do_listy_ze_sciezki('lista_nazwisk.txt')
print(wczytana_lista_imion)
print(wczytana_lista_nazwisk)

lista_liczb_podniesionych_do_kwadratu = [liczba ** 2 for liczba in range(1, 6)]
print(lista_liczb_podniesionych_do_kwadratu)


#Funkcja, ktora dla argumentu sciezki dla listy imion i listy nazwisk,
#zwroci liste imion i nazwisk.

def zamien_imiona_na_nazwiska_ze_sciezki(sciezka_imion, sciezka_nazwisk):
    wczytana_lista_imion = wczytaj_do_listy_ze_sciezki(sciezka_imion)
    wczytana_lista_nazwisk = wczytaj_do_listy_ze_sciezki(sciezka_nazwisk)
    nowa_lista = change_names_to_surnames(wczytana_lista_imion, wczytana_lista_nazwisk)
    return nowa_lista

lista_ze_sciezek = zamien_imiona_na_nazwiska_ze_sciezki("lista_imion.txt", "lista_nazwisk.txt")
print(lista_ze_sciezek)

imie = 'Dorota'

#11_tuples

waluty = ('PLN', 'USD')
#waluty.remove('PLN')
#nie da się zmieniać tupli

waluty_lista = []

def tuple_to_list(tuple, list):
    for currency in tuple:
        list.append(currency)
    return list

print(tuple_to_list(waluty, waluty_lista))

#list comprehension zamiast linii 66 i 67:
#list = [currency for currency in tuple]


# 12_prawda_i_falsz

try:
    liczba = int(input("Podaj liczbę:"))
    print(f"Twoja liczba to {liczba}!")
except ValueError:
    print("Nie podawaj liczby innej niż całkowita.")

#13_slowniki

def zwroc_wartosc_pod_kluczem(slownik, klucz):
    try:
        return slownik[klucz]
    except KeyError:
        print("Prosze podac klucz, ktory jest w slowniku.")

slownik = {'drzewo' : 'klon', 'budynek' : 'kamienica'}
klucz = 'kwiat'
zwrocona_wartosc = zwroc_wartosc_pod_kluczem(slownik, klucz)
print(zwrocona_wartosc)


def iterowanie_po_kluczach_slownika(dictionary):
    for slownik_key in dictionary:
        return slownik.keys()

print(iterowanie_po_kluczach_slownika(slownik))

for klucz, wartosc in slownik.items():
    print(f"Klucz:{klucz}")
    print(f"Wartość:{wartosc}")



