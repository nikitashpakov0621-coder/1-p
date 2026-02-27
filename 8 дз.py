import logging
import random

logging.basicConfig(level=logging.INFO)

class Person:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        logging.info(f"{self.name} создан")

    def act(self):
        if random.random() > 0.5:
            self.energy -= 10
            logging.info(f"{self.name} учится. Энергия {self.energy}")
        else:
            self.energy += 5
            logging.info(f"{self.name} отдыхает или играет . Энергия {self.energy}")



people = [Person("кирилл"), Person("гамид"), Person("никита")]

for step in range(3):
    logging.info(f" {step+1}")
    for p in people:
        p.act()