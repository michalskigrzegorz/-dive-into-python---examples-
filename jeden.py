""" Przykłady z książki zanurkuj w Pythonie """

""" tworzymy nowy słownik """
d = {"server":"mpilgrim", "database":"master"}
print (d)

""" podglądamy wartość klucza server """
print (d["server"])

print (d["database"])

d["database"] = "pubs"
print (d)

d["uid"] = "nowa_wartosc"
print (d)

""" dodajemy do słownika nowy klucz i wartość w miejsce losowe """
e = {}
e["klucz"] = "wartość"
print ("To jest słownik E =", e)

""" dodajemy do słownika nowy klucz i wartość w miejsce losowe """
x = {'bazadanych': 'pubs', 'serwer': 'mpilgrim', 'uid': 'sa'}
x['35'] = 'szanel'
print (x)

print (x['35'])

""" tworzymy słownik """
dziennik = {'1': 'Iwona', '2': 'Klaudia', '3': 'Dorota'}
print (dziennik)

""" CLEAR - kasujemy drugi klucz razem z wartością """
del dziennik['2']
print (dziennik)

""" CLEAR - czyścimy cały słownik """
dziennik.clear()
print (dziennik)

""" tworzymy listę """
li = ["a", "b", "mpilgrim", "z", "przykład"]
print (li)

""" wypisujemy na ekran elementy listy: drugi i od drugiego do 4 włącznie """
print (li[2])
print (li[2:5])

""" APPEND - umieszczamy na końcu listy wartość 'korozja' """
lista = ['a', 'b', 'kolor', 'fu', 'zja']
lista.append('korozja')
print (lista)

""" INSERT - umieszczamy na pozycji 3 wartość 'korozja_wczesniej' """
lista.insert(3, 'korozja_wczesniej')
print (lista)

""" rozszerzamy listę li o listę lista, łączymy obie listy """
li.extend(lista)
print (li)

""" EXTEND - rozszerzamy listę literki o nowe wartości """
literki = ['a', 'b', 'c']
literki.extend(['1', '2', '3'])
print (literki)

""" LEN - sprawdzamy długość listy literki, poprawny wynik to 6 elementów """
print (len(literki))

""" INDEX - sprawdzamy gdzie na liście znajduje się wartość 'b' """
print (literki.index('b'))

""" sprawdzamy czy wartosc 'd' istnieje na liście literki """
print ('d' in literki)

""" ### EXTEND, APPEND, INDEX, INSERT to metody listy ### """

""" usuwanie elementów listy """
""" metoda REMOVE """
literki.remove('2')
print (literki)

""" POP - usuwa ostatni element na liście i zwraca jego wartość
dziwne bo zwraca 1, czyli przedostatni element ??? """
print (literki.pop())

""" operatory na listach +, -, *, / """
""" + działa tak samo jak EXTEND, ale EXTEND jest szybszy """
k = ['a', 'b', 'mpilgrim']
k = k + ['przykład', 'nowy', 'stary']
print (k)

""" zwielokrotnianie listy """
cyfry_i_liczby = ['2', '3', '4.5', '14.7', '83']
cyfry_i_liczby = cyfry_i_liczby * 2
print (cyfry_i_liczby)

""" istnieje jeszcze operator += i jest równoważny z EXTEND
cyfry_i_liczby += ['dwa'] to to samo co cyfry_i_liczby.extend(['dwa']) """

""" KROTKI / TUPLE (str. 49/41)
Krotki nie posiadają żadnej metody, oprócz operatora IN """
t = ('a', 'b', 'koko_szanel', 'element')
print (t)

print (t[2])
print (t[1:3])

""" operator IN """
print ('b' in t)

""" Deklarowanie zmiennych (str. 51/43) """
x = 1
print (x)

""" Wielozmienne przypisania """
""" przypisanie jednej krotki do drugiej """
v = ('a', 'b', 'e')
""" v jest krotką z trzech elementów """
(x, y, z) = v
print (x)
print (y)

""" przypisanie kolejnych wartości """
""" wbudowana funkcja RANGE zwraca listę liczb całkowitych """
print (range(7))
(poniedzialek, wtorek, sroda, czwartek, piatek,\
 sobota, niedziela) = range(7)
