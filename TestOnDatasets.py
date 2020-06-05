import random

# load datasets
price = []
rsi = []
tsi = []
macd = []
highestBalance = []
bestValue = []
bestValue2 = []
bestValue3 = []
bestValue4 = []


def load(filename, indicator):
    with open(
        "C:/Users/123/Documents/GitHub/USD-Trader - code/datasets/" + filename, "r"
    ) as fhandle:
        for l in fhandle:
            cPlace = l[:-1]
            indicator.append(cPlace)


# open file and read the content in a list
load("datasetPrice.txt", price)
load("datasetRSIval.txt", rsi)
load("datasetTSI.txt", tsi)
load("datasetMACD.txt", macd)

# testing our strategy
for x in range(5000000):
    rialPocket = 100000
    usdtPocket = 0
    i = 0
    sold = False
    bought = False
    bv = random.choice(range(10)) / -10
    sv = random.choice(range(10)) / 10
    b2v = random.choice(range(30, 50)) + (random.choice(range(10)) / 10)
    s2v = random.choice(range(50, 65)) + (random.choice(range(10)) / 10)

    while True:
        if bought == False and i != 1999:
            if float(rsi[-i]) <= b2v and float(tsi[-i]) <= bv:
                usdtPocket = (rialPocket / int(price[-i])) * 0.9965
                rialPocket -= rialPocket
                bought = True
            i += 1
        else:
            bought = False
            break

    while True:
        if sold == False and i != 1999:
            if float(rsi[-i]) >= s2v and float(tsi[-i]) >= sv:
                rialPocket = (usdtPocket * int(price[-i])) * 0.9965
                usdtPocket -= usdtPocket
                sold = True
            i += 1
        else:
            sold = False
            break
    highestBalance.append(rialPocket)
    bestValue.append(bv)
    bestValue2.append(sv)
    bestValue3.append(b2v)
    bestValue4.append(s2v)


# finding best result
maxi = highestBalance.index(max(highestBalance))
print(
    f"{highestBalance[maxi]}, TSI's: {bestValue[maxi]} {bestValue2[maxi]}, RSI's: {bestValue3[maxi]} {bestValue4[maxi]}"
)
