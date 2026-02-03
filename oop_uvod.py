"""# vytvořením třídy jsme NEvytvořili žádný objekt
class Auto: # třída ("šablona") pro objekty Auto
  def __init__ (self, x, y, nazev): # tato metoda se spustí při vytváření objektu
    self.pozice = [x,y]
    self.hp = 0
    self.nazev = nazev

  def __str__(self): # speciální metoda __str__() určuje, jak se objekt převede na string
    return "Auto {} s hp {} na pozici {}".format(self.nazev, self.hp, self.pozice)

auto1 = Auto(0,0,"Škodovka") # zde vytváříme objekt typu Auto - tedy spouštíme metodu __init__() ve třídě Auto
auto2 = Auto(10,20,"Trabant")
auto3 = Auto(300,400,"Ferrari")

print(auto1, type(auto1)) # funkce print() vždy tiskne string - zavolá se tedy metoda __str__() a vrácený string se zobrazí
print(auto2, type(auto2))
print(auto3, type(auto3))

# pro spuštění této buňky musíte předtím alespoň jednou spustit buňku, ve které se vytváří objekty auto1, auto2 a auto3
print("Auto1: x:", auto1.pozice[0], "y:", auto1.pozice[0], "hp:", auto1.hp, "nazev:", auto1.nazev)
print("Auto2: x:", auto2.pozice[0], "y:", auto2.pozice[0], "hp:", auto2.hp, "nazev:", auto2.nazev)
print("Auto3: x:", auto3.pozice[0], "y:", auto3.pozice[0], "hp:", auto3.hp, "nazev:", auto3.nazev)


class Zeton:
  def __init__(self, pozice_x, pozice_y, hodnota):
    self.pozice = [pozice_x, pozice_y]
    self.hodnota = hodnota


# Dále už kód neměňte
vsechny_zetony = []
for i in range(0, 5):
  vsechny_zetony.append(Zeton(-i, 10 * i, 7 * i))

print("Existuje {} Žetonů:".format(len(vsechny_zetony)))
for i, z in enumerate(vsechny_zetony):
  print("{}. pozice: {} hodnota {}".format(i + 1, z.pozice, z.hodnota))
"""
"""
class Zeton:
  def __init__(self, hodnota):
    self.__hodnota = hodnota

### Dále kód neupravujte !!!
try:
  Z1 = Zeton(10)
  expected_var = "hodnota"
  all_vars = dir(Z1)
  if "_Zeton__"+expected_var in all_vars:
    print("V pořádku")
  elif expected_var in all_vars:
    print(expected_var, "není skrytý atribut")
  elif "_"+expected_var in all_vars:
    print("_"+expected_var, "není skrytý atribut")
  else:
    print(expected_var, "nenalezeno")
except NameError as e:
  print("Třída Zeton nenalezena")
except TypeError as e:
  print("Třída Zeton má příjmat jeden argument při vytváření")
"""

# TODO: Zde vytvořte třídu dle zadání
class Zeton:
  def __init__(self, hodnota):
    self.h = hodnota

  @property
  def h(self):
    return self._h

  @h.setter
  def h(self, hod):
    self._h = max(hod, 50)


### Dále kód neupravujte !!!
Z1 = Zeton(10)
if Z1.h != 50:
  print("Při vytváření Žetonu je potřeba hodnotu zkontrolovat - dostala se do něj hodnota", Z1.h)
else:
  Z1.h = 20
  if Z1.h != 50:
    print("Při úpravě Žetonu je potřeba hodnotu zkontrolovat - dostala se do něj hodnota", Z1.h)
  else:
    Z1._h = 60
    if Z1.h != 60:
      print("Zakázané hodnoty jsou pouze 49 a méně - očekávaná hodnota je 60, skutečná hodnota:", Z1.h)
    else:
      print("V pořádku")