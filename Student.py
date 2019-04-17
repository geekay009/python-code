class Student:
    attendance = 0
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.attend = 0
        attendance = 0
        print("Hello My name is {0}".format(self.name))

    def addGrade(self, grade):
        self.grades.append(grade)

    def attendDay(self):
        self.attend += 1
        Student.attendance += 1

    def getAverage(self):
        return sum(self.grades) / len(self.grades)


student1 = Student("Gaurav")
student2 = Student("Vikas")

for x in range(1, 11):
    student1.attendDay()
print ("The attendance is {0}".format(Student.attendance))

print("The variable student1.attend ", student1.attend)
student1.addGrade(45)
student1.addGrade(90)
student1.addGrade(30)
student1.addGrade(40)
student1.addGrade(85)

print(student1.grades)
print(student1.getAverage())


student1.name
student2.name
