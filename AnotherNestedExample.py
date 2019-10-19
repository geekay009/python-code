# class D:
#    value = 5

# class C:
#     def __init__(self):
#         self.value2 = D.value * 5
#         print(self.value2)


class D:
    class C:
        def __init__(self, outer):
            self.outer = outer


d = D()
c = d.C(d)
print('Outer is a {}'.format(type(D)))
print('Inner is a {}', format(type(d.C)))

# from boundinnerclass import BoundInnerClass


# class Outer(object):
#     def method(self):
#         pass

#     @BoundInnerClass
#     class Inner(object):
#         def __init__(self, outer):
#             self.outer = outer


# o = Outer()
# o.method()
# i = o.Inner()
# print('Outer is a {}'.format(type(Outer)))
# print('Inner is a {}', format(type(o.Inner)))
# This last example did not work as it could not find the boundInnerClass
# Traceback (most recent call last):
#   File "C:\Users\Gaurav\Desktop\GK-Python\AnotherNestedExample.py", line 21, in <module>
#     from boundinnerclass import BoundInnerClass
# ImportError: No module named 'boundinnerclass'
