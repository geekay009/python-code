def add_two(a,b):
    return a+b

a = int(input("please enter your first number: "))
b = int(input("please enter your second number: "))
sum=add_two(a,b)
print ("Total amount of two numbers is {}". format(sum))

r=lambda n: n*n 
result=r(5)
print (result)
s=lambda a,b: a+b
result=s(5,6)
print (result)
