year = int(input())

price = 1000

if year > 2020:
    increase_price = (year - 2020) * 100
    price += increase_price
    print(price)
else:
    print(price)
