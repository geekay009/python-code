class Stu:

    def __init__(self, name):
        self.name = name
        self.attend = 0
        self.grades = []
        print("Hello My Name is {0}".format(self.name))

    def addGrade(self, grade):
        self.grades.append(grade)


Stu1 = Stu("Gaurav")
Stu2 = Stu("Vikas")

Stu1.addGrade(45)
Stu1.addGrade(30)

print(Stu1)
print(Stu2)
print(Stu1.grades)
