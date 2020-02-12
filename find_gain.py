first_price = 125
today_price = 200
percent_gain = 0
with open('Test.txt', 'r') as f:
    while True:
        line_text = f.readline()
        if not line_text:
            break
        print(line_text.strip())


def calc_gain():
    price_difference = today_price - first_price
    percent_gain = (price_difference / first_price) * 100
    return percent_gain


print("Percent Gain is {} %".format(calc_gain()))
