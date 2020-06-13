import random

# load datasets
price = []
rsi = []
tsi = []
macd = []
bb = []


def load(filename, indicator):
    f = open("../datasets/"+filename, "r")
    for l in f:
        cPlace = l[:-1]
        indicator.append(cPlace)
    f.close()


# open file and read the content in a list
load("datasetPrice.txt", price)
load("datasetRSIval.txt", rsi)
load("datasetTSI.txt", tsi)
load("datasetMACD.txt", macd)
load("datasetBB.txt", bb)

# testing our strategy
for x in range(1):
    rialPocket = 100000
    usdtPocket = 0
    i = 0
    sold = False
    bought = False
while i != 3809:
    while True:
        if bought == False and i != 3809:
            if (
                float(rsi[-i]) <= 47
                and float(tsi[-i]) <= -0.1
                and float(macd[-i])/10 >= 7
                and float(int(bb[-i])/100) >= 6
            ):
                usdtPocket = (rialPocket / int(price[-i])) * 0.9965
                rialPocket -= rialPocket
                print(
                    f"B ! usdt={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={float(macd[-i])/10}, BB={float(bb[-i])/100}, {usdtPocket}, {i}"
                )
                bought = True
            i += 1
        else:
            bought = False
            break

    while True:
        if sold == False and i != 3809:
            if (
                float(rsi[-i]) >= 70
                and float(tsi[-i]) >= 0.6
                and float(macd[-i])/10 >= 8
                and float(int(bb[-i])/100) >= 6
            ):
                rialPocket = (usdtPocket * int(price[-i])) * 0.9965
                usdtPocket -= usdtPocket
                print(
                    f"S ! usdt={int(price[-i])}, RSI={rsi[-i]}, TSI={tsi[-i]}, MACD={float(macd[-i])/10}, BB={float(bb[-i])/100}, {rialPocket}, {i}"
                )
                sold = True
            i += 1
        else:
            sold = False
            break

if rialPocket == 0:
    rialPocket = usdtPocket * 17800
# finding best result
print(f"balance: {rialPocket}")