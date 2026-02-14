import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет меня зовут {self.name}, мне {self.age} лет")


class Student(Person):
    def __init__(self, name, age, knowledge=0):
        super().__init__(name, age)
        self.knowledge = knowledge  

    def study(self):
        gain = random.randint(5, 15)
        self.knowledge += gain
        print(f"{self.name} учится и получает +{gain} знаний (всего {self.knowledge})")

    def relax(self):
        loss = random.randint(1, 5)
        self.knowledge = max(0, self.knowledge - loss)
        print(f"{self.name} отдыхает и теряет -{loss} знаний (всего {self.knowledge})")



class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"В университет {self.name} зачислен {student.name}")

    def study_day(self):
        print(" Учебный день")
        for student in self.students:
            if random.random() > 0.3:
                student.study()
            else:
                student.relax()

    def show_rating(self):
        print(" Рейтинг студентов:")
        sorted_students = sorted(
            self.students,
            key=lambda s: s.knowledge,
            reverse=True
        )
        for s in sorted_students:
            print(f"{s.name}: {s.knowledge}")



uni = University("супер универ")

s1 = Student("тимур", 18)
s2 = Student("жека", 19)
s3 = Student("али", 20)

uni.add_student(s1)
uni.add_student(s2)
uni.add_student(s3)


for day in range(5):
    uni.study_day()

uni.show_rating()
