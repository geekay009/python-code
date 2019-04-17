class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('{0} has been born!'.format(self.name))
        Person.population += 1

    def __str__(self):
        return '{0} is {1} is years old.'.format(self.name, self.age)

    def __del__(self):
        print('{0} is dying! :('.format(self.name))
        Person.population -= 1

    def totalPop():
        print('There are {} people in the world.'.format(Person.population))


p1 = Person("Johney", 20)
# print(Person.population)
p2 = Person("Mary", 30)
print(Person.population)
'''
print(p1)
print(p2)
'''
# Person.totalPop()
# print(Person.population)
