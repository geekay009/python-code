mydict={"firstKey":"firstValue",
        "secondKey":"secondValue",
         "thirdKey":"thirdValue"}

for i in mydict:
    print (i)
    print ("value for this key: {}".format(mydict[i]))    

print ("Now trying Again.....")
for x in mydict.values():
    print(x)

print()
print ("Now trying Again.....")
for x in mydict.keys():
    print (x)

print()
print ("Now trying Again.....")
for x in mydict.items():
    print (x)

print ("Length of this Dictionary is : {}".format(len(mydict)))

x=raw_input("Value for What key would you like to find:")

