class Outer(object):

        # o = Outer()
        # self.i = self.Inner(outer)

    def show_method(self):
        pass
        # if __name__ == '__main__':
        #    o = Outer('memory')
        #    print("The Value from specs is {}".format(o.i.find_value_from_dict()))

    class Inner(object):
        def __init__(self, outer, akey):
            self.outer = outer
            self.akey = akey

        def find_dict_value():
            specs = {'Brand': 'HP', 'Memory': '8GB', 'OS': 'Windows 10'}
            avalue = specs[self.akey]
            return avalue


o = Outer()
i = o.Inner(o, 'Brand')
o.show_method(i)
print('Outer is a {}'.format(type(Outer)))
print('Inner is a {}', format(type(o.Inner)))

# class Outer(object):
#     def method(self):
#         pass


#     class Inner(object):
#         def __init__(self, outer):
#             self.outer = outer


# o = Outer()
# o.method()
# i = o.Inner()
# print('Outer is a {}'.format(type(Outer)))
# print('Inner is a {}', format(type(o.Inner)))
