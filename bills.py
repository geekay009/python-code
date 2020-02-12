entry = "y"
name = []
bills = []
Total_amt = 0
print("Please start and enter n to finish entering .. ")
while (entry != "n"):
    entry = input("What is  Store name: ")
    if (entry != "n"):
        bill_amt = int(input("How much is the bill: "))
        Total_amt = Total_amt + bill_amt
        name.append(entry)
        bills.append(bill_amt)

Total_records = len(name)
print("Total number of Bills Entered {}".format(name))
print('Total Bill Amount entered: {}'.format(Total_amt))
