class Animal:
    def __init__(self, name):
        self.name = name  

    def eat(self):
        print(f"{self.name} кушает корм")

    def sleep(self):
        print(f"{self.name} отключён")



class Robot:
    def __init__(self, battery_level):
        self.battery_level = battery_level  

    def charge(self):
        self.battery_level = 100
        print("Батарея заряжена на максимум")

    def show_battery(self):
        print(f"Уровень батареи: {self.battery_level}%")


class RoboPet(Animal, Robot):
    def __init__(self, name, battery_level, model):
        Animal.__init__(self, name)
        Robot.__init__(self, battery_level)
        self.model = model  

    def introduce(self):
        print(f"Я {self.name}, супермодель {self.model}.")

    def full_status(self):
        print(" Статус пета ")
        self.introduce()
        self.show_battery()



pet = RoboPet("Бум", 50, "supra_rx7")

pet.eat()           
pet.sleep()         
pet.charge()        
pet.show_battery()  
pet.introduce()     
pet.full_status()   