print (poniedzialek)
print (sroda)
""" dni tygodnia są zdefiniowane w funkcji CALENDAR i CAL """

""" formatowanie łańcucha znaków
%s """
k = "uid"
v = "sa"
print ("%s=%s" % (k, v))

""" formatowanie tekstu a łączenie """
uid = "sa"
pwd = "secret"
""" dwa sposoby łączenia """
print (pwd + " nie jest poprawnym hasłem dla " + uid)
print ("%s nie jest poprawnym hasłem dla %s" % (pwd, uid))

userCount = 4
print ("Użytkowników: %d" % (userCount, ))

"""
%d do liczb całkowitych
%s do łańcucha znaków
%f do liczb rzeczywistych / 6 miejsc po przecinku

przykłady:
"""
print ("Dzisiejsza cena akcji: %f" % 50.4625)
print ("Dzisiejsza cena akcji: %.2f" % 50.4625)
print ("Zmiana w stosunku do dnia wczorajszego: %+.2f" % 1.5)
print ("Zmiana w stosunku do gnia wczorajszego: %-.1f" % 1.7)

""" Odwzorowanie listy + pętla FOR (str. 56 / 48) """
li = [1, 3, 5, 6, 132]
li = [elem*2 for elem in li]
print (li)

""" Funkcje KEYS, VALUES, ITEMS """
params = {'server':'mpilgrim', 'database':'master', 'uid':'sa'}
print (params.keys())
print (params.values())
print (params.items())

""" Wyrażenia listowe """
params = {'server':'mpilgrim', 'database':'master', 'uid':'sa'}
print (params.items())
print ([k for k, v in params.items()])
print ([v for k, v in params.items()])
print (["%s=%s" % (k, v) for k, v in params.items()])

""" Łączenie list i dzielenie łańcuchów znaków """
""" Metoda JOIN """
params = {'server':'mpilgrim', 'database':'master', 'uid':'sa'}
print ("; ".join(["%s=%s" % (k, v) for k, v in params.items()]))

""" Metoda SPLIT / dzielenie """
li = ['server=mpilgrim', 'database=master', 'uid=sa']
s = ";".join(li)
print (s)

print (s.split(";"))
print (s.split(";", 1))

""" Kodowanie znaków (str. 60/53) """
""" Funkcja ORD zwraca liczbę, która odpowiada danemu symbolowi """
print (ord('a'))
""" Funkcja CHR odpowiada jaki znak jest przypisany danej liczbie """ 
print (chr(99))
print (ord('%'))

""" UNIKOD reprezentuje wszystkie znaki jako
2-bajtowe liczby, od 0 do 65535 """

print (ord(u"ą"))
""" funkcja, która nie działa UNICHR """
""" print (unichr(378)) """

errmsg = u"Nie można otworzyć pliku"
print (errmsg)
print (errmsg + u', brak dostępu.')
""" podzielenie unikodu na listę """
print (errmsg.split())
file = "myfile.txt"
print (errmsg + ' ' + file)

""" ENCODE I DECODE """
print (errmsg.encode('iso-8859-2'))
print (errmsg.encode('utf-8'))
msg = errmsg.encode('utf-8')
print (msg.decode('utf-8'))

""" Funkcja INFO
from apichelper import info
li = []
print (info(li)) """

""" Importowanie modułów IMPORT MODULE i FROM MODULE IMPORT
(str. 74/66) """
import types
print (types.FunctionType)

from types import FunctionType
print (FunctionType)

""" Wbudowane funkcje TYPE, STR, DIR i inne / są one
wbudowane w module specjalnym _builtin_ """
print (type(1))
li = []
print (type(li))
slownik = {}
print (type(slownik))
krotka = ()
print (type(krotka))

""" Funkcja STR przekształca dane w łańcuch znaków """
print (str(1))
horseman = ['war', 'pestilence', 'famine']
print (horseman)
horseman.append('Powerbuilder')
print (str(horseman))

