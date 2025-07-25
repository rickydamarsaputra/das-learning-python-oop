class Hero:
  # private class variable
  __jumlah = 0

  def __init__(self,name):
    self.__name = name
    Hero.__jumlah += 1

  # method ini hanya berlaku untuk objek
  def getJumlah(self):
    return Hero.__jumlah
  
  # method ini tidak berlaku untuk objek tapi berlaku untuk class
  def getJumlah1():
    return Hero.__jumlah
  
  # method static (decorator)
  @staticmethod
  def getJumlah2():
    return Hero.__jumlah
  
  @classmethod
  def getJumlah3(cls):
    return cls.__jumlah

sniper = Hero("sniper")
print(Hero.getJumlah2())
rikimaru = Hero("rikimaru")
print(rikimaru.getJumlah2())
drowranger = Hero("drowranger")
print(drowranger.getJumlah3(), Hero.getJumlah3())