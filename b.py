
for x in range(4):
    for y in range(3):
        print('({},{})'.format(x, y))


class animal:
    def walk(self):
        print("I am walking")


class Dog(animal):
    def bark(self):
        print("bhon Bhon!!!")


class Cat(animal):
    def talk(self):
        print("Miao, Miao..")


d1 = Dog()
d1.bark()
d1.walk()
c1 = Cat()
c1.talk()
c1.walk()