""" Funkcja UNICODE pełni tą samą funkcję co STR, ale zamiast
łańcucha znaków tworzy unikod """
""" print unicode(1) - coś nie działa """

""" Funkcja DIR (str. 78/70) - zwraca listę atrybutów
i metod danego obiektu """
li = []
print (dir(li))

d = {}
print (dir(d))

""" Funkcja CALLABLE zwraca True jeżeli dany obiekt
może być wywoływany, a w przeciwnym wypadku False """
import string
""" punctuation - moduł który zawiera wszystkie znaki
przystankowe """
print (string.punctuation)
print (callable(string.punctuation))

""" info(__builtin__, 20) nie działa, trzeba zmienić
lokalizację pliku jeden.py, najlepiej do katalogu
roboczego pythona """

""" Funkcja GETATTR, dzięki niej otrzymujemy referencję
np. do określonej metody """
li = ["Larry", "Curly"]
""" otrzymujemy referencję metody pop """
print (li.pop)
""" zwrot referencji metody pop ...??? """
print (getattr(li, "pop"))

getattr(li, "append")("Moe")
print (li)

print (getattr({}, "clear"))

""" GETATTR nie pracuje na krotkach bo nie posiadają
one żadnej metody """

""" GETATTR funkcja ta jest używana powszechnie jako
funkcja pośrednicząca """

""" Filtrowanie listy """
li = ["a", "mpilgrim", "foo", "b", "c", "d"]
print ([elem for elem in li if len(elem) > 1])
"""
print ([elem for elem in li if elem != "b"])
print ([elem for elem in li if li.count(elem) == 1])
"""

""" Operatory AND i OR
Odpowiadają boolowskim operacjom logicznym, jednak nie zwracają wartości
logicznych
"""

""" AND - Jeżeli wszystkie wartości w kontekście logicznym są prawdą AND
zwraca ostatnią wartość, a czyta od lewej do prawej """
print ('a' and 'b')

""" Dziwny przypadek bo wg. książki AND powinno zwrócić '' """
print ('' and 'b')

""" Wszystkie są prawdziwe, zwraca ostatnią """
print ('a' and 'b' and 'c')

""" OR - Jeżeli jakaś wartość jest prawdą OR zwraca tą wartość
natychmiast """
print ('a' or 'b')

""" OR wyznacza '' jako fałsz, ale potem 'b' jako prawdę i zwraca 'b' """
print ('' or 'b')

""" Jeśli wszystkie wartości są fałszem OR zwraca ostatnią wartość """
print ('' or [] or {})

""" Sztuczka AND-OR """
a = "first"
b = "second"
print (1 and a or b)
print (0 and a or b)

""" Upewnienie się czy wartość a nigdy nie jest fałszywa """
""" jest jakiś błąd, nie zwraca nic """
a = " " 
b = "second"
print ((1 and [a] or [b])[0])


""" Wyrażenie LAMBDA (str. 89/81)
Pobiera dowolną liczbę argumentów i zwraca wartość, którą otrzymujemy
po wykonaniu pojedynczego wyrażenia """
""" definicja jednolinijkowej mini-funkcji """
def f(x):
    return x*2
print (f(3))

""" lub / to samo """
g = lambda x: x*2
print (g(3))

""" lub """
print ((lambda x: x*2)(3))

""" SPLIT bez argumentów """
s = "this is\na\ttest"
print (s)

print (s.split())

print (" ".join(s.split()))

""" UNIKOD w notkach dokumentacyjnych 93/85 """
def foo(): print (2)
foo()

foo.__doc__
foo.__doc__ == None

""" w SQL musimy skorzystac z IS NULL zamiast z = NULL
aby porownac cos z pusta wartoscia.
W Pythonie mozemy uzyc albo == None albo is None, lecz
is None jest szybsze """

""" Poznajemy LJUST """
""" ljust wypełnia napis spacjami do zadanej długości """
s = 'buildConnectionString'
print (s.ljust(30))
print (s.ljust(20))

""" Wypisywanie listy 94/86"""
li = ['a', 'b', 'c']
print ("\n".join(li))


""" ---------------------------- POWTÓRKA ------------------------------ """
