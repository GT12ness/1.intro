# Python list (zoznam)
"""  
    - a list of comma-separated values (items) between square brackets
    volny preklad: list ciarkou oddelenych hodnot(poloziek) vo vnutri hranatych zatvoriek
    
    - Important thing about a list is that items in a list need not be of the same type.
    volny preklad: dolezite vec na zozname je ze jednotlive polozky zoznamu nemusia byt rovnakeho typu
    
    - Similar to string indices, list indices start at 0, and lists can be sliced, concatenated and so on
    volny preklad: Podobne ako reťazcové indexy, zoznamy indexov začínajú od 0 a zoznamy môžu byť rozdelene,
                    zreťazené a tak ďalej
"""
# ukazka:
list = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7, 7, 9, 10]
list3 = ["a", "b", "c", "d"]

# ulohy na precvicenie:
# 1. access values in lists
print("list1[0]: ", list[0])
print("list2[1:5]: ", list3[1])
print("list2[1:5]: ", list2[2:6])

# 2. Updating Lists
# You can update single or multiple elements of lists
print("Value available at index 2 : ")
print(list[2])
list[2] = 2001
print("New value available at index 2 : ")
print(list[2])

# add values to list - append()
print("stary list:")
print(list)
list.append('python')
list.append(123)
print("novy list:")
print(list)

# 3. Delete List Elements
print("stary list, pred zmazanim:")
print(list)
del list[2]
print("pozmazani hodnoty na indexe 2 : ")
print(list)


"""
     - Lists respond to the + and * operators much like strings
        - the result is a new list, not a string.
"""
L1 = [1, 2, 3]
L2 = [4, 5, 6]

# dlzka retazca
print(len(L1))

# scitanie
print(L1 + L2)

# nasobenie:
print(L1 * 4)
print(["Hi! "] * 3)

# membership - clenstvo
print(3 in L1)
print(3 in L2)

# iteration - iterovanie (opakovanie)
for x in L1:
    print(x)

"""
        Built-in List Functions & Methods:
        Python obsahuje zabudovane methody na pracu s retazcami
        napr.: len(list), max(list), min(list)
         - : list.append(obj) - prida objekt obj do zozname list
         - : list.count(obj) - vrati kolko krat sa obj nachadza v zozname list
         - : list.index(obj) - vrati najmensi index na ktorom sa  obj nachadza v zozname list
         - : list.remove(obj) -  zmaze obj zo zoznamu list
         - : list.reverse() - Prevrati objekty v zozname
         - : list.sort() - zoradi objekty zo zoznamu
"""
# ukazka:
zoznam = [6, 4, 1, 2, 9, 8, 3, 5, 7]
print(zoznam)
print(len(zoznam))
print(max(zoznam))
print(min(zoznam))

zoznam.append(5)
print(zoznam)

pocet = zoznam.count(5)
print(pocet)

index = zoznam.index(5)
print(index)

zoznam.remove(5)
print(zoznam)

zoznam.reverse()
print(zoznam)

zoznam.sort()
print(zoznam)

# Python tuples
"""
        A tuple is a sequence of immutable Python objects.
         Tuples are sequences, just like lists.
         
         volny preklad : tuple(N-tica) je sekvenciou nezmeniteľných objektov Pythonu.
                          Tuples sú sekvencie, rovnako ako zoznamy.
         
          The differences between tuples and lists are, the tuples cannot be changed,
              -  tuples use parentheses, ()
                   whereas lists use square brackets []
                   
        volny preklad:  rozdiel medzi tuples(n-ticami) a zoznamami je ze n-tice nemozu byt zmenene
                            - n-tice pouzivaju klasicke zatvorky ()
                              - listy pouzivaju hrante zatvorky []
"""
# ukazka:
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
print(tup1[0])
print(tup2[1])

tup1[0] = 300
print(tup1[0])

tup3 = tup1 + tup2
print(tup3)

print(len(tup3))
