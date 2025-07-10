class Hero:
  # class variable
  jumlah = 0

  def __init__(self, inputName, inputHealth, inputPower, inputArmor):
    # instance variable
    self.name = inputName
    self.health = inputHealth
    self.power = inputPower
    self.armor = inputArmor
    Hero.jumlah += 1
    print(f"membuat Hero dengan nama {inputName}")

hero1 = Hero("sniper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("jagernaut", 500, 100, 5)
print(Hero.jumlah)