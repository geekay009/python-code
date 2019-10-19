entry = "y"
name = []
print("Please start and enter n to finish entering .. ")
while (entry != "n"):
    entry = input("What is your name: ")
    if (entry != "n"):
        name.append(entry)

for aname in name:
    print("your name is {}".format(aname))
Total_records = len(name)
print('Total name entered: {}'.format(Total_records))
