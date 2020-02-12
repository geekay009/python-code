"""
Google Share Price URL
https://goo.gl/3zaUlD
path = "F:\data\google_stock_data.csv"
path = "C:\Users\Gaurav\Desktop\GK-Python\


Now reading the file, picking individual lines, splitting on comma etc
lines = [line for line in open(path)]
lines[0]
'Date,Open,High,Low,Close,Volume,Adj Close\n'
lines[1]
'8/19/2014,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n'
lines[0].strip()
'Date,Open,High,Low,Close,Volume,Adj Close'
lines[0].strip().split(',')
['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
#Now not only removing white spaces, new lines etc but putting all data(line) in a list
dataset = [line.strip().split(',') for line in open(path)]
dataset[0] = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
dataset[1] =
['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '086.862643']
But list value items are stings here

Now delve into csv so that you could identify each column as right datatype and not splitting
a column because a comma is inside the column content string

import csv
now to check what functions etc the csv module contains
print (dir(csv))
It will show many functions among which there are reader and writer functions

import csv
path = "F:\data\google_stock_data.csv"
file = open(path, newline='') #notice that '' is used for newline char. It is an empty string. It ensures
                              #fully working on both \n in unix and \n\r in windows 
reader= csv.reader(file)
#First line is just a header so we have to ignore and go to next  line like this
header = next(reader)
data = [row for row in reader] #Reading the remaining data
print(header)
print(data[0])
#It prints the lines as earlier shown
#['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
#['8/19/2014', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '086.862643']
#i.e in a list

#so, to parse the date we import datetime library module as well This is additional code to above
import datetime

data = []
for row in reader:
  #row = [Date, Open, High, Low, Close, Volume, Adj Close]
  #So, let us extract date from the first row, first column, giving the format that we want using a func
  date       = datetime.strptime(row[0], '%m/%d/%Y')
  open_price = float(row[1])
  high       = float(row[2])
  low        = float(row[3])
  close      = float(row[4])
  volume     = int(row[5])
  adj_close  = float(row[6])

  data.append([date, open_price, high, low, close, volume, adj_close])
  print(data[0])  #It prints the data is appropriate datatype for each column

  #Let us compute % daily return of stock and store it

  returns_path = "google_returns.csv"
  file = open (returns_path, 'w')
  writer = csv.writer(file)
  #Let us write the header first
  writer.writerow(["Date", "Return"])
  #As we need previous date price to work out return, so we will stop at the last but one row or the first row
  for i in range(len(data) - 1):
    todays_row     = data[i]
    todays_date    = todays_row[0]
    todays_price   = todays_row[-1]
    yesterdays_row   = data[i+1]
    yesterdays_price = yesterdays_row[-1]


    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date. daily_return])


