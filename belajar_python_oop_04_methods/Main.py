class Hero:
  jumlah_hero = 0

  def __init__(self,inputName,inputHealth,inputPower,inputArmor):
    self.name = inputName
    self.health = inputHealth
    self.power = inputPower
    self.armor = inputArmor
    Hero.jumlah_hero += 1

  # void method, method tanpa return
  def siapa(self):
    print(f"nama hero adalah {self.name}")

  # method dengan argumen
  def healthUp(self,up):
    self.health += up

  # method dengan return
  def getHealth(self):
    return self.health

hero1 = Hero("sniper",100,10,5)
hero2 = Hero("jagernaut",90,5,10)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())