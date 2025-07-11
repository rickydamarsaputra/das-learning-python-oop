class Hero:
  def __init__(self,name,health,attackPower):
    self.__name = name
    self.__health = health
    self.__attPower = attackPower

  # getter
  def getName(self):
    return self.__name
  
  def getHealth(self):
    return self.__health
  
  def getAttPower(self):
    return self.__attPower
  
  # setter
  def diserang(self,serangPower):
    self.__health -= serangPower

  def setAttPower(self,nilaiBaru):
    self.__attPower = nilaiBaru

# awal dari game
earthshaker = Hero("earthshaker",50,5)
print(earthshaker.__dict__)

# game berjalan
print(earthshaker.getName())

print(earthshaker.getHealth())
earthshaker.diserang(5)
print(earthshaker.getHealth())

print(earthshaker.getAttPower())
earthshaker.setAttPower(15)
print(earthshaker.getAttPower())