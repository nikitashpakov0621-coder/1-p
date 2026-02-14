class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50     
        self.energy = 50    
        self.mood = 50      

    def eat(self):
        print(f"{self.name} кушает ")
        self.hunger = max(0, self.hunger - 20)
        self.energy = min(100, self.energy + 10)
        self.mood = min(100, self.mood + 5)

    def sleep(self):
        print(f"{self.name} спит ")
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 10)

    def play(self):
        print(f"{self.name} играет ")
        self.energy = max(0, self.energy - 20)
        self.hunger = min(100, self.hunger + 15)
        self.mood = min(100, self.mood + 20)

    def status(self):
        print(f"""
Котик {self.name}:
  Голод: {self.hunger}
  Энергия: {self.energy}
  Настроение: {self.mood}
""")
