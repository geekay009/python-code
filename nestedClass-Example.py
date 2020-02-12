#!/usr/bin/python3


class Outer():

    class Nested():
        def __init__(self, akey):
            self.akey = akey

        def __str__(self):
            specs = {'Brand': 'HP', 'Memory': '8GB', 'OS': 'Windows 10'}
            avalue = specs[self.akey]
            return 'Outer.Nested, name = ' + self.akey + ' Value = ' + avalue

        # def find_dict_value(self):
        #     specs = {'Brand': 'HP', 'Memory': '8GB', 'OS': 'Windows 10'}
        #     avalue = specs[self.akey]
        #     return avalue


n = Outer.Nested('Brand')
# a = Outer.Nested.find_dict_value('Brand')
print(n)
# print(a)
# # def find_dict_value(self):
