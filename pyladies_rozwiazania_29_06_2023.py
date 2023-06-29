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