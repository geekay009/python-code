class Employee:
    raise_amount = 1.04
    no_of_empys = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
        Employee.no_of_empys += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)

    # def __rendr__(self, emp_1, emp_2):
    #     return emp_1 + emp_2


emp_1 = Employee('Gaurav', 'Kaushik', 20000)
emp_2 = Employee('Ramesh', 'Sharma', 30000)

print(Employee.no_of_empys)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print(emp_1.__dict__)  # Printing the namespace
# print(Employee.__dict__)
# Employee.raise_amount = 1.05

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.email)
print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
