# https://www.youtube.com/watch?v=YQhJsWj6ydU
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(self.name, "은(는)", self.power, "만큼 강하다.")
        
unit = Unit("홍길동", 375)
unit.attack()

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
        
monster = Monster("슬라임", 10, "초급")
monster.attack()